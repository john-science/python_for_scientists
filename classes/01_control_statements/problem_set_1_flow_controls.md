# Flow Controls

## Continue, Break, and Pass

The major Python control statements we have already seen:

    for,  while, if...elif...else

But there are also three minor control statements:

    continue, break, pass

These are used in conjunction with the major control statements, to allow for great flexibility and to help deal with special cases.

### The continue Statement

The `continue` statement in Python returns the control to the beginning of the `for` or `while` loop. The `continue` statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.

    # First Example
    for letter in 'Python':
        if letter == 'h':
            continue
         print('Current Letter: ' + letter)
    
    # Second Example
    var = 10
    while var > 0:              
        var = var - 1
        if var == 5:
            continue
        print('Current variable value :' + str(var))

    print("Good bye!")

This will produce following result:

    Current Letter : P
    Current Letter : y
    Current Letter : t
    Current Letter : o
    Current Letter : n
    Current variable value : 10
    Current variable value : 9
    Current variable value : 8
    Current variable value : 7
    Current variable value : 6
    Current variable value : 4
    Current variable value : 3
    Current variable value : 2
    Current variable value : 1
    Good bye!

Now, try this yourself. Use the `continue` statement and a `for` loop to print just the odd numbers from 1 to 20.  (HINT: `range(1, 20)`)


### Syntatic Sugar

Flow is done within blocks (where indentation matters):

    x = 1
    if x > 0:
        print("yo")
    else:
        print("dude")

A quick note colons & indentations (tabbed or spaced):

    x = 1
    if x > 0:
          print('yo')
    else:
               print('dude')

You can also put a whole if-else statment on one line:

    "yo" if x > 0 else "dude"

One important way to control the flow of a program is to use `break`:

    x = 1
    y = 0
    while True:
        print("yo" if x > 0 else "dude")
        x *= -1
        y += 1
        if y > 100:
            break

Blocks can not be empty in Python:

    if x == "spam for dinner":
        print "I will destroy the universe"
    else:
        # I'm fine with that. I'll do nothing
        pass

## Problems

 1. Print the numbers 1 through 10 with a `for` loop.
 2. Print the numbers 2 through 20 with a `while` loop.
 3. Using `range`, print only the odd numbers from 4 to 40.
 4. Using an `if` statement inside a `for` loop, print only the odd numbers from 4 to 40.
 5. Using a `while` loop and a `break`, print the numbers from 10 down to 0.
 6. Using a `for` loop and a `continue`, print only the even numbers from 1 to 30.
 7. Using a `range` as part of a `for` loop, loop through every number divsible by 5 below 100. Using an `if` statement, print only the even numbers from that set.
 8. Using `type`, write an `if` statement that will print a variable `x` if it is a string, but not if it is anything else.
 9. Using a `for` loop, sum up the even numbers from 1 to 10,000.
 10. Using a `while` loop, an `if-elif` block, and the `%` operator, find the smallest number that is evenly divisible by: 2, 3, 4, 5, 6, 10, and 12.
 11. Using `range` and `while`, sum all the numbers evenly divisble by 7, from 0 to 10000.


[Back to Lecture](lecture_01.5.md)
