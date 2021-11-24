from json import JSONEncoder
class NBA_player:
    
    def __init__(self, first_name:str, last_name:str, h_in:float, h_meters:float) -> None:
       self.__first_name = first_name
       self.__last_name = last_name
       self.__h_in = float(h_in)
       self.__h_meters = float(h_meters)
       
    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name} {self.__h_in}"
    
    def __repr__(self) -> str:
        return f"<first name: {self.__first_name} last name: {self.__last_name} height (inches):{self.__h_in}"
    
    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__
    
    def getFirstName(self) -> str:
        return self.__first_name
    def getLastName(self) -> str:
        return self.__last_name
    def getHeightInches(self) -> float:
        return self.__h_in
    def getHeightMeters(self) -> float:
        return self.__h_meters
    
    def setFirstName(self, first_name:str) -> None:
        self.__first_name = first_name
    def setLastName(self, last_name:str) -> None:
        self.__last_name = last_name
    def setHeightInches(self,h_in:float) -> None:
        self.__h_in = h_in
    def setHeightMeters(self,h_meters:float) -> None:
        self.__h_meters = h_meters
        
    class NBA_player_encoder(JSONEncoder):
        def default(self, pythonObject:object) -> dict:
            return pythonObject.__dict__
            
    
        


