import NBA_player
import requests
import json
import os
from dotenv import load_dotenv 
 
class NBA_player_DB:
    def __init__(self) -> None:
        self.__data = []
   
    def __load(self) -> None:
        load_dotenv()
        url = os.getenv("DATA_URL")
        request_response = requests.get(url)
        request_data = request_response.json()
        print(request_data)
        
    def filter(self, total_height: float):
        return self.__data        
        
    def getData(self):
        return self.__data
      