from typing import List
from NBA_Player import NBA_player_duo
import NBA_Player
from NBA_Player.NBA_player_DB import NBA_player_DB
class User:
    def __init__(self) -> None:
        self.__total_height = 0.0
        self.__query_result = []
        self.__DB = NBA_player_DB() 
        
    def setTotalHeight(self, total_height: float) -> None:
        self.__total_height = total_height
        
    def listQueryResults(self) -> str:
        str_result_list = ""
        for nba_duo in self.__query_result:
            str_result_list += str(nba_duo)
        return str_result_list
    
    def query(self):        
        for index, nba_player_1 in enumerate(self.__DB):
            if index == 0:
                NBA_player_space, initial_pos, _ = self.__DB.filter(self.__total_height - nba_player_1.getHeightInches())
            else:
                NBA_player_space, _, _ =  self.__DB.filter(self.__total_height - nba_player_1.getHeightInches())
            for nba_player_2 in NBA_player_space:
                self.__query_result.append(NBA_player_duo(nba_player_1,nba_player_2))
            if index == initial_pos:
                break
            
            
                    