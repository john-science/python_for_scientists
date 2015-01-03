# Flow Controls

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

Try to build you own example using `continue` in a `for` loop, to only print the even numbers from 1 to 12.
