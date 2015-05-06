# Python Data Structures

## Lists

1. Initialize a list called "boys" with the elements: "Fred", "George", "Percy", "Ron".
2. Initialize a list called "girls" with elements: "Giney".
3. Print both lists.
4. Print the first element in `girls`.
5. Find two or three ways to print the last element in `boys`.
6. Add the element "Charles" to the "boys" list.
7. Add the `boys` and `girls` together, and save the results as a list called "weasleys".
8. Use the `.sort()` method to sort the "weasleys" list into alphabetical order.
9. Print the length of `weasleys`.
10. Using a `for` loop, iterate through `weasleys` and add the first letter of each name to into a string called "firsts", then print that string.
11. Using a `for` loop and an `if` statement, iterate through `weasleys` and create a new list, "reds", of only names longer than 4 letters.
12. Using an `in` statement, test if "Charles" is in the `weasleys`.
13. Using a slice (`[:]`), take a slice of all but the first and last elements of `weasleys`.
14. Using two slices (`[:]`), add the first element of `boys` to the last element of `weasleys`.

#### Sorting

In general, sorting a list of items is a classic, but difficult computational tast. However, it has been studied so thoroughly, that there are two methods built right into Python to do this for you:

    lst = [7, 4, 3, 1, 8, 4, 333, -1234]
    lst.sort()
    print(lst)
    
    lst = [7, 4, 3, 1, 8, 4, 333, -1234]
    sorted(lst)

So, what is the difference between `sort` and `sorted` above?

## Dictionaries

1. Create an empty dictionary named "tardis".
2. Add a key/value pair to `tardis` of "Doctor"/"Who".
3. Add a key/value pair to the `tardis` dictionary of "Dalek"/"Evil".
4. Print the `tardis` dictionary. Print the keys and the values in `tardis`.
5. Change the value of "Dalek" to "Exterminate"
6. Add the key/value pair "Companion"/"Human" to `tardis`.
7. Print `tardis` (in two different ways).
8. Using a `for` loop and `.keys()`, print the values of the `tardis`.
9. Without using `.keys()` or `.values()`, use a `for` loop to print the values of the `tardis`.
10. **Save the Doctor!** Remove the "Dalek" key from the dictonary.
11. Print `tardis`.
12. Find the number of keys in the `tardis`.
13. Using `sorted` and a slice (`[:]`), print the `keys` of `tardis` in reverse alphabetical order.

## Tuples

This will be short, because tuples are so much like lists.

1. Create a tuple called "months" containing the words "January" and "February".
2. Add "March" to the "months" tuple.
3. Change "January" to "June".
4. Return the first element in "months"
5. Return the last element in "months" in two or three different ways.

## Sets

1. Create a empty sets called "insects".
2. One-at-a-time, add these elements to insects: "6 legs", "exoskeleton", "3-part bodies", "small", "lay eggs"
3. Create a new set called "spiders" that starts off including the elements: "8 legs", "spin webs", "2-part bodies", "small", "lay eggs"
4. Print both sets.
5. Find the intersection of both sets.
6. Determine if either set is a subset of the other.
7. Add "not cuddly" to the spider set, and print.
8. Remove the "not cuddly" from the spider set, and print.

## Solutions

 * [Data Structures - Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_02.md)
