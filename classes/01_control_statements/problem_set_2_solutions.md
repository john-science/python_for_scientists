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
    new_s = first + new_s[1:]
    print(new_s)

#### 4. Given strings `a` and `b`, print a single string with `a` and `b` separated by a space `'<a> <b>'`, except swap the first 2 characters of each string (e.g.  `'dog', 'dinner'` becomes `'dig donner'`). Assume `a` and `b` are length 2 or more.

    # given strings a and b
    
    temp = a[1]
    a = a[0] + b[1] + a[2:]
    b = b[0] + temp + b[2:]
    print(a + ' ' + b)

#### 5. Given a sentence as a string `s`, use a `for` loop to print each word in that sentence.

    # given a sentence string s
    
    for word in s.split(' '):
        print(word)

#### 6. Start with the string `text = 'Emigrate'`, replace the letter `m` with `n`, replace the letter `r` with `m`, and remove the last two characters.

    text = 'Emigrate'
    new_text = text.replace('m', 'n').replace('r', 'm')[:-2]
    print(new_text)  # Enigma

#### 7. Start with the string `cipher = 'planbluring'`, replace the fifth character with a space, replace all `p`s with `A`, and replace the sixth character with `T`.

    cipher = 'planbluring'
    text = cipher[:4] + ' ' + cipher[5:]
    text = text.replace('p', 'A')
    text = text[:5] + 'T' + text[6:]
    print(text)

[Back to Problem Set](problem_set_2_strings.md)
