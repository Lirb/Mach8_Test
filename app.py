import NBA_Player

def main():
    db = NBA_Player.NBA_player_DB()
    filtered_data = db.filter(85)
    print(filtered_data)
    
if __name__ == "__main__":
    main()
    