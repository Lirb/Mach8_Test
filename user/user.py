from typing import List
from NBA_Player import NBA_player_duo
class User:
    def __init__(self) -> None:
        self.__total_height = 0.0
        self.__query_result = []
        
    def setTotalHeight(self, total_height: float) -> None:
        self.__total_height = total_height
        
    def listQueryResults(self) -> str:
        str_result_list = ""
        for nba_duo in self.__query_result:
            str_result_list += str(nba_duo)
        return str_result_list
     