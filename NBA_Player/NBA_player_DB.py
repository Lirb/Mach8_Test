from collections.abc import Iterator, Iterable
from . import NBA_player
import requests
import json
import os
from dotenv import load_dotenv
 
class NBA_player_DB(Iterator):
    def __init__(self) -> None:
        self.__position = 0
        self.__data = []
        self.__height_final_pos = {}
        self.__height_init_pos = {}
        self.__load()
    
    def __next__(self):
        try:
            nba_player = self.__data[self.__position]
            self.__position += 1
        except IndexError:
            raise StopIteration()
        
        return nba_player
    
    def __iter__(self):
        return self 

    def setPosition(self, position:int):
        if position < len(self.__data):
            self.__position = position
        #else:
            #raise an error
   
    def __load(self) -> None:
        load_dotenv()
        url = os.getenv("DATA_URL")
        request_response = requests.get(url)
        request_data = json.loads(request_response.text)
        for jsonObject in request_data["values"]:
            nba_player = NBA_player(**jsonObject)            
            self.__data.append(nba_player)     
        
        def sortingAtribute(nba_player:NBA_player):
            return nba_player.getHeightInches()
        
        self.__data = sorted(self.__data, key=sortingAtribute)
        print("Hola")
        for index, nba_player in enumerate(self.__data):
            height_inches = nba_player.getHeightInches()
            self.__height_final_pos[float(height_inches)] = index
            if not height_inches in self.__height_init_pos:
                self.__height_init_pos[height_inches] = index            
                         
    def filter(self, height: float):
        if not height in self.__height_init_pos:
            return None
        init_pos = self.__height_init_pos[height]
        final_pos = self.__height_final_pos[height]
        return self.__data[init_pos:final_pos], init_pos, final_pos
    

      