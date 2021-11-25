from collections.abc import Iterator
from . import Player
import requests
import json
import os
from dotenv import load_dotenv
 
class PlayerDB(Iterator):
    """retrieve NBA player data from the defined endpoint.Allows to make filtered
    queries(by the NBA player height in inches) to the data retrieved. Extends 
    from Iterator making the data search more easy. 

    Args:
        __data (List[Player]): Store sorted by height NBA Player(Player objects) created from the data retrieved.
        __position (int): Encode the actual position during iterations.
        __height_init_pos(Dict[int, int]): Enconde the first appearance position of a specificed height within __data atribute.
        __height_final_pos(Dict[int, int]): Enconde the last appearance position of a specificed height within __data atribute.
    """
    def __init__(self) -> None:
        self.__position = 0
        self.__data = []
        self.__height_final_pos = {}
        self.__height_init_pos = {}
        self.__load()
    
    def __next__(self):
        try:
            player = self.__data[self.__position]
            self.__position += 1
        except IndexError:
            raise StopIteration()
                
        return player
    
    def __iter__(self):
        return self 
    
    def __check_data_server_connection(self, url:str) -> None:
        try:
            requests.head(url, timeout=3)
        except requests.ConnectionError:
            raise ValueError("No internet connection")            
            
    def __request_player_data(self, url:str) -> str:
        try:
            request_response = requests.get(url)
            return request_response.text
        except requests.RequestException:
            raise ValueError("Has occurred a problem while trying to get the data")     
    
    def __transform_json(self, data_text: str) -> None:
        try:
            transform_data = json.loads(data_text)
            for json_object in transform_data["values"]:
                player = Player(**json_object)            
                self.__data.append(player)
        except Exception:            
            raise ValueError("Data was corrupt")
              
    def __load(self) -> None:
        """Retrieve NBA player data from the defined endpoint,
        this data is in json data and using data populate __data,
        __height_init_pos and __height_final_pos.
        """
        load_dotenv()
        url = os.getenv("DATA_URL")
        self.__check_data_server_connection(url)
        response_text = self.__request_player_data(url)
        self.__transform_json(response_text)            
        
        def sorting_atribute(player:Player):
            return player.get_height_inches()
        
        self.__data = sorted(self.__data, key=sorting_atribute)
        for index, player in enumerate(self.__data):
            height_inches = player.get_height_inches()
            self.__height_final_pos[float(height_inches)] = index
            if not height_inches in self.__height_init_pos:
                self.__height_init_pos[height_inches] = index            
                         
    def filter(self, height: float):
        """Filter and return a set of NBA players(Player objects) by a height
        in inches.
         
        Returns:
            [Player]: Set of NBA players which meet the height filter, in case of no 
            NBA player meet the filter returns None.
            [init_pos]: Encode the first appearance position of the filtered height within the __data attribute.
            In case of no NBA plater meet the filter returns -1.
        """        
        if not height in self.__height_init_pos:
            return None, -1
        init_pos = self.__height_init_pos[height]
        final_pos = self.__height_final_pos[height]
        return self.__data[init_pos:final_pos+1], init_pos
    

      