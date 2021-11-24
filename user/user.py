
from NBA_Player import PlayerDuo
from NBA_Player import PlayerDB

class User:
    def __init__(self, total_height: float) -> None:
        self.__query_result = []
        self.__DB = PlayerDB() 
        self.__total_height = total_height
                     
    def list_query_results(self) -> str:
        str_result_list = ""
        for nba_duo in self.__query_result:
            str_result_list += str(nba_duo)
        return str_result_list
    
    def query(self): 
        initial_pos = 0       
        for index, player_1 in enumerate(self.__DB):
            if index == 0:
                player_space, initial_pos, _ = self.__DB.filter(self.__total_height - player_1.get_height_inches())
            else:
                if index == initial_pos:
                    break
                player_space, _, _ =  self.__DB.filter(self.__total_height - player_1.get_height_inches())
            for player_2 in player_space:
                self.__query_result.append(PlayerDuo(player_1, player_2))
            
            
            
            
                    