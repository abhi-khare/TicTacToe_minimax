class User:

    def __init__(self):
        self.win_tab: int = 0

    @staticmethod
    def get_move():
        pos = input()
        return int(pos)

    def set_tab(self):
        self.win_tab += 1

    def get_tab(self):
        return self.win_tab


class MiniMaxBot:

    def __init__(self):
        self.win_tab: int = 0

    def get_bot_move(self, game_state, level: int):

        # check the status of the game. It's an anchor condition if there are
        # no more valid moves left on board. Otherwise, we proceed with computing
        # score for each game_state.
        status = self.check_status(game_state)

        if status == 'BOT':
            # game state gets a score of 10 in which bot wins
            return [10, -1, -1]
        elif status == 'USER':
            # game state gets a score of -10 in which user win
            return [-10, -1, -1]
        elif status == 'TIE':
            # 0 score is assigned to state in which there is a tie.
            return [0, -1, -1]
        else:
            score_list = []
            # iterating through each cell of board, recursively computing the
            # score of each board and storing it in the list
            for i in range(0, 3):
                for j in range(0, 3):
                    if game_state[i][j] == -10:
                        game_state[i][j] = level  # 0 = BOT and 1 = USER
                        score = self.get_bot_move(game_state, 1 - level)
                        score_list.append([score[0], i, j])
                        game_state[i][j] = -10  # resetting the game state

            min_score, max_score, pos_x, pos_y = 100, -100, -1, -1
            for move in score_list:
                if level == 1 and move[0] < min_score:
                    min_score = move[0]
                    pos_x, pos_y = move[1], move[2]
                elif level == 0 and move[0] > max_score:
                    max_score = move[0]
                    pos_x, pos_y = move[1], move[2]

            if level == 1:
                return min_score, pos_x, pos_y
            else:
                return max_score, pos_x, pos_y

    @staticmethod
    def check_status(game_state):

        score_sum = [(game_state[0][0] + game_state[0][1] + game_state[0][2]),  # horizontal sum
                     (game_state[1][0] + game_state[1][1] + game_state[1][2]),
                     (game_state[2][0] + game_state[2][1] + game_state[2][2]),
                     (game_state[0][0] + game_state[1][0] + game_state[2][0]),  # vertical sum
                     (game_state[0][1] + game_state[1][1] + game_state[2][1]),
                     (game_state[0][2] + game_state[1][2] + game_state[2][2]),
                     (game_state[0][0] + game_state[1][1] + game_state[2][2]),  # cross sum
                     (game_state[2][0] + game_state[1][1] + game_state[0][2])]

        if 0 in score_sum:
            return 'BOT'
        elif 3 in score_sum:
            return 'USER'
        if -10 in game_state[0] or -10 in game_state[1] or -10 in game_state[2]:
            return 'TBD'
        else:
            return 'TIE'

    def get_move(self, game_state) -> int:

        score, x, y = self.get_bot_move(game_state, 0)

        # converting x,y coordinates into [1-9] range
        pos = 3 * x + y + 1
        return pos

    def set_tab(self) -> None:
        self.win_tab += 1

    def get_tab(self) -> int:
        return self.win_tab
