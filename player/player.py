from json import JSONEncoder
class Player:
    
    def __init__(self, first_name:str, last_name:str, h_in:float, h_meters:float) -> None:
       self.__first_name = first_name
       self.__last_name = last_name
       self.__h_in = float(h_in)
       self.__h_meters = float(h_meters)
       
    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name}\t{self.__h_in}"
    
    def __repr__(self) -> str:
        return f"<first name: {self.__first_name} last name: {self.__last_name} height (inches):{self.__h_in}"
    
    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__
    
    def get_first_name(self) -> str:
        return self.__first_name
    def get_last_name(self) -> str:
        return self.__last_name
    def get_height_inches(self) -> float:
        return self.__h_in
           
    class NBA_player_encoder(JSONEncoder):
        
        def default(self, pythonObject:object) -> dict:
            return pythonObject.__dict__
            
    
        


