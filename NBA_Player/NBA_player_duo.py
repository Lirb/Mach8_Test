from .NBA_player import NBA_player
class NBA_player_duo:
    def __init__(self, NBA_player_1: NBA_player, NBA_player_2: NBA_player) -> None:
        self.__NBA_player_1 = NBA_player_1
        self.__NBA_player_2 = NBA_player_2
        self.__height_sum =  self.__NBA_player_1.getHeightInches() + self.__NBA_player_2.getHeightInches()
    def __str__(self) -> str:
        return f"- {self.__NBA_player_1}\t{self.__NBA_player_2}\n "
    def __repr__(self) -> str:
        return f"<{self}>"
    
    def getNBAPlayer1(self) -> NBA_player:
        return self.__NBA_player_1
    def getNBAPlayer2(self) -> NBA_player:
        return self.__NBA_player_2
    def getHeightSum(self) -> float:
        return self.__height_sum
    
    def setNBAPlayer1(self, NBA_player_1:NBA_player) -> None:
        self.__NBA_player_1 = NBA_player_1
    def setNBAPlayer2(self, NBA_player_2:NBA_player) -> None:
        self.__NBA_player_2 = NBA_player_2
    