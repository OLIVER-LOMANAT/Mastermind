# Bulls & Cows CLI Game

This is a command-line game where players guess a secret 4-digit number. The game tracks player stats and saves all game results to a database.

## What It Does

- Allows you to **create and select player profiles**.
- Generates a random **4-digit number with no repeating digits** for you to guess.
- Provides hints using "Bulls" (correct digit in the correct position) and "Cows" (correct digit in the wrong position).
- Saves all game results and guesses to a SQLite database using **SQLAlchemy ORM**.
- Shows your personal statistics, including your **win rate**.
- Tracks your game history.

## Prerequisites

- **Python 3.x** installed.
- **Pipenv** for dependency management.
- No internet connection required; everything runs locally.

## Installation

1.  **Clone the repository** to your local machine.
2.  Navigate to the project's root directory in your terminal.
3.  **Install dependencies**:
    ```bash
    pipenv install
    ```
4.  **Set up the database**:
    ```bash
    pipenv run alembic upgrade head
    ```

## Usage

1.  **Run the game** from the project's root directory
    ```bash
    pipenv run python lib/cli.py
    ```
2.  Follow the interactive menu to select your desired option.

    - **1. Create new player**: Enter a unique username to create a new profile.
    - **2. List all players**: See a list of all existing player profiles.
    - **3. Select player**: Choose an existing player by entering their username. This is required before you can play a game.
    - **4. Play game**: Start a new game with the currently selected player. You will be prompted to enter your 4-digit guesses.
    - **5. View my stats**: See your personal game history, including total games played, wins, and your win percentage.
    - **6. Exit**: Close the game.

3.  **To play a game**, you must first select or create a player. The game will prompt you to enter a 4-digit number for each guess. A response of "4 Bulls, 0 Cows" means you have won!

## Game Rules

- The secret number is a random 4-digit number with no repeating digits (e.g., `1234`, not `1123`).
- You have **10 guesses** to figure out the number.
- **Bulls** are correct digits in the correct position.
- **Cows** are correct digits but in the wrong position.
- The goal is to guess the number in as few tries as possible.

## Files Included

- `lib/cli.py`: The main game program and command-line interface.
- `lib/models.py`: Defines the SQLAlchemy database models (`Player`, `Game`, `Guess`).
- `lib/helpers.py`: Contains helper functions for game logic (e.g., generating the secret number, checking guesses).
- `alembic/`: Database migration files for managing the database schema.

## Author

- **Oliver Ekeno** - [https://github.com/OLIVER-LOMANAT/Mastermind](https://github.com/OLIVER-LOMANAT/Mastermind)

## Contribution Guidelines

If you would like to contribute, please follow these steps:

1.  **Fork** the repository.
2.  Create a new feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.
