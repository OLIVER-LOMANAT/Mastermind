from helpers import * 
from models import session
from helpers import save_guess 

def main_menu():
    current_player = None

    while True:
        print("\n ---Bulls & Cows Game ----")
        print("1. Create new player")
        print("2. List all players")
        print("3. Select player")
        if current_player:
            print(f"4. Play game ({current_player.username})")
            print("5. View my stats")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            if find_player_by_username(username):
                print("Username taken!")
            else:
                current_player = create_player(username)
                print(f"Player {username} created")
        
        elif choice == "2":
            players = get_all_players()
            if players:
                for player in players:
                    print(f"{player.username}")
            else:
                print("No players found")

        elif choice == 3:
            username = input("Enter username: ")
            player = find_player_by_username(username)
            if player:
                create_player = player
                print(f"Hello {current_player.username}")
            else:
                print("Player not found")

        elif choice == 4 and current_player:
            secret_number = generate_secret_number()
            guesses_count = 0
            won = False

            game = Game(
                player_id = current_player.id,
                secret_number = secret_number,
                status = "in_progress"
            )
            session.add(game)
            session.commit()

