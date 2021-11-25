    """Wrap the objects Player, PlayerDB and PlayerDuo and all functialities need to users interact with each object.
    
    Player class describe and NBA player, using his full name and height.
    PlayerDuo class describe a set of two differents NBA players(Player objects).
    PlayerDB class retrieve NBA player data from the defined endpoint and create a python 
    collection of NBA players(Player object).   
    """


from .player import Player
from .player_duo import PlayerDuo
from .player_db import PlayerDB
