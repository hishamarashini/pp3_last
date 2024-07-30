### X||O GAME

The X,O game is a Python terminal game which runs in mock terminal on Heroku. Played on a three-by-three grid by player with a computer who alternately place the marks X and O in one of the nine spaces in the grid.

![img](images/responsiv22.png)

#### How to play
The player start with choosing number from the grid marking the spaces in a three-by-three grid with X and the computer will mark the O in random. 
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

#### Features
* Existing Feature
    * Game start with the grid and explain to the player to choose number or "q" to quit.

![img](images/start.JPG)


    * The player will start with letter "X", and the computer will choose "O".

![img](images/error.JPG)

* Input valid and error checking
    * You cannot enter any letter or numbers greater than number 9.

![img](images/you_won.JPG)

    * Result for winner, or loser and if it's tie.

#### Data Model
The game start with grid of numbers from 1 to 9, adding text explaining to the player to choose number and will change to "X", and the computer will choose the "O" randomly, the player can choose "q" to quit the game, or "r" to restart again.

#### Testing
* I manually tested this project at PEP8 and confirmed that no problems.
* Played the game using undefined numbers or letter to insure the code will give invailed entry
* Tested the code in Heroku terminal
#### Bugs
#### Validating
* PEP8
    * No errors

![img](images/pep8_test.JPG)   

#### Deployment
* This project was deployed using deployment method at Heroku and connected with Github, 
    * Creating a new Heroku app
    * Set the buildbacks to Python and Node Js in the order  as I get fron the template that i got from Love Sandwiches project.
    * Link the Heroku app to repositry
    * Click on manual Deploy.


#### Credits
* Wikipidia details of the game.
