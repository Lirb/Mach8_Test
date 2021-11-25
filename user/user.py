
from player import PlayerDuo
from player import PlayerDB

class User:
    def __init__(self, total_height: float) -> None:
        self.__query_result = []
        self.__DB = PlayerDB() 
        self.__total_height = total_height
                     
    def list_query_results(self) -> str:
        str_result_list = ""
        if len(self.__query_result) == 0:
            raise ValueError("No matches found")
        for nba_duo in self.__query_result:
            str_result_list += str(nba_duo)
        return str_result_list
    
    def query(self) -> None: 
        initial_pos = 0       
        for index, player_1 in enumerate(self.__DB):
            if index == 0 or player_space is None:
                player_space, initial_pos, _ = self.__DB.filter(self.__total_height - player_1.get_height_inches())
            else:
                if index == initial_pos:
                    break
                player_space, _, _ =  self.__DB.filter(self.__total_height - player_1.get_height_inches())
            if player_space is not None:
                for player_2 in player_space:
                    try:
                        player_duo =  PlayerDuo(player_1, player_2)
                        self.__query_result.append(player_duo)
                    except Exception:
                        continue
                        
            
            
            
            
                    