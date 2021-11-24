import NBA_Player

def main():
    db = NBA_Player.NBA_player_DB()
    db.setPosition(500)
    for nba_player in db:
        print(nba_player.getFirstName())
    
if __name__ == "__main__":
    main()
    