# Flow Controls

#### If Statements

Python has pretty much all of what you use:

    if...elif...else,  for,  while

As well as:

    break, continue (within loops)

Does not have:

    case (explicitly), goto

Does have: `pass`

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
