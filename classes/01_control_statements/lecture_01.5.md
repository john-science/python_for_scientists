## Control Statements

#### for loops

Basically, a `for` loop just does something for every value in a list. (Lists will be discussed in the next class.) For instance:

    new_list = [1950, 'There Will Come Soft Rains', 'Ray Bradbury', 2026]
    
    for element in new_list:
        print(element)

Try that out yourself and see, when the loop executes, it runs through all of the values in the list mentioned after `in`. It then puts them into `element`, and executes through the loop, each time with `element` being worth something different. Let's write another example, printing the square of the odd numbers from `1` to `10`:

    for number in range(1, 11, 2):
        print(number * number)

We also just learned about the `range` function. The `range` function produces a list, given: `start`, `end`, and `step` value2, though the `step` value is optional. For instance:

    >>> range(1, 5, 2)
    [1, 3]
    >>> range(1, 5)
    [1, 2, 3, 4]
    >>> range(1, 30, 7)
    [1, 8, 15, 22, 29]

(**NOTE**: As you can see above, the `start` value is *inclusive* and the `end` value is *exclusive*.)

#### while loops

A `while` loop does something until its main condition is no longer met:

    a = 0
    while a < 10:
        a = a + 1
        print(a)

The above loop will print the numbers `0` through `10` and then comparison between `a` and `10` will be no longer true, and the loop will terminate. You can also create more complicated predicates for the while loop:

    n = 15
    while n > 0 and n < 30:
        n -= 3  # this is the same as `n = n - 3`
        print(n)

The above loop will print the numbers 15, 12, 9, 6, 3 and then the complicated predicate will no longer be true, and the loop will terminate.

Unlike your typical `for` loop, `while` loops leave open an interesting possibility. What if the predicate is *never* true?

    >>> n = 7.0
    >>> while n > 0:
    ...     n += 0.5
    ... 

This is called an `infinte loop`, because it would never terminate on its own. This is, obviously, not a good thing.

#### if statements

![spam and eggs](http://upload.wikimedia.org/wikipedia/commons/a/a7/SPAM_and_Eggs.jpg)

In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability. The simplest form is the if statement, which has the genaral form:

    if PREDICATE:
        BODY STATEMENTS

In this case, only if the predicate is true is the body of the statement executed. For example:

    food = 'spam'
    
    if food == 'spam':
        print('Ummmm, my favorite!')
        print('I feel like saying it 100 times...')
        print(100 * (food + '! '))

Above is the basic `if` statement. You will use these to control the flow of the program. But what if you want to execute a different block of code if the predicate isn't satisfied? Well, you could do this:

    food = 'spam'
    
    if food == 'spam':
        print('Joy!')
    
    if food != 'spam':
        print('Sadness...')

But the above logic is *so* common, and needed so often, that Python provides a shortcut:

    if food == 'spam':
        print('Ummmm, my favorite!')
    else:
        print("No, I won't have it. I want spam!")

There is another option, what if you want to have several different conditionals chained together, to execute one of many different blocks of code, based on various predicates? That is the purpose of the `elif` symbol:

    if food == 'spam':
        print('Mmmmm, my favorite!')
    elif food == 'spam and eggs':
        print('Acceptable. I can pick out the eggs.')
    elif food == 'spam and bacon':
        print('Acceptable. I can pick out the bacon.')
    else:
        print("No, I won't have it. I want spam!")

Lastly, the `else` symbol is always optional:

    if food == 'spam':
        print('Mmmmm, my favorite!')
    elif food == 'spam and eggs':
        print('Acceptable. I can pick out the eggs.')

## Indentation

Did you notice in the `for` and `while` loops above how the content *inside* the loop was indented? That indentation is how Python decides what logic is contained within a loop, function, or class (more on those later). Unlike in other languages you might have seen, the indentation *really* matters in Python.

`White Space` is very important in Python.

![white space](http://imgs.xkcd.com/comics/python.png)

Here is an example of a correctly (though confusingly) indented piece of Python code:

    if n == 0:
     return 0
    elif n == 1:
          return 1
    else:
      return (n - 1) + (n - 2)

The following example shows various indentation errors:

        if n == 0:               # error: first line indented
    return 0                     # error: not indented
    elif n == 1:
          return 1
     else:                       # error: inconsistent dedent
       return (n - 1) + (n - 2)

In the end, the only way to make your code correct *and* readable is to be consistent with your indents. Do the same thing every time. The standard is four spaces per indent:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n - 1) + (n - 2)

## Comments!

> You are what you comment.

If you write code and there are no comments and no documentation, the code doesn't exist. No one will want to touch it, and they won't be able to understand it if they do.

    # this is the first comment
    spam = 1  # and this is the second comment
              # ... and now a third!
    text = "# This is not a comment because it's inside quotes."
    
    """This is an especially long comment,
    that takes up two lines."""

    '''This is another especially long comment,
    that takes up multiple
    lines.
    '''

## Problem Sets

 * [Basic Control Flow](problem_set_1_flow_controls.md)
 * [Modifying Strings](problem_set_2_strings.py)

## Further Reading

 * [Python Tutorial: Conditional Statements](http://www.python-course.eu/conditional_statements.php)


[Back to Syllabus](../../README.md)
