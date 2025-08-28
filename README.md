# Bulls & Cows CLI Game

This is a command-line game where players guess a secret 4-digit number. The game tracks player stats and saves all game results to a database.

## What it does

- Lets you create and select player profiles
- Generates a random 4-digit number for you to guess
- Gives hints with "Bulls" (correct digit in correct position) and "Cows" (correct digit in wrong position)
- Saves all game results to a SQLite database using SQLAlchemy ORM
- Shows your personal statistics and win rate
- Tracks your game history

## How to use it

1. Make sure you have Python and Pipenv installed on your computer
2. Download all the project files
3. Open your terminal or command prompt
4. Navigate to the project folder
5. Install dependencies: `pipenv install`
6. Set up the database: `pipenv run alembic upgrade head`
7. Run the game: `pipenv run python lib/cli.py`
8. Follow the menu options to create a player and start playing

## Game rules

- The computer generates a random 4-digit number with no repeating digits
- You have 10 guesses to figure out the number
- After each guess, you get:
  - Bulls: How many digits are correct and in the right position
  - Cows: How many digits are correct but in the wrong position
- Try to guess the number in as few tries as possible!

## What you need

- Python 3.x installed
- Pipenv for dependency management
- No internet connection required (everything runs locally)

## Files included

- `lib/cli.py` - The main game program
- `lib/models.py` - SQLAlchemy database models
- `lib/helpers.py` - Game functions
- `alembic/` - Database migration files

## Note

The game uses SQLAlchemy ORM with Alembic migrations to create and manage the database. All data is stored in a SQLite database file called `bulls_and_bulls.db`.

## How to run

```bash

pipenv install

# Set up database migrations
pipenv run alembic upgrade head

# Run the game
pipenv run python lib/cli.py
```
