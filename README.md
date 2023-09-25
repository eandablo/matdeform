# 3D Tic Tac

3D Tic Tac is a 3D version of the loved tic tac toe game. The game runs in the code institute deployment terminal.
The user will play a game vs the computer, which has been equipped with sufficient intelligence to provide the user with a stimulating challenge.

[You can visit the deployed proyect here](https://new-tick-tac-toe-9fb1e1ca8d45.herokuapp.com/)

## How to play

In this game, the user will battle the machine in three floors simultaneously. Each floor consisting of the original 3 x 3 grid tic tac toe.

The game will start by showing the three floors. The machine will start the game selecting a position in any of the three floors. The user, then will be asked to select a move by giving three numbers, first for the floor, second and third for the row and column in the floor. The computer selection will be marked by 'X', whereas the user position will be marked as 'O'. After a new computer selection, the updated floors will be displayed again. This exchange will continue , until a player wins or a tie is declared. To win, one of two conditions are met by either player:

1. One of the players wins two out of three floors. Winning a floor, requires either player to connect one column, one row or a diagonal. 

2. One of the players connects all three floors by filling the three positions of any vertical line.

On the other hand, a tie will be declared if at a point of the game, there is no possibility for any of the player to fullfil the first option above.

## Features

A menu gives the user the opportunity to choose between instructions or start playing the game.

![welcome](assets/images/welcome.png)

The selection is done by choosing a number, 1 for instructions or 2 for play. If in the menu selection, no number is provided or the number is not either 1 or 2, an error is displayed giving another chance to provide an appropriate entry.

![welcome-error](assets/images/welcome-error.png)

Instruction how to play the game are complemented with an example to unsdertand how to win and select a move. 

![instructions](assets/images/instructions.png)


![example](assets/images/example.png)

Selecting 2, the game will start with the computer move as shown bellow.

![game-start](assets/images/game-1.png)

The user moves are taken with 3 entries, each consisting of a number between 1 and 3. Entry errors are handled with the same function used for the menu.

![entry-error](assets/images/entry-error.png)

Moves made by the computer are of two kind.

1. Deterministic moves: The algorithm searches for moves to block winning posibilities created by the user, scoring by culminating potential opportunities creating by the computer or generating "attacks" by creating potential opportunities to win by connecting the floors (second option). 

2. Stochastic moves: If deterministic moves are not neccesary at the moment, the algorithm decides for a stochastic option by creating moves using a Bayes-like approach with random likelihood matrices for both, user and computer previous positions. This algorithm is a simple approach to allow the computer learning from the user choices and create a medium level of difficulty, providing an entertaining and challenging experience for the user.


## Data model

Each floor in the program is created as an instance of a class Floor. 
The Floor class is designed to lodge the moves in an 2D array. It contains three functions: (i) assign_values updates the floor with either computer or user moves, count_empties counts the available spaces in the floors arrays and print_floor displays in console the current state of the floor.


## Testing

### Menu entry handling

The initial menu is capable to handle exceptions to ensure an appropriate number is entered to choose either instructions of start playing the game as shown below.

### User move entry handling

The error handling of menu was thoroughly tested and showed capable of reject invalid entries.

![menu-entry-handling](assets/images/test-menu-entries.png)

The same testing was performed for the three neccessary entries for the user move. As seen in the figures below for floor, row and column, respectively, the interface rejects any invalid entry.

![floor-entry-handling](assets/images/floor-error-handling.png)

![row-entry-handling](assets/images/row-error-handling.png)

![row-entry-handling](assets/images/column-error-handling.png)

The algorithm must also prevent the user from selecting a space already busy as shown in the image below.

![handling-busy](assets/images/busy-position.png)

### Computer intelligence

On testing, the computer proved being capable to block user opportunities and create winning opportunities. In the image below the computer had blocked the user winning option in the third floor and subsequently created an opportunity to win by connecting vertically all floors. This represents a challenge to the user, since it requires attention to spot this attempts.

![computer-block](assets/images/computer-schemming.png)

In this case, the computer managed to create the vertical option, but also an opportunity to win the second floor by forcing the user to block the vertical "attack", leaving the computer to connect the third row in the second floor.

Further testing proved the computer capacity to win by either:
- option 1 (winning two floors) 

![computer-two-floor-win](assets/images/computer-two-floor-win.png)

or 

- option two (connecting floors vertically)

![computer-vertica-win](assets/images/computer-vertical-win.png)

The computer gracefully will advice the user they you have lost.

![losing-message](assets/images/losing-notice.png)

## Bugs

No bugs were found.

## Deployment

The project was deployed in the Code Institute's mock terminal for Heroku followin the steps bellow:

1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildpacks to Python and NodeJS in that order
4. Link the Heroku app to the repository
5. Click on Deploy

## Credits

- Code Institute for providing the mock template user for this project deployement
