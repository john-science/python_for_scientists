# Dealing with CSV Files

One day seven people sat down and played five games of power.

For the following problem, copy the following text into a file named `poker_winnings.csv`:

    Player,Game1,Game2,Game3,Game4,Game5
    Tycho Brahe,1324,2600,-3318,1210,-4146
    Albert Einstein,918,2784,-1928,658,-298
    Richard Feynman,-202,-1310,240,898,430
    Johannes Kepler,-268,-382,-86,210,-1696
    Issac Newton,128,1024,2048,-512,-1024
    Emmy Noether,554,586,620,640,528
    Erwin Schrödinger,-2454,-5302,2424,-3104,6206


## Problems

Write a function that:

1. `read_poker_csv` that takes a file path and returns a dictionary named `winnings` where the keys are the names of the poker players (column 0), and each key is paired with a list of five integer values, according to how much each person one in each game.
2. `find_players` that takes in a dictionary like `winnings` above and returns the names of all the poker players in a list.
3. `find_total` that takes in a list of integers and returns the sum.
4. `find_average` that takes in a list of integers and returns the average.
5. `find_totals` that takes in a dictionary like `winnings` above and uses `find_total` to return a dictionary where the keys are the names of the power players and the values are the total amount each player won/lost after all five games.
6. `find_averages` that takes in a dictionary like `winnings` above and uses `find_average` to return a dictionary where the keys are the names of the power players and the values are the average amount each player won/lost during all five games.
7. `game_totals` that takes in a dictionary like `winnings` above and produces a list of five integers, that represent the sum total of all winnings/losses added together for each game. (Obviously, we expect the winnings for each game to add to zero.)
8. `write_new_winnings` that takes in a dictionry like `winnings` above and a string for the filepath of the new output file. This function will then call `find_averages` and `find_totals` to get the averages and totals. Then it will write a new CSV file that looks much like the original one, but with two new columns: one for each player's average winnings, and one for each player's total winnings.

## Solutions

* [CSV - Solutions](problem_set_2_solutions.md)


[Back to Lecture](lecture_04.md)
