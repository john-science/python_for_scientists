# Python Standard Libraries, Part 1


## datetime

Write a function named:

1. `pprint_date` that takes in a `datetime` object and returns a string formatted like: `Saturday, March 14, 2015 at 9:26AM`.
2. `days_diff` that takes two `datetime` objects and returns the number of days between them. Use this function to determine how many days you've been alive.
3. `apollo_dates` that takes two `datetime` objects and prints each date formatted nicely, including the day-of-week. Use this function to print out the dates of the Apollo 11 moon-landing mission, which left the Earth on July 16th, 1969 and landed safely again on July 24th, 1969.
4. `dow_dict` that takes a start date and an end date (as `datetime` objects) and returns a dictionary where the keys are `'Monday'` through `'Sunday'`, and the values are the count of week days between those dates (both inclusive). To test your function, given `datetime(2015, 3, 14)` and `datetime(2015, 3, 15)` it will return `'Saturday':1, 'Sunday: 1`.
5. `sloppy_timeit` that takes no inputs, but calls `datetime.now()` twice and find the difference between those two times in microseconds. Run this function a few times, what is the difference? This is why you want to use `timeit`, instead of timing things yourself.


## math

Write a function named:

1. `cube` that takes a number and returns that number cubed (using the power function in `math`).
2. `quadratic_formula` that takes in four numbers (`a`, `b`, `c`, and `x`) and returns a tuple of the two values returned by the [quadratic formula](https://en.wikipedia.org/wiki/Quadratic_formula).
3. `sine_degrees` that takes in a number in degrees and returns the sine of that number (remembering that the `math` library takes values in radians, not degrees.
4. `sine_in_bits` that takes in a number `n` and prints out the sine function from 0 to 180 degrees in `n` steps. You will want to use your new function `sine_degrees` from above.
5. `verify_tangent` that takes in a number (in radians) and prints the tangent of that number, and then prints the sine of that number divided by the cosine. This is just a check of the `math` library: tangent should be equal to the sine/cosine.
6. `log_base_2` that takes a number and returns the log of that number, base 2.


## random

Write a function named:

1. `single_die_roll` that returns a random value from 1 to 6.
2. `roll_a_six` that uses a `while` loop to print the result of `single_die_roll` again and again until you roll a six.
3. `monte_carlo_dice` that takes in an integer `n` and performs `single_die_roll` n times, and then returns the average of the results. Use your new function for n equals: 100, 1000, 10000, and 100000, and compare the results.
4. `double_choice` that takes in a list and returns two non-equal items that were selected from that list. Be careful, what if the list only has one item?
5. `random_split` that takes in a number `x` (greater than 10), and returns two randomly selected numbers, one from zero to `x/2` and one from `x/2` to `x`.


## timeit

1. Time each of the functions you above that you wrote for this problem set. Time them for several different numbers of trials (say, 10, 100, 10000, 100000), and then divide the resultant time by the number of trials. Which of the functions above are very fast? Which of the functions above can you make very slow by giving them different inputs?


## Solutions

 * [Standard Libraries, Part 1 - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_09.md)
