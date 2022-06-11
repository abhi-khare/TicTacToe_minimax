from tabulate import tabulate


class TicTacToe:

    def __init__(self):
        # initialising Tic-Tac-Toe board
        self.board = [[-10, -10, -10],
                      [-10, -10, -10],
                      [-10, -10, -10]]

        self.printable_board = [["", "", ""],
                                ["", "", ""],
                                ["", "", ""]]

    def set_state(self, pos: int, player: str):
        # resolving pos into x,y coordinates
        x = pos % 3
        y = int(pos / 3)

        if player == 'AI':
            self.board[x][y] = 0
            self.printable_board[x][y] = '0'
        else:
            self.board[x][y] = 1
            self.printable_board[x][y] = '1'

    def return_state(self):
        return self.board

    def print_board(self):
        print(tabulate(self.printable_board, tablefmt="grid"))

    def check_status(self):

        score_sum = [sum(self.board[0]),  # horizontal sum
                     sum(self.board[1]),
                     sum(self.board[2]),
                     (self.board[0][0] + self.board[0][1] + self.board[0][2]),  # vertical sum
                     (self.board[1][0] + self.board[1][1] + self.board[1][2]),
                     (self.board[2][0] + self.board[2][1] + self.board[2][2]),
                     (self.board[0][0] + self.board[1][1] + self.board[2][2]),  # cross sum
                     (self.board[2][0] + self.board[1][1] + self.board[0][2])]

        if 0 in score_sum:
            return 'AI'
        elif 1 in score_sum:
            return 'USER'
        else:
            return 'TIE'
