def test_tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]  # Exemple de séquence de mouvements
    for move in moves:
        row, col = move
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

        print_board(board)
        if check_winner(board):
            print("Player " + player + " wins!")
            return

    print("No winner. It's a draw.")

test_tic_tac_toe()
