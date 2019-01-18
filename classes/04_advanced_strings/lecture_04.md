# Advanced Strings

## Quick Review

First, let's do a quick review of what we already know about strings in Python.

You know how to define strings:

```python
>>> s1 = "Hello "
>>> s2 = "World"
```

And how to add two strings:

```python
>>> s1 + s2
"Hello World"
```

You can also retrive a single letter from a string like it is an element of a list:

```python
>>> s1[0]
'H'
>>> s1[1]
'e'
```

You can also get the last character in a string, if that's easier:

```python
>>> s2[-1]
'd'
>>> s2[-2]
'l'
```

It is far less common, but you can even multiply strings:

```python
>>> 3 * 'hi'
'hihihi'
>>> 4 * 'Hello! '
'Hello! Hello! Hello! Hello! '
```

You can also take a `slice` of a string:

```python
>>> s2[1:4]
'orl'
>>> s1[0:4]
'Hell'
>>> s1[:4]
'Hell'
>>> s2[1:5]
'orld'
>>> s2[1:99999]  # error surpressed!
'orld'
```

Another really popular tool is `len`, which calculates the number of characters in a string:

```python
>>> len(s1)
6
>>> len(s2)
5
```


## String Operations

Python has a nice variety of tools to do commonly-desired things to strings.

### `lower`, `upper`, `capitalize` do what you'd think

```python
>>> "funKY tOwn".capitalize()
'Funky town'
>>> "funky tOwn".lower()
'funky town'
>>> "funky tOwn".upper()
'FUNKY TOWN'
```

### `split` splits a string using another string

```python
>>> "bright copper kettles and warm woolen mittens".split(" ")
['bright', 'copper', 'kettles', 'and', 'warm', 'woolen', 'mittens']
>>> "bright,copper,kettles,and,warm,woolen,mittens".split(",")
['bright', 'copper', 'kettles', 'and', 'warm', 'woolen', 'mittens']
>>> "bright copper kettles and warm woolen mittens".split('tt')
['bright copper ke', 'les and warm woolen mi', 'ens']
```

#### By default, `split` uses any white space (`' '`, `'\t'`,  or `'\n'`)

```python
>>> "funKY tOwn".split()
['funKY', 'tOwn']
>>> "funKY tOwn".capitalize().split()
['Funky', 'town']
```

Notice that by default, `split` uses spaces to split the string.

### `strip`, `join`, `replace` are also super useful:

```python
>>> csv_string = '  Dog,Cat,Spam, Defenestrate,1, 3.1415 \n\t'
>>> csv_string.strip()
'Dog,Cat,Spam, Defenestrate,1, 3.1415'
>>> csv_string.rstrip()
'  Dog,Cat,Spam, Defenestrate,1, 3.1415'
>>> csv_string.lstrip()
'Dog,Cat,Spam, Defenestrate,1, 3.1415 \n\t'
```
    
Notice `rstrip()` just strips the right side of the string, `lstrip()` just strips the left side, and `strip()` strips both.

### `join` allows you to combine a list of strings into one string:

```python
>>> zen = ['Simple', 'is', 'better', 'than', 'complex.']
>>> ' '.join(zen)
'Simple is better than complex.'
>>> under = ['python', 'naming', 'convension']
>>> '_'.join(under)
'python_naming_convension'
```

### `replace` strings in strings with other strings

```python
>>> csv_string = 'Dog,Cat,Spam,Defenestrate,1, 3.1415 \n\t'
>>> csv_string.strip().replace(' ', '')
'Dog,Cat,Spam,Defenestrate,1,3.1415'
>>> csv_string.strip().replace(' ', '').replace(',', '! ')
'Dog! Cat! Spam! Defenestrate! 1! 3.1415'
```

### `find` searches for a substring

If the string exists, it returns the index of the first time the string is found:

```python
>>> s = 'My Funny Valentine'
>>> s.find("M")
0
>>> s.find("y")
1
```

If the substring is not found, it returns a `-1`:

```python
>>> s.find("z")
-1
>>> s.find("Halloween")
-1
```
    
See if you understand this short example:

```python
>>> ss = [s, "Argentine","American","Quarentine"]
>>> for thestring in ss:
        if thestring.find("tine") != -1:
            print("'" + str(thestring) + "' contains 'tine'.")
'My Funny Valentine' contains 'tine'.
'Argentine' contains 'tine'.
'Quarentine' contains 'tine'.
```

## Type Conversions

This is a quick aside. Python has several methods built-in to do type coversions, just like we did with `str()` above. There are built-in type converters for each primitive type:

 * str
 * int
 * float
 * bool

And they all work much like you would expect:

```python
>>> int(3.0)
3
>>> int(3.1415926535897932384626)
3
>>> float(3)
3.0
>>> bool(0)
False
>>> bool(1)
True
>>> bool(2.0)
True
```

