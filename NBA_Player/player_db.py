from collections.abc import Iterator
from . import Player
import requests
import json
import os
from dotenv import load_dotenv
 
class PlayerDB(Iterator):
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

    def set_position(self, position:int):
        if position < len(self.__data):
            self.__position = position
        #else:
            #raise an error
   
    def __load(self) -> None:
        load_dotenv()
        url = os.getenv("DATA_URL")
        request_response = requests.get(url)
        request_data = json.loads(request_response.text)
        for json_object in request_data["values"]:
            player = Player(**json_object)            
            self.__data.append(player)     
        
        def sorting_atribute(player:Player):
            return player.get_height_inches()
        
        self.__data = sorted(self.__data, key=sorting_atribute)
        for index, player in enumerate(self.__data):
            height_inches = player.get_height_inches()
            self.__height_final_pos[float(height_inches)] = index
            if not height_inches in self.__height_init_pos:
                self.__height_init_pos[height_inches] = index            
                         
    def filter(self, height: float):
        if not height in self.__height_init_pos:
            return None
        init_pos = self.__height_init_pos[height]
        final_pos = self.__height_final_pos[height]
        return self.__data[init_pos:final_pos+1], init_pos, final_pos
    

      