# CODSOFT Task 2: Tic-Tac-Toe AI

This repository contains **Task 2** of the CODSOFT Artificial Intelligence Internship: an AI-powered Tic-Tac-Toe game where a human player competes against an unbeatable computer player.

## Project Overview

This is a console-based Tic-Tac-Toe game written in Python. The human player plays as `X`, and the AI plays as `O`.

The AI uses the **Minimax algorithm** to evaluate possible future moves and choose the best move. This makes the AI very strong and prevents the human player from easily winning.

## Features

- Human vs AI gameplay
- Human player uses `X`
- AI player uses `O`
- Board positions are numbered from 1 to 9
- Validates user input
- Rejects already occupied positions
- Detects win, loss, and draw conditions
- Uses Minimax algorithm for AI decision making

## Technologies Used

- Python
- Python standard library

## Concepts Used

- Artificial Intelligence in games
- Game theory
- Minimax algorithm
- Recursion
- Board evaluation
- Decision making

## Project Structure

```text
task2_tictactoe_ai/
|-- README.md
|-- tictactoe.py
```

## Requirements

- Python 3.10 or newer
- No external libraries required

## How to Run

Open PowerShell or Command Prompt inside this folder and run:

```bash
python tictactoe.py
```

If you are running from the main `codsoft` folder, use:

```bash
python task2_tictactoe_ai/tictactoe.py
```

On Windows PowerShell, this also works:

```powershell
python task2_tictactoe_ai\tictactoe.py
```

## Board Positions

The game board uses numbers from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

The player enters a number to place `X` in that position.

## Sample Output

```text
Tic-Tac-Toe AI
You are X. The AI is O.

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Choose a position from 1 to 9: 1
AI chooses position 5.
```

## How Minimax Works

The Minimax algorithm checks possible future game states and assigns scores:

| Result | Score |
| --- | --- |
| AI wins | `1` |
| Human wins | `-1` |
| Draw | `0` |

The AI tries to maximize the score, while the human player's possible moves are treated as minimizing the score. By checking all possible future moves, the AI chooses the best available move.

## Main Functions

| Function | Purpose |
| --- | --- |
| `print_board()` | Displays the current board |
| `winner()` | Checks if there is a winner or draw |
| `minimax()` | Scores future game states |
| `best_ai_move()` | Selects the best move for the AI |
| `get_human_move()` | Gets and validates user input |
| `main()` | Runs the game loop |

## Test Cases

| Test | Expected Result |
| --- | --- |
| Enter a valid empty position | Player move is placed |
| Enter a number outside 1 to 9 | Error message is shown |
| Enter a non-number value | Error message is shown |
| Enter an occupied position | Error message is shown |
| Complete a game | Win or draw message is shown |
| Play against AI | AI chooses strong moves using Minimax |

## Internship Task Requirement

**Task:** Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. Use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable.

This implementation satisfies the requirement by using the Minimax algorithm to choose optimal AI moves.

## Author

Created by **Deiva** for the CODSOFT Artificial Intelligence Internship.
