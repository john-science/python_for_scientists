# Modifying Strings - Solutions

####  1. Given an integer count of a number of donuts, print a string of the form: `'Number of donuts: <count>',` where `<count>` is the number passed in. However, if `count` is `10` or more, then use the word `'many'` instead of the `count`.

    # given integer count

    count_str = 'many'
    if count <= 10:
        count_str = str(count)
    
    print('Number of donuts: ' + count_str)

#### 2. Given a string `s`, print a string made of the first 2 and the last 2 charachters of the original string, so `'spring'` yields `'spng'`. However, if the string length is less than 2, print the empty string.

    # given string s
    
    if len(s) < 2:
        print('')
    else:
        print(s[:2] + s[-2:]

#### 3. Given a string `s`, print a string where all occurences of its first character have been changed to `'*'`, except do not change the first character itself (e.g. `'babble'` yields `'ba**le'`). Assume that the string is length 1 or more.

    # given string s
    
    first = s[0]
    new_s = s.replace(first, '*')
    new_s[0] = first
    print(new_s)

#### 4. Given strings `a` and `b`, print a single string with `a` and `b` separated by a space `'<a> <b>'`, except swap the first 2 characters of each string (e.g.  `'dog', 'dinner'` becomes `'dig donner'`). Assume `a` and `b` are length 2 or more.

    # given strings a and b
    
    temp = a[1]
    a[1] = b[1]
    b[1] = temp
    print(a + ' ' + b)

#### 5. Given a sentence as a string `s`, use a `for` loop to print each word in that sentence.

    # given a sentence string s
    
    for word in s.split(' '):
        print(word)

[Back to Problem Set](problem_set_2_strings.md)
