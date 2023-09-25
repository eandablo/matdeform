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

On running the application, a menu is provided to select a number to either be directed to instructions or starting the game.

![welcome](assets/images/welcome.png)

If in the menu selection, no number is provided or the number is not either 1 or 2, an error is displayed giving another chance to provide an appropriate entry.

![welcome-error](assets/images/welcome-error.png)

Selecting 1, the first part of the instructions are displayed.

![instructions](assets/images/instructions.png)

After finishing the first read, you must press enter to find an example. The example provides an image of how a win by linking all floors looks.

![example](assets/images/example.png)

After pressing enter again you will be redirected to the game.

![game-start](assets/images/game-1.png)

## Data model

Each floor in the program is created as an instance of a class Floor. 
The Floor class is designed to alot 

## Testing


## Bugs


## Deployment

The project was deployed in the Code Institute's mock terminal for Heroku followin the steps bellow:

1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildpacks to Python and NodeJS in that order
4. Link the Heroku app to the repository
5. Click on Deploy

## Credits

- Code Institute for providing the mock template user for this project deployement
