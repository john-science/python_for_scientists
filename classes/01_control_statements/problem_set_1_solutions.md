# Basic Control Flow - Solutions

#### 1. Print the numbers 1 through 10 with a `for` loop.
 
    for i in range(1, 11):
        print(i)
 
#### 2. Print the numbers 2 through 20 with a `while` loop.

    i = 2
    while i < 21:
        print(i)
        i += 1

#### 3. Using `range`, print only the odd numbers from 4 to 40.

    for n in range(5, 41, 2):
        print(n)

#### 4. Using an `if` statement inside a `for` loop, print only the odd numbers from 4 to 40.

    for i in range(4, 41):
        if i % 2 == 1:
            print(i)

#### 5. Using a `while` loop and a `break`, print the numbers from 10 down to 0.

    x = 10
    while True:
        print(x)
        x -= 1
        if x < 0:
            break

#### 6. Using a `for` loop and a `continue`, print only the even numbers from 1 to 30.

    for i in range(1, 31):
        if i % 2 == 1:
            continue
        print(i)

#### 7. Using a `range` as part of a `for` loop, loop through every number divsible by 5 below 100. Using an `if` statement, print only the even numbers from that set.

    for i in range(0, 101, 5):
        if i % 2 == 0:
            print(i)

#### 8. Using `type`, write an `if` statement that will only print a variable `x` if it is a string.

    if type(x) == str:
        print(x)

#### 9. Using a `for` loop, sum up the even numbers from 1 to 10,000.

    # using range
    sum = 0
    for i in range(2, 10001 2):
        sum += i
    
    print(sum)
    
    # or using an if-statement
    sum = 0
    for i in range(1, 10001):
        if i % 2 == 0:
            sum += i
    
    print(sum)

#### 10. Using a `while` loop, an `if-elif` block, and the `%` operator, find the smallest number that is evenly divisible by: 2, 3, 4, 5, 6, 10, and 12.

    i = 1
    while True:
        if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
            if i % 6 == 0 and i % 10 == 0 and i % 12 == 0:
                print(i)
                break
        i += 1
    

#### 11. Using `range` and `for`, sum all the numbers evenly divisble by 7, from 0 to 10000.

    sum = 0
    for i in range(0, 10001, 7):
        sum == i
    
    print(sum)


[Back to Problem Set](problem_set_1_flow_controls.md)
