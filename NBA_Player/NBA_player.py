class NBA_player:
    
    def __init__(self, first_name: str, last_name: str, h_in:float,h_meters:float ) -> None:
       self.__first_name = first_name
       self.__last_name = last_name
       self.__h_in = h_in
       self.__h_meters = h_meters
       
    def __str__(self) -> str:
        return f"{self.__first_name} {self.__last_name} {self.__h_in}"
    
    def __repr__(self) -> str:
        return f"<first name: {self.__first_name} last name: {self.__last_name} height (inches):{self.__h_in}"
    
    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict___
    
    def getFirstName(self) -> str:
        return self.__first_name
    def getLastName(self) -> str:
        return self.__last_name
    def getHeightInches(self) -> str:
        return self.__h_in
    def getHeightMeters(self) ->str:
        return self.__h_meters
    
    def setFirstName(self, first_name:str) -> None:
        self.__first_name = first_name
    def getLastName(self, last_name:str) -> None:
        self.__last_name = last_name
    def getHeightInches(self,h_in:str) -> None:
        self.__h_in = h_in
    def getHeightMeters(self,h_meters:str) -> None:
        self.__h_meters = h_meters