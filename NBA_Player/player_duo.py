from .player import Player

class PlayerDuo:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.__player_1 = player_1
        self.__player_2 = player_2
        self.__height_sum =  self.__player_1.get_height_inches() + self.__player_2.get_height_inches()
    
    def __str__(self) -> str:
        return f"- {self.__player_1}\t{self.__player_2}\n"
    
    def __repr__(self) -> str:
        return f"<{self}>"
    
    