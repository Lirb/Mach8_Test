
from player import PlayerDuo
from player import PlayerDB

class User:
    """Represent a user, which query for two NBA players, which heights adds up
    to an user defined height in inches.
    
     Args:
        __query_result(List[PlayerDUO]): Store all set of different NBA
        players, which adds up to __total_height.
        __DB (PlayerDB): Allow to filter and iterate throught the NBA player database Encode the actual position during iterations.
        __total_height(float): Enconde the user definded height to execute the query.        
    
    """
    def __init__(self, total_height: float) -> None:
        self.__query_result = []
        self.__DB = PlayerDB() 
        self.__total_height = total_height
                     
    def list_query_results(self) -> str:
        """Build a string with the __query_result content.

        Raises:
            ValueError: In case of query result be empty raise "Not matches found".

        Returns:
            str: Representation of the __query_result_content.
        """
        str_result_list = ""
        if len(self.__query_result) == 0:
            raise ValueError("No matches found")
        for nba_duo in self.__query_result:
            str_result_list += str(nba_duo)
        return str_result_list
    
    def query(self) -> None:
        """Search in the NBA player database(PlayerDB object) for each pair of
        NBA players(Player object) which height adds up to __total_height.
        
        This method iterate through the NBA players database(PlayerDB) and for each player(player_1) in the database, filter it 
        looking for those NBA players whith a height equal to __total_height minus his height (both heights in inches), if the filter returns
        NBA players that meet the condition create pairs of players(PlayerDuo) with each of them 
        ([player_1, player_filtered_1], [player_1, player_filtered_2],....[player_1, player_filtered_n]) and append these pairs to __query_result.    
        """ 
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
                        
            
            
            
            
                    