# Snake Water Gun Game

This is a simple Flask-based implementation of the classic **Snake-Water-Gun** game. Users can play against the computer by selecting their choice (Snake, Water, or Gun) via an API endpoint. The server generates a random computer choice, evaluates the result, and returns whether the user won, lost, or tied.

## Game Rules:
- **Snake beats Water**.
- **Water beats Gun**.
- **Gun beats Snake**.
- If both choices are the same, it's a **tie**.

## Features:
- **Flask API** for game logic.
- Randomized computer moves.
- Clear JSON response with user choice, computer choice, and the game result.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/snake-water-gun-game.git
   ```

2. Navigate into the project folder:

   ```bash
   cd snake-water-gun-game
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. The game will be hosted on `http://127.0.0.1:5000/`.

## API Endpoints:

- **GET /**: Returns the index HTML page for the game.
- **POST /play**: Sends the user choice in JSON format and receives the result.

