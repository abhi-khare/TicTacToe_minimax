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
        x = int((pos - 1) / 3)
        y = (pos - 1) % 3

        if player == 'BOT':
            self.board[x][y] = 0
            self.printable_board[x][y] = '0'
        else:
            self.board[x][y] = 1
            self.printable_board[x][y] = '1'

    def get_state(self):
        return self.board

    def reset_state(self):
        self.board = [[-10, -10, -10],
                      [-10, -10, -10],
                      [-10, -10, -10]]

        self.printable_board = [["", "", ""],
                                ["", "", ""],
                                ["", "", ""]]


    def print_board(self):
        print(tabulate(self.printable_board, tablefmt="grid"))

    def check_status(self):

        score_sum = [(self.board[0][0] + self.board[0][1] + self.board[0][2]),  # horizontal sum
                     (self.board[1][0] + self.board[1][1] + self.board[1][2]),
                     (self.board[2][0] + self.board[2][1] + self.board[2][2]),
                     (self.board[0][0] + self.board[1][0] + self.board[2][0]),  # vertical sum
                     (self.board[0][1] + self.board[1][1] + self.board[2][1]),
                     (self.board[0][2] + self.board[1][2] + self.board[2][2]),
                     (self.board[0][0] + self.board[1][1] + self.board[2][2]),  # cross sum
                     (self.board[2][0] + self.board[1][1] + self.board[0][2])]

        if 0 in score_sum:
            return 'BOT'
        elif 3 in score_sum:
            return 'USER'
        if -10 in self.board[0] or -10 in self.board[1] or -10 in self.board[2]:
            return 'TBD'
        else:
            return 'TIE'
