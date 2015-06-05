# Generating Random Numbers in NumPy

## Set 1 - Testing Flatness randint

1. Use `zeros` to create an array with 10 elements, name it `counts`.
2. Use a `for` loop to create 100,000 `random.randint` numbers less than 10. Add 1.0 to each element of `counts` that your random integer matches. (For instance, if your random number is 0, you would do counts[0] += 1.0. If your random number is 8, you would do counts[8] += 1.0.)
3. Create a new array `bins` where you divide each element in `counts` by 100,000.
4. Are all 10 spots in `bins` the same? If `random.randint` truly generated a "flat" random distribution, they should be. Perhaps they would look closer to 10% each if you did a bigger test. Try parts 1 through 3 again with more than 100,000 trials.

## Set 2 - Testing Flatness rand

1. Use `zeros` to create an array with 10 elements, name it `counts`.
2. Use a `for` loop to create 100,000 random decimals between zero and one (use `rand`). For each number you generate, multiple it by 10 and convert it to an integer using `int()`. Then add your number to the `counts` bin, as we did in part 2 of set 2.
3. Create a new array `bins` where you divide each element in `counts` by 100,000.
4. Are all 10 spots in `bins` the same? If `random.rand` truly generated a "flat" random distribution, they should be. Perhaps they would look closer to 10% each if you did a bigger test. Try parts 1 through 3 again with more than trials.

## Set 3 - Testing Flatness randn

Unlike `randint` and `rand` in Set 1, `randn` is *not* supposed to be flat. It is supposed to be a Normal Distribution.

1. Use `zeros` to create an array with 10 elements, name it `counts`.
2. Use a `for` loop to create 100,000 random decimals using `randn`. Take the absolute value (`abs`) of each of your numbers, then convert it to an integer using `int`. If your number is less than 10, add 1.0 to the appropriate element in your `counts` array, as in Sets 1 and 2 above.
3. Create a new array `bins` where you divide each element in `counts` by 100,000.
4. Take a look at `bins`, does it match a Normal Distribution? Perhaps it would look closer to Normal if you did a bigger test. Try parts 1 through 3 again with more trials.

## Set 4 - Shuffle & Choice

1. Use `arange` to create an array `a` with values 0 to 99.
2. Use `numpy.random.shuffle` to randomly re-order `a`.
3. Randomly select an element from `a` using `numpy.random.choice`.
4. Find the type of your selected element using `.dtype`.

## Solutions

* [Random Numbers - Solutions](problem_set_2_solutions.md)


[Back to Lecture](lecture_10.md)
