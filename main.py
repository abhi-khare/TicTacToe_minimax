from board import TicTacToe
from players import User, MiniMaxBot


repeat_game = 'Y'
user = User()
bot = MiniMaxBot()
board = TicTacToe()

# game loop
while repeat_game != 'N' or repeat_game != 'n':

    board.print_board()
    status = 'TBD'

    while status == 'TBD':

        if board.check_status() != 'TBD':
            break
        else:
            user_move = user.get_move()
            board.set_state(user_move, 'USER')
            board.print_board()

        if board.check_status() != 'TBD':
            break
        else:
            current_board_state = board.get_state()
            bot_move = bot.get_move(current_board_state)
            board.set_state(bot_move, 'BOT')
            board.print_board()

    status = board.check_status()
    if status == 'USER':
        user.set_tab()
    elif status == 'BOT':
        bot.set_tab()

    repeat_game = input('Do you want to play again?[Yes|NO]')

    if repeat_game.lower() == 'no':
        print(f'USER win count: {user.get_tab()} and Bot win count: {bot.get_tab()}')
        del user
        del bot
        del board
        break
    else:
        board.reset_state()
