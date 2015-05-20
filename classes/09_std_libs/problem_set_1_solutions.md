# Standard Libraries, Part 1 - Solutions


## datetime

#### 1. `pprint_date` that takes in a `datetime` object and returns a string formatted like: `Saturday, March 14, 2015 at 9:26AM`.

    def pprint_date(d):
        '''Return a pretty-printed form of a given date'''
        return d.strftime('%A, %B %d, %Y at %H:%m%p')

#### 2. `days_diff` that takes two `datetime` objects and returns the number of days between them. Use this function to determine how many days you've been alive.

    def days_diff(date1, date2):
        '''calculate the difference between to days,
        in days.'''
        diff = date2 - date1
        return diff.days
    
    >>> # ages of various actors on Christmas, 2015:
    >>> from datetime import datetime
    >>> now = datetime.now()
    >>> now
    datetime.datetime(2015, 12, 31, 8, 0)
    >>> chris_pratt = datetime(1979, 6, 21)
    >>> days_diff(chris_pratt, now)
    13342
    >>> sarah_michelle_gellar = datetime(1977, 4, 14)
    >>> days_diff(sarah_michelle_gellar, now)
    14140
    >>> will_wheaton = datetime(1972, 7, 29)
    >>> days_diff(will_wheaton, now)
    15860
    >>> nathan_fillion = datetime(1971, 3, 27)
    >>> days_diff(nathan_fillion, now)
    16350

#### 3. `apollo_dates` that takes two `datetime` objects and prints each date formatted nicely, including the day-of-week. Use this function to print out the dates of the Apollo 11 moon-landing mission, which left the Earth on July 16th, 1969 and landed safely again on July 24th, 1969.

    from datetime import datetime, timedelta
    
    def apollo_dates(date1, date2):
        '''print out nicely-formatted dates between two
        given start and end dates'''
        current = date1
        while current <= date2:
            print(current.strftime('%A, %B %d, %Y'))
            current += timedelta(days=1)
    
    >>> takeoff = datetime(1969, 7, 16)
    >>> landing = datetime(1969, 7, 24)
    >>> apollo_dates(takeoff, landing)
    Wednesday, July 16, 1969
    Thursday, July 17, 1969
    Friday, July 18, 1969
    Saturday, July 19, 1969
    Sunday, July 20, 1969
    Monday, July 21, 1969
    Tuesday, July 22, 1969
    Wednesday, July 23, 1969
    Thursday, July 24, 1969

#### 4. `dow_dict` that takes a start date and an end date (as `datetime` objects) and returns a dictionary where the keys are `'Monday'` through `'Sunday'`, and the values are the count of week days between those dates (both inclusive). To test your function, given `datetime(2015, 3, 14)` and `datetime(2015, 3, 14)` it will return `'Saturday':1, 'Sunday: 1`.



#### 5. `sloppy_timeit` that takes no inputs, but calls `datetime.now()` twice and find the difference between those two times in microseconds. Run this function a few times, what is the difference? This is why you want to use `timeit`, instead of timing things yourself.




## math

#### 1. `cube` that takes a number and returns that number cubed (using the power function in `math`).



#### 2. `quadratic_formula` that takes in three numbers (`a`, `b`, and `c`) and returns a tuple of the two values returned by the quadratic formula.



#### 3. `sine_degrees` that takes in a number in degrees and returns the sine of that number (remembering that the `math` library takes values in radians, not degrees.



#### 4. `sine_in_bits` that takes in a number `n` and prints out the sine function from 0 to 180 degrees in `n` steps. You will want to use your new function `sine_degrees` from above.



#### 5. `verify_tangent` that takes in a number (in radians) and prints the tangent of that number, and then prints the sine of that number divided by the cosine. This is just a check of the `math` library: tangent should be equal to the sine/cosine.



#### 6. `log_base_2` that takes a number and returns the log of that number, base 2.




## random

#### 1. `single_die_roll` that returns a random value from 1 to 6.



#### 2. `roll_a_six` that uses a `while` loop to print the result of `single_die_roll` again and again until you roll a six.



#### 3. `monte_carlo_dice` that takes in an integer `n` and performs `single_die_roll` n times, and then returns the average of the results. Use your new function for n equals: 100, 1000, 10000, and 100000, and compare the results.



#### 4. `double_choice` that takes in a list and returns two non-equal items that were selected from that list. Be careful, what if the list only has one item?



#### 5. `random_split` that takes in a number `x` (greater than 10), and returns two randomly selected numbers, one from zero to `x/2` and one from `x/2` to `x`.




## timeit

#### 1. Time each of the functions you above that you wrote for this problem set. Time them for several different numbers of trials (say, 10, 100, 10000, 100000), and then divide the resultant time by the number of trials. Which of the functions above are very fast? Which of the functions above can you make very slow by giving them different inputs?




[Back to Problem Set](problem_set_1_batteries.md)