Notice that here Python equates `False` with `0` and `True` with `1` (or anything else that's not zero).

```python
>>> int(False)
0
>>> int(True)
1
>>> float(False)
0.0
>>> float(True)
1.0
```

#### `str` creates a string from another variable type

Here are some easy examples:

```python
>>> str(3)          # convert an integer to a string
'3'
>>> str(3.14)       # convert a float to a string
'3.14'
>>> str(True)       # convert a boolean to a string
'True'
>>> str([1, 2, 3])  # convert a list to a string
'[1, 2, 3]'
```

### And all of these can be used on strings

```python
>>> int("3")          # convert an string to a integer
3
>>> float("3.14")     # convert a string to a float
3.14
>>> bool("True")      # convert a string to a boolean
True
>>> bool("False")     # the Boolean of anything other than 0 is True
True
>>> bool("Anything")  # the Boolean of anything other than 0 is True
True
```

## Reading and Writing Text Files

Python has a really great interface for reading and writing text files. Everything can be done using the `open` function.

To read an existing text file, we might do:

```python
f = open('/full/path/to/ray_bradbury.txt', 'r')
```

To write text to a new file we might do:

```python
f = open('ray_bradbury.txt', 'w')
```

And if the text file already exists, and we want to `append` more lines to the end it (like you might do in a log file):

```python
f = open('ray_bradbury.txt', 'a')
```

Now, let's try a simple example of writing to a new file:

```python
>>> soft_rains = '''
"There will come soft rains and the smell of the ground,
And swallows circling with their shimmering sound;
And frogs in the pools singing at night,
And wild plum trees in tremulous white;
Robins will wear their feathery fire,
Whistling their whims on a low fence-wire;
And not one will know of the war, not one
Will care at last when it is done.
Not one would mind, neither bird nor tree,
if mankind perished utterly;
And Spring herself, when she woke at dawn
Would scarcely know that we were gone."
'''

>>> fout = open('ray_bradbury.txt', 'w')
>>> fout.write(soft_rains)
>>> fout.close()
```
    
It is very important that we remember to use the `close()` statement at the end. Python does a pretty good job of handling these details if you forget. But there is no subsitute for doing it right.

Now, let's say we want to add one extra line to the end of the file:

```python
>>> author_line = '             - Ray Bradbury'
>>> 
>>> fout = open('ray_bradbury.txt', 'w')
>>> fout.write(author_line)
>>> fout.close()
```

Darn, we just erased the original contents of the file. Python thought we wanted a fresh file, so it erased the old one. Instead, we should have used the `a` flag to append the extra line:

```python
>>> author_line = '             - Ray Bradbury'
>>> 
>>> fout = open('ray_bradbury.txt', 'a')
>>> fout.write(author_line)
>>> fout.close()
```

On the other hand, let's say we wanted to read this file. The most common solution is to read the entire file into a list of strings, where each element of the list is a line in the file:

```python
>>> fin = open('ray_bradbury.txt', 'r')
>>> lines = fin.readlines()
>>> fin.close()
>>> lines
['"There will come soft rains and the smell of the ground,\n', 'And swallows circling with their shimmering sound;\n', 'And frogs in the pools singing at night,\n', 'And wild plum trees in tremulous white;\n', 'Robins will wear their feathery fire,\n', 'Whistling their whims on a low fence-wire;\n', 'And not one will know of the war, not one\n', 'Will care at last when it is done.\n', 'Not one would mind, neither bird nor tree,\n', 'if mankind perished utterly;\n', 'And Spring herself, when she woke at dawn\n', 'Would scarcely know that we were gone."\n', '             - Ray Bradbury']
```

Another option is to just read the entire file into one big, long string:

```python
>>> fin = open('ray_bradbury.txt', 'r')
>>> lines = fin.read()
>>> fin.close()
>>> lines
'"There will come soft rains and the smell of the ground,\nAnd swallows circling with their shimmering sound;\nAnd frogs in the pools singing at night,\nAnd wild plum trees in tremulous white;\nRobins will wear their feathery fire,\nWhistling their whims on a low fence-wire;\nAnd not one will know of the war, not one\nWill care at last when it is done.\nNot one would mind, neither bird nor tree,\nif mankind perished utterly;\nAnd Spring herself, when she woke at dawn\nWould scarcely know that we were gone."\n             - Ray Bradbury'
```

If it's an old fixed-format text file (like Fortran prefers), you might just want to read a certain number of characters at a time. Which you can do with `read`:

```python
>>> fin = open('ray_bradbury.txt', 'r')
>>> fin.read(27)
'"There will come soft rains'
>>> fin.close()
```

## Reading and Writing Binary Files

Scientists frequently need to deal with [binary files](https://en.wikipedia.org/wiki/Binary_file). This can, in general, be quite complicated. But Python's `open` function takes care of the basics:

```python
>>> myfile = open('test_bin.txt', 'wb')
>>> for c in range(50, 70):
...     myfile.write(chr(c).encode())
... 
>>> myfile.close()
>>> myfile = open('test_bin.txt', 'rb')
>>> myfile.read()
b'23456789:;<=>?@ABCDE'
>>> myfile.close()
```

What we did above was: create a binary file and wrote in the binary characters with ASCII values from 50 to 69. The `chr` method was used to convert the integers to their character representation. Thus, when we read the file back in, we end up reading the characters, not the integers we wanted to store. This is just one of the many possible things you have to be careful of when dealing with binary files.

There are other caveats. Fortran binary files all have headers, which have to be read separately from the rest of the file. This involves some knowledge of the header format. Also different operating systems store files with different [endianness](https://en.wikipedia.org/wiki/Endianness). 

There is no "magic bullet" to read binary files. Some knowledge of your binary format will be needed to read or write the files correctly.

## Reading and Writing CSV Files

One of the most popular file formats for scientists is CSV (comma separated values). It is easily read by the human eye, and easy to write Python code to read and write. It is well worth the time to learn to do this right.

First, let's paste the following data into `radiation_dose.csv` (or try writing the file with one quick Python loop):

    source,dose (Sv),dose (BED)
    eating a banana,1.0E-7,1
    arm x-ray,1.0e-6,10
    dental x-ray,5.0e-6,50
    one day natural background,1.0e-5,100
    flight from LA to New york,4.e-5,400
    mammogram,4e-4,4000
    head CT scan,2.0e-3,20000
    chest CT scan,7.0e-3,70000
    max yearly radiation worker dose,5.0e-2,5e5
    lowest yearly dose linked to cancer,0.1,1e6
    usually fatal dase,4.0,4e7

### CSVs are Just Text Files

Well, we know how to read text files. And CSV files are just text files. So let's try reading the file like any other text file:

```python
>>> fin = open('radiation_dose.csv', 'r')
>>> lines = fin.readlines()
>>> fin.close()
>>> 
>>> header = lines[0].strip().split(',')
>>> header
['source', 'dose (Sv)', 'dose (BED)']
>>> for line in lines[1:]:
>>>     values = line.strip().split(',')
>>>     print(values[0], float(values[1]), float(values[2]))
```

Notice above the use of `strip()`. This is because we want to find the integer value of that last column, so we want to do `float('1')`, not `float('1\n')`.

Also notice that `split(',')` above to a long string of text and created a list of strings:

```python
>>> line = 'source,dose (Sv),dose (BED)\n'
>>> line.strip()
'source,dose (Sv),dose (BED)'
>>> line.strip().split(',')
['source', 'dose (Sv)', 'dose (BED)']
```

### Import the Standard CSV Library

Of course, so many people have wanted to read CSV files with Python that there is a standard library for it: `import csv`. There are two major ways to use Python's standard `csv` library to read CSV files: you can read the data into a list of lists, or a list of dictionaries. Both have their merits, so let's try them.

#### Read as Lists

How you read the CSV file should depend on what you want to do with the data. Sometimes it might be easiest to treat each line in the CSV file as a list:

```python
>>> import csv
>>> f = open('radiation_dose.csv', 'r')
>>> reader = csv.reader(f)
>>> for row in reader:
...     print(row)
... 
['source', 'dose (Sv)', 'dose (BED)']
['eating a banana', '1.0E-7', '1']
['arm x-ray', '1.0e-6', '10']
...
>>> f.close()
```

This is essentially the same as when we read the CSV file as a raw text file, except the stripping and splitting has been done for us.

#### Read as Dictionaries

Another popular option is to read each line of the CSV file into a dictionary, with the column headers as keys and the row split into values:

```python
>>> import csv
>>> f = open('radiation_dose.csv', 'r')
>>> dict_reader = csv.DictReader(f)
>>> for row in dict_reader:
...     print(row)
... 
{'dose (Sv)': '1.0E-7', 'source': 'eating a banana', 'dose (BED)': '1'}
{'dose (Sv)': '1.0e-6', 'source': 'arm x-ray', 'dose (BED)': '10'}
{'dose (Sv)': '5.0e-6', 'source': 'dental x-ray', 'dose (BED)': '50'}
... 
>>> f.close()
```

This approach is particularly handy if the CSV data will eventually be read into any kind of dictionary.


## Problem Sets

 * [Problem Set 1 - Working with Strings](problem_set_1_strings.py)
 * [Problem Set 1 - Solutions](problem_set_1_solutions.py)
 * [Problem Set 2 - Working with CSVs](problem_set_2_csv.md)


[Back to Syllabus](../../README.md)
