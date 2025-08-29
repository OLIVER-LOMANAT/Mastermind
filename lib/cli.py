import click
from helpers import *
from models import session

@click.group()
def cli():
    """Bulls & Cows Game"""
    pass

@cli.command()
def menu():
    """Start the game menu"""
    current_player = None

    while True:
        click.echo("\n--- Bulls & Cows Game ---")
        click.echo("1. Create new player")
        click.echo("2. List all players")
        click.echo("3. Select player")
        if current_player:
            click.echo(f"4. Play game ({current_player.username})")
            click.echo("5. View my stats")
        click.echo("6. Exit")

        choice = click.prompt("Choose option", type=str)

        if choice == "1":
            username = click.prompt("Enter username")
            if find_player_by_username(username):
                click.echo("Username taken!")
            else:
                current_player = create_player(username)
                click.echo(f"Player {username} created!")

        elif choice == "2":
            players = get_all_players()
            if players:
                for player in players:
                    click.echo(f"- {player.username}")
            else:
                click.echo("No players found")

        elif choice == "3":
            username = click.prompt("Enter username")
            player = find_player_by_username(username)
            if player:
                current_player = player
                click.echo(f"Hello {current_player.username}!")
            else:
                click.echo("Player not found")

        elif choice == "4" and current_player:
            click.echo("\nNew game started!")
            secret_number = generate_secret_number()
            guesses_count = 0
            won = False

            game = Game(
                player_id=current_player.id,
                secret_number=secret_number,
                status="in_progress"
            )
            session.add(game)
            session.commit()

            while guesses_count < 10 and not won:
                guess_input = click.prompt(f"Guess{guesses_count + 1}", type=str)

                if len(guess_input) != 4 or not guess_input.isdigit():
                    click.echo("Enter 4-digit number")
                    continue

                guesses_count += 1
                bulls, cows = check_guess(secret_number, guess_input)
                click.echo(f"{bulls} Bulls, {cows} Cows")

                save_guess(game, guess_input, bulls, cows)

                if bulls == 4:
                    won = True
                    game.status = "won"
                    game.guesses_taken = guesses_count
                    click.echo(f"You won in {guesses_count}guesses")

            if not won:
                game.status = "lost"
                game.guesses_taken = guesses_count
                click.echo(f"Game over! Number was {secret_number}")

            session.commit()
            click.echo("Game saved!")

        elif choice == "5" and current_player:
            games = get_player_games(current_player.id)
            if games:
                wins = sum(1 for game in games if game.status == 'won')
                total = len(games)
                click.echo(f"\n{current_player.username}Stats")
                click.echo(f"Games: {total}")
                click.echo(f"Wins: {wins}")
                if total > 0:
                    click.echo(f"Win: {wins / total * 100:.1f}")
                else:
                    click.echo("Win:0")
            else:
                click.echo("No games played")

        elif choice == "6":
            click.echo("Goodbye!")
            session.close()
            break

        else:
            click.echo("Wrong choice")

if __name__ == "__main__":
    cli()

