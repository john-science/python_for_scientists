# Standard Libraries, Part 1 - Solutions


## datetime

#### 1. `pprint_date` that takes in a `datetime` object and returns a string formatted like: `Saturday, March 14, 2015 at 9:26AM`.

    def pprint_date(d):
        '''Return a pretty-printed form of a given date'''
        return d.strftime('%A, %B %d, %Y at %H:%M%p')

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

#### 4. `dow_dict` that takes a start date and an end date (as `datetime` objects) and returns a dictionary where the keys are `'Monday'` through `'Sunday'`, and the values are the count of week days between those dates (both inclusive). To test your function, given `datetime(2015, 3, 14)` and `datetime(2015, 3, 15)` it will return `'Saturday':1, 'Sunday: 1`.

    def dow_dict(start, end):
        '''Return a dictionary with the county of different weekdays
        between two given datetimes.'''
        dows = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0,
                'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 6}

        current = start
        while current <= end:
            dow = current.strftime('%A')
            dows[dow] += 1
        
        return dows

#### 5. `sloppy_timeit` that takes no inputs, but calls `datetime.now()` twice and find the difference between those two times in microseconds. Run this function a few times, what is the difference? This is why you want to use `timeit`, instead of timing things yourself.

    from datetime import datetime

    def sloppy_timeit():
        d1 = datetime.now()
        d2 = datetime.now()
        return (d2 - d1).microseconds
        
    >>> sloppy_timeit()
    15
    >>> sloppy_timeit()
    20
    >>> sloppy_timeit()
    19
    >>> sloppy_timeit()
    18


## math

#### 1. `cube` that takes a number and returns that number cubed (using the power function in `math`).

    import math

    def cube(n):
        '''calculates the cube of a number'''
        return math.pow(n, 3)

#### 2. `quadratic_formula` that takes in four numbers (`a`, `b`, and `c`) and returns a tuple of the two values returned by the quadratic formula.

    import math

    def quadratic_formula(a, b, c, x):
        '''return both results of the quadratic equation in a tuple'''
        numerator = math.sqrt(b * b - 4.0 * a * c)
        plus_numerator = ((-1.0 * b) + numerator) / (2.0 * a)
        minus_numerator = ((-1.0 * b) - numerator) / (2.0 * a)
        
        return (plus_numerator, minus_numerator)

#### 3. `sine_degrees` that takes in a number in degrees and returns the sine of that number (remembering that the `math` library takes values in radians, not degrees.

    from math import radians, sin

    def sine_degrees(deg):
        '''Take the sine of a number, in degrees)'''
        rads = radians(deg)
        return sin(rads)

#### 4. `sine_in_bits` that takes in a number `n` and prints out the sine function from 0 to 180 degrees in `n` steps. You will want to use your new function `sine_degrees` from above.

    def sine_in_bits(n):
        '''print the sine of 0 to 180 in n chunks'''
        for deg in range(0, 181, 180 / n):
            print(sine_degrees(deg))

#### 5. `verify_tangent` that takes in a number (in radians) and prints the tangent of that number, and then prints the sine of that number divided by the cosine. This is just a check of the `math` library: tangent should be equal to the sine/cosine.

    from math import cos, sin, tan
    
    def verify_tangent(rads):
        '''Just a quick, visual inspection that the
        tangent function is correct.'''
        t = tan(rads)
        c = cos(rads)
        s = sin(rads)
        print('\ntangent(' + str(rads) + ') = ' + str(t))
        print('\nsine(' + str(rads) + ') / cosine(' + str(rads) + ') = ' + str(s/c))

#### 6. `log_base_2` that takes a number and returns the log of that number, base 2.

    from math import log

    def log_base_2(n):
        '''a convenience math, to calculate log, base 2'''
        return log(n, 2)


## random

#### 1. `single_die_roll` that returns a random value from 1 to 6.

    from random import randint
    
    def single_die_roll():
        '''If you roll a die you get a randomly selected number,
        from 1 to 6, inclusive.'''
        return randint(1, 6)

#### 2. `roll_a_six` that uses a `while` loop to print the result of `single_die_roll` again and again until you roll a six.

    def roll_a_six():
        '''print out the results of random dice rolls,
        until you get a six.'''
        num = -999
        while num != 6:
            num = single_die_roll()
            print(num)

