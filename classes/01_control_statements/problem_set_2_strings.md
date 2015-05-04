# Modifying Strings - Problems

 1. Given an integer count of a number of donuts, return a string of the form: `'Number of donuts: <count>',` where `<count>` is the number passed in. However, if `count` is `10` or more, then use the word `'many'` instead of the `count`.
 2. Given a string `s`, return a string made of the first 2 and the last 2 charachters of the original string, so `'spring'` yields `'spng'`. However, if the string length is less than 2, return the empty string.
 3. Given a string `s`, return a string where all occurences of its first character have been changed to `'*'`, except do not change the first character itself (e.g. `'babble'` yields `'ba**le'`). Assume that the string is length 1 or more.
   * **Hint**: `s.replace(stra, strb)` returns a version of string `s` where all instances of `stra` have been replaced by `strb`.
 4. Given strings `a` and `b`, return a single string with `a` and `b` separated by a space `'<a> <b>'`, except swap the first 2 characters of each string (e.g.  `'dog', 'dinner'` becomes `'dig donner'`). Assume `a` and `b` are length 2 or more.
 5. Given a sentence as a string `s`, use a `for` loop to print each word in that sentence.
    * **Hint**: `s.split(',')` will break a string into bits, using commas as a seperator.

#### Where did these problems come from?

The first four problems were taken from the Google Code guide to Python Strings [here](https://developers.google.com/edu/python/strings).

## Solutions

 * [Modifying String - Solutions](problem_set_2_solutions.md)

[Back to Lecture](lecture_01.5.md)
