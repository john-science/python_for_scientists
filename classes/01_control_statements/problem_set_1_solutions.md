# Basic Control Flow - Solutions

#### 1. Print the numbers 3 through 13 using a `for` loop and a `range` statement.
 
    for i in range(1, 11):
        print(i)
 
#### 2. Print the numbers 2 through 20 using a `while` loop.

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

#### 7. Using `range` as part of a `for` loop, loop through every number evenly divsible by 5 from zero to 100. Using an `if` statement, print only the even numbers from that set.

    for i in range(0, 101, 5):
        if i % 2 == 0:
            print(i)

#### 8. Using `type`, write an `if` statement that will only print a variable `x` if it is a string.

    if type(x) == str:
        print(x)

#### 9. Using a `for` loop, sum the even numbers from 1 to 10,000.

    # using range
    sum = 0
    for i in range(2, 10001, 2):
        sum += i
    
    print(sum)
    
    # or using an if-statement
    sum = 0
    for i in range(1, 10001):
        if i % 2 == 0:
            sum += i
    
    print(sum)
    
    # answer is: 25005000

#### 10. Using a `while` loop, an `if-elif` block, and the `%` operator, find the smallest number that is evenly divisible by: 1, 2, 3, 4, 5, 6, 10, and 12.

    i = 1
    while True:
        if i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
            if i % 6 == 0 and i % 10 == 0 and i % 12 == 0:
                print(i)
                break
        i += 1
    
    # answer: 60 (This is why there are 60 seconds in a minute and 60 minutes in an hour.)

#### 11. Using `range` and `for`, sum all the numbers evenly divisble by 7, from 0 to 10000.

    sum = 0
    for i in range(0, 10001, 7):  # 0, 7, 14, 21, ...
        sum += i
    
    print(sum)
    
    # answer: 7142142

#### 12. Using `for` or `while` and/or an `if` statement, print the numbers `10` through `1`, then the string `"Blast off!"`.

    # Version 1: Using for, range, and an if statement
    for count in range(10, 0, -1):
        if count > 0:
            print(count)
        else:
            print("Blast off!")

    # Version 2: Use a while, but no if
    count = 10
    while count > 0:
        print(count)
        count -= 1
    
    print("Blast off!")

#### 13. Use a `while` loop to calculate the sum of the first 100 odd integers.

    found = 0  # How many odd integers have I found so far?
    sum = 0    # Place to store the sum, thus far.
    i = 1      # Place to store what integer I'm on.
    while found < 100:
        sum += i    # increment the sum thus far
        found += 1  # we found another odd integer
        i += 2      # Every other number is odd
    
    print(sum)
    
    # answer: 10000

#### 14. Use a `for` loop to calculate the 10th Triangular Number. The nth Triangular Number is: `1 + 2 + 3 + ... + n`.

    sum = 0
    for i in range(1, 11):
        sum += i
    
    print(sum)
    
    # answer:55

Actually, if you looked at the Wikipedia link in the problem set, you would see that the nth Triangular Number can be calculated by: `n * (n + 1) / 2`. This would be a great way to check your work for any `n`.

#### 15. Using two `for` loops (one nested inside the other), print out the factorials of `10` through `1` (in that order).

    for n in range(10, 0, -1):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(fact)

#### 16. Below is the multiplication table up to 2. Following that example, use two nested `for` loops to print the multiplication table up to 5.

    # In this solution, I build each tab-seperated line seperately.

    print('x\t1\t2\t3\t4\t5')  # header
    for row in range(1, 6):
        line = str(row)
        for col in range(1, 6):
            line += '\t' + str(col * row)
        print(line)

[Back to Problem Set](problem_set_1_flow_controls.md)
