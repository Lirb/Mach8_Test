import NBA_Player

def main():
    db = NBA_Player.NBA_player_DB()
    data = db.getData() 
    print(data)
    
if __name__ == "__main__":
    main()
    