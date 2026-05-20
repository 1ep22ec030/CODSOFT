# CODSOFT Artificial Intelligence Internship Tasks

This repository contains three completed beginner-friendly AI tasks:

1. Task 1: Chatbot with Rule-Based Responses
2. Task 2: Tic-Tac-Toe AI
3. Task 4: Recommendation System

All projects use only Python's standard library, so no package installation is required.

## How to Run

Install Python 3.10 or newer first. While installing, enable **Add Python to PATH**.

Open a terminal in this `CODSOFT` folder and run any task:

```bash
python task1_chatbot/chatbot.py
python task2_tictactoe_ai/tictactoe.py
python task4_recommendation_system/recommender.py
```

If `python` does not work on your system, try:

```bash
py task1_chatbot/chatbot.py
py task2_tictactoe_ai/tictactoe.py
py task4_recommendation_system/recommender.py
```

On Windows, you can also double-click `run_tasks.bat` and choose a task from the menu.

## Task 1: Chatbot with Rule-Based Responses

The chatbot uses simple pattern matching to identify user intent and respond with predefined answers. It handles greetings, help requests, AI questions, time/date queries, jokes, and exit commands.

Main implementation ideas:

- Convert user text to lowercase.
- Use regular expression pattern matching to detect simple intents.
- Return a predefined response for known intents.
- Return a fallback response for unknown questions.
- Exit when the user types `bye`, `exit`, or `quit`.

Demo flow:

- Ask `hello`
- Ask `what is artificial intelligence`
- Ask `tell me a joke`
- Ask `help`
- Type `bye` to exit

## Task 2: Tic-Tac-Toe AI

This game lets a human player play against an unbeatable AI. The AI uses the Minimax algorithm to choose the best move.

Main implementation ideas:

- Store the board as a list of 9 cells.
- Human player uses `X`; AI uses `O`.
- Validate all user moves before placing them on the board.
- Check all rows, columns, and diagonals for a winner.
- Use Minimax to score possible future game states.

Demo flow:

- Run the game.
- Pick positions from 1 to 9.
- Try an invalid position or already-filled position.
- Explain that the AI checks future game states and chooses the move with the best outcome.

## Task 4: Recommendation System

This project recommends movies using content-based filtering. It compares the user's selected genres with each movie's genres and ranks the best matches.

Main implementation ideas:

- Store movies with genre sets.
- Ask the user for preferred genres.
- Compare the user's preferences with each movie's genres.
- Score movies based on matching genres.
- Display the top recommendations.

Demo flow:

- View the sample movies.
- Enter genres such as `sci-fi, action`.
- Show the top recommendations and explain that movies with more matching genres score higher.

## Suggested Demo Script

1. Run the chatbot and show that it responds to `hello`, AI questions, jokes, and `bye`.
2. Run Tic-Tac-Toe and show the human choosing board positions while the AI replies with strong moves.
3. Run the recommendation system and enter `sci-fi, action` to show ranked movie recommendations.

## Submission Guidance

For the internship submission:

1. Create a GitHub repository named `CODSOFT`.
2. Upload this folder's contents.
3. Record a short demo video showing all three tasks running.
4. Post or submit the GitHub repository link when the task submission form is shared.
