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

        