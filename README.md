### X||O GAME

The X,O game is a Python terminal game which runs in mock terminal on Heroku. 
The game is played on a three-by-three grid by player with computer who alternately place the marks X and O in one of the nine numbers in the grid, and the one who will get three vertical or horizantal or diagonal will win the game.

[Link to live version of my project](https://pp3-last-f8d180165b83.herokuapp.com/)

![img](images/responsiv22.png)

#### How to play
The player start with choosing number from the grid marking the spaces in a three-by-three grid with "X" and the computer will mark the "O" in random. 
The one who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

#### Features
* Existing Feature
    * Game start with the grid and explain to the player to choose number or "q" to quit.

![img](images/start.JPG)


    * The player will start with letter "X", and the computer will choose "O".

![img](images/error.JPG)

* Input valid and error checking
    * If the player place or enter any wrong letter or numbers greater than number 9, terminal will give invalid entry and giving the player to start again.

![img](images/you_won.JPG)

    * Result for winner, or loser and if it's tie.

#### Data Model
The game start with grid of numbers from 1 to 9, adding text explaining to the player to choose number and will change to "X", and the computer will choose the "O" randomly, the player can choose "q" to quit the game, or "r" to restart again.

#### Testing
* I manually tested this project at PEP8 and confirmed that is no problems.
* Played the game using undefined numbers or letter to insure the code will give invailed entry
* Tested the code in Heroku terminal

#### Validating
* PEP8
    * No errors

![img](images/pep8_test.JPG)   

#### Deployment
* Starting with the template form Code Institute project on github, changing the python code at run.py
* Creating Heroku student account 
* Creating a new Heroku app
* Connect the github with Heroku app
* Set the buildbacks to Python and Node Js in Heroku settings in order as I get from the template that i got from project.
* Link the Heroku app to the repositry
* Click on manual Deploy.
* Test the code in Heroku terminal after deployment. 


#### Credits
* Wikipidia details of the game.
