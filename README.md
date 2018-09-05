# TicTacToe_minimax

**Introduction** 

A TicTacToe is a finite state game in which two players plays the game sequentially to make a horizontal , vertical or diagonal sequence of 'O' or 'X'. Due to finite nature of TIC-TAC-TOE, it is technically possible to enumerate all the possible moves and therefore design an unbeatable AI bot. The only issue is that we may need to store all the state space information. This is fine for small game like tic-tac-toe, but may throw some issues for games like chess. We can use Min-Max algorithm that will reduce the space complexity and allow us to search through the state space for optimal moves in exchange of small searching cost. 

**Dependencies**

- numpy 1.13.3 <br />
- pygame 1.9.3 <br />

**Install instructions**

- install the dependencies using the command: pip install requirements.
- to run the game, type python main.py.

**Usage**

Input: 1-9 corresponding to cell number from top to bottom and left-right.
first input is by user and shown by O and AI moves are shown by X.


