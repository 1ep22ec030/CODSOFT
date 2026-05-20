HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for row in range(3):
        cells = []
        for col in range(3):
            index = row * 3 + col
            cells.append(board[index] if board[index] != EMPTY else str(index + 1))
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]

    if EMPTY not in board:
        return "Draw"

    return None


def minimax(board, is_ai_turn):
    result = winner(board)
    if result == AI:
        return 1
    if result == HUMAN:
        return -1
    if result == "Draw":
        return 0

    if is_ai_turn:
        best_score = -10
        for index, value in enumerate(board):
            if value == EMPTY:
                board[index] = AI
                best_score = max(best_score, minimax(board, False))
                board[index] = EMPTY
        return best_score

    best_score = 10
    for index, value in enumerate(board):
        if value == EMPTY:
            board[index] = HUMAN
            best_score = min(best_score, minimax(board, True))
            board[index] = EMPTY
    return best_score


def best_ai_move(board):
    best_score = -10
    move = None

    for index, value in enumerate(board):
        if value == EMPTY:
            board[index] = AI
            score = minimax(board, False)
            board[index] = EMPTY

            if score > best_score:
                best_score = score
                move = index

    return move


def get_human_move(board):
    while True:
        try:
            choice = input("Choose a position from 1 to 9: ").strip()
        except EOFError:
            return None

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        index = int(choice) - 1
        if index < 0 or index > 8:
            print("Please choose a number between 1 and 9.")
            continue

        if board[index] != EMPTY:
            print("That position is already taken.")
            continue

        return index


def main():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe AI")
    print("You are X. The AI is O.")

    while winner(board) is None:
        print_board(board)
        human_move = get_human_move(board)
        if human_move is None:
            print("Game ended because no more input was provided.")
            return
        board[human_move] = HUMAN

        if winner(board) is not None:
            break

        ai_move = best_ai_move(board)
        board[ai_move] = AI
        print(f"AI chooses position {ai_move + 1}.")

    print_board(board)
    result = winner(board)

    if result == "Draw":
        print("Game over: It is a draw.")
    elif result == HUMAN:
        print("Game over: You win!")
    else:
        print("Game over: AI wins!")


if __name__ == "__main__":
    main()