#### 3. `monte_carlo_dice` that takes in an integer `n` and performs `single_die_roll` n times, and then returns the average of the results. Use your new function for n equals: 100, 1000, 10000, and 100000, and compare the results.

    def monte_carlo_dice(n):
        '''roll Python's fair dice n times, and average the results'''
        total = 0
        for i in range(n):
            total += single_die_roll()

        return total / float(n)
        
    >>> monte_carlo_dice(100)
    3.75
    >>> monte_carlo_dice(1000)
    3.497
    >>> monte_carlo_dice(10000)
    3.4719
    >>> monte_carlo_dice(100000)
    3.50094
    >>> monte_carlo_dice(1000000)
    3.498375
    >>> monte_carlo_dice(10000000)
    3.5005983

Now, because these are random numbers, your average probably won't come out looking just like mine. But as you put greater and greater `n` values into your function, you should notice the results converge to `3.5`. This is because the [expectation value](https://en.wikipedia.org/wiki/Expected_value) of a fair dice roll is `3.5`.

#### 4. `double_choice` that takes in a list and returns two non-equal items that were selected from that list. Be careful, what if the list only has one item?

    from random import choice

    def double_choice(lst):
        '''select two different elements from a list'''
        # This check makes sure that there is more than
        # one unique element in the list.
        if len(set(lst)) <= 1:
            return None
        
        item1 = choice(lst)
        item2 = choice(lst)
        # This loop makes sure I didn't accidentally
        # select the same element twice.
        while item2 == item1:
            item2 = choice(lst)
        
        return(item1, item2)

#### 5. `random_split` that takes in a number `x` (greater than 10), and returns two randomly selected numbers, one from zero to `x/2` and one from `x/2` to `x`.

    def random_split(x):
        '''find two random numbers, from the bottom and top half
        of a given number'''
        rand1 = random()
        rand2 = random()
        
        num1 = (x / 2) * rand1
        num2 = ((x / 2) * rand2) + (x / 2)
        
        return(num1, num2)

#### 6. `random_integer` that uses `random.random()` to produce a random integer between between a min and a max number (just like `random.randint`).

    from random import random

    def random_integer(min, max):
        '''creates a random integer between a
        min and a max value'''
        return min + int((max - min) * random())

#### 7. `random_list_choice` that uses the `random_integer` above to randomly select an item from a list (just like `random.choice`).

    def random_list_choice(lst):
        '''randomly selects an item from a list'''
        return lst[random_integer(0, len(lst))]

## timeit

#### 1. Time each of the functions you above that you wrote for this problem set. Time them for several different numbers of trials (say, 10, 100, 10000, 100000), and then divide the resultant time by the number of trials. Which of the functions above are very fast? Which of the functions above can you make very slow by giving them different inputs?

I won't show *all* the results, but here is a quick look at `monte_carlo_dice`:

    >>> from timeit import timeit
    >>>
    >>> timeit(str(monte_carlo_dice(1000)), number=10)
    9.5367431640625e-07
    >>> timeit(str(monte_carlo_dice(1000)), number=100)
    1.9073486328125e-06
    >>> timeit(str(monte_carlo_dice(1000)), number=1000)
    1.0967254638671875e-05
    >>> timeit(str(monte_carlo_dice(1000)), number=10000)
    0.00011301040649414062
    >>> 
    >>> # now let's try a bigger input to monte_carlo_dice
    >>> timeit(str(monte_carlo_dice(100000)), number=10)
    1.1920928955078125e-06
    >>> timeit(str(monte_carlo_dice(100000)), number=100)
    1.9073486328125e-06
    >>> timeit(str(monte_carlo_dice(100000)), number=1000)
    1.3828277587890625e-05
    >>> timeit(str(monte_carlo_dice(100000)), number=10000)
    0.0001270771026611328
    >>> timeit(str(monte_carlo_dice(100000)), number=100000)
    0.0012660026550292969

So, what we're seeing is that the input to `monte_carlo_dice` makes a BIG difference to the run times. That's no suprise. You will notice that is not true for `random_split`.

[Back to Problem Set](problem_set_1_batteries.md)
