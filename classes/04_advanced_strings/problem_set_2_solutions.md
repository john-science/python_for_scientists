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

#### 1. `read_poker_csv` that takes a file path and returns a dictionary named `winnings` where the keys are the names of the poker players (column 0), and each key is paired with a list of five integer values, according to how much each person one in each game.

    def read_poker_csv(filepath):
        '''Read in a special CSV file for poker game results
        and return a player-oriented dicionary of their winnings.
        '''
        f = open(filepath, 'r')
        header = f.readline()
        lines = f.readlines()
        f.close()
        
        winnings = {}
        for ln in lines:
            line = ln.strip().split(',')
            winnings[line[0]] = []
            for money in line[1:]:
                winnings[line[0]].append(float(money))
        
        return winnings

#### 2. `find_players` that takes in a dictionary like `winnings` above and returns the names of all the poker players in a list.

    def find_players(winnings):
        '''pull all of the unique player names
        from a specialty poker dictionary.
        '''
        return winnings.keys()

#### 3. `find_total` that takes in a list of integers and returns the sum.

    def find_total(lst):
        '''Find the sum of all the items in a list of integers'''
        sum = 0
        for item in lst:
            sum += item
        
        return sum

Or, if you want to cheat, use the built-in Python function:

    def find_total(lst):
        '''Find the sum of all the items in a list of integers'''
        return sum(lst)

#### 4. `find_average` that takes in a list of integers and returns the average.

    def find_average(lst):
        '''Find the average of all the items in a list of integers'''
        return find_total(lst) / float(len(lst))

**HINT***: I had to put float around either the numerator or the denominator so that the answer could be a float. If I forgot to do this, the answer would always be an integer and thus a little bit wrong.

#### 5. `find_totals` that takes in a dictionary like `winnings` above and uses `find_total` to return a dictionary where the keys are the names of the power players and the values are the total amount each player won/lost after all five games.

    def find_totals(winnings):
        '''create a dictionary of the total winnings of each player'''
        totals = {}
        for player in winnings:
            totals[player] = find_total(winnings[player])
        
        return totals

#### 6. `find_averages` that takes in a dictionary like `winnings` above and uses `find_average` to return a dictionary where the keys are the names of the power players and the values are the average amount each player won/lost during all five games.

    def find_avearges(winnings):
        '''create a dictionary of the averages winnings,
        per game, of each player'''
        averages = {}
        for player in winnings:
            averages[player] = find_average(winnings[player])
        
        return averages

#### 7. `game_totals` that takes in a dictionary like `winnings` above and produces a list of five integers, that represent the sum total of all winnings/losses added together for each game. (Obviously, we expect the winnings for each game to add to zero.)

    def game_totals(winnings):
        '''sum each players winnings or loses for all five games
        to ensure that each game no money was created or destroyed.'''
        totals = [0, 0, 0, 0, 0]
        for game in range(5):
            for player in winnings:
                totals[game] += winnings[player][game]
        
        return totals

#### 8. `write_new_winnings` that takes in a dictionry like `winnings` above and a string for the filepath of the new output file. This function will then call `find_averages` and `find_totals` to get the averages and totals. Then it will write a new CSV file that looks much like the original one, but with two new columns: one for each player's average winnings, and one for each player's total winnings.

    def write_new_winnings(winnings, filepath):
        '''Write a new CSV file with two extra stats columns about
        each player: average winnings per game, and total winnings.'''
        # The file needs a header
        header = 'Player,Game1,Game2,Game3,Game4,Game5,Average,Total\n'
        # Do the stats on each player
        averages = find_averages(winnings)
        totals = find_totals(winnings)

        # Open the file and write a line for each player
        f = open(filepath, 'w')
        f.write(header)
        for player in winnings:
            # I decided it would be easier to build each line as a
            # list and then join them later.
            line = [player]
            for game in range(5):
                line.append(str(winnings[player][game]))
            line.append(str(averages[player]))
            line.append(str(totals[player]))
            f.write(','.join(line) + '\n')

        # don't forget to clsoe the file
        f.close()


[Back to Problem Set](problem_set_2_csv.md)
