# Advanced Strings

## String Operations

Python has a nice variety of tools to do commonly-desired things to strings.

#### `lower`, `upper`, `capitalize` do what you'd think:

    >>> "funKY tOwn".capitalize()
    'Funky town'
    >>> "funky tOwn".lower()
    'funky town'
    >>> "funky tOwn".upper()
    'FUNKY TOWN'

#### `split` splits a string using another string:

    >>> "funKY tOwn".split()
    ['funKY', 'tOwn']
    >>> "funKY tOwn".capitalize().split()
    ['Funky', 'town']
    >>> [x.capitalize() for x in "funKY tOwn".split()]
    ['Funky', 'Town']
    >>> "I want to take you to, funKY tOwn".split("u")
    ['I want to take yo', ' to, f', 'nKY tOwn']
    >>> "I want to take you to, funKY tOwn".split("you")
    ['I want to take ', ' to, funKY tOwn']

Notice that by default, `split` uses spaces to split the string.

#### `strip`, `join`, `replace` are also super usefule:

    >>> csv_string = 'Dog,Cat,Spam,Defenestrate,1, 3.1415 \n\t'
    >>> csv_string.strip()
    'Dog,Cat,Spam,Defenestrate,1, 3.1415'
    >>> clean_list = [x.strip() for x in csv_string.split(",")]
    >>> clean_list
    ['Dog', 'Cat', 'Spam', 'Defenestrate', '1', '3.1415']
    
#### `join` allows you to combine a list of strings into one:

    >>> print ",".join(clean_list)
    'Dog,Cat,Spam,Defenestrate,1,3.1415'
    >>> print "\t".join(clean_list)
    Dog! Cat! Spam!
    Defenestrate!1! 3.1415

#### `replace` strings in strings with other strings

    >>> csv_string = 'Dog,Cat,Spam,Defenestrate,1, 3.1415 \n\t'
    >>> alt_csv = csv_string.strip().replace(' ', '')
    >>> alt_csv
    'Dog,Cat,Spam,Defenestrate,1,3.1415'
    >>> print csv_string.strip().replace(' ', '').replace(',', '\t')
    Dog! Cat! Spam!
    Defenestrate!1! 3.1415

#### `find` searches for a substring, and returns the index of the first found:

    >>> s = 'My Funny Valentine'
    >>> s.find("y")
    1
    >>> s.find("y",2)
    7
    >>> s[s.find("Funny"):]
    'Funny Valentine'
    >>> s.find("z")
    -1
    >>> ss = [s,"Argentine","American","Quarentine"]
    >>> for thestring in ss:
            if thestring.find("tine") != -1:
                print "'" + str(thestring) + "' contains 'tine'."
    'My Funny Valentine' contains 'tine'.
    'Argentine' contains 'tine'.
    'Quarentine' contains 'tine'.

#### `str` casts a variable to a string format, where available:

    >>> str(3)
    '3'
    >>> str(3.14)
    '3.14'
    >>> str(True)
    'True'
    >>> str(type(3.14))
    "<type 'float'>"
    >>> str(True and False)
    'False'
    >>> str(1 + 2 + 3 + 4 + 5.0)
    '15.0'

Not everything can be converted using `str()`, only classes which have a `__str__` method. (We'll see more about classes later.)

## Reading and Writing Text Files

Python has one of the most convenient interfaces for reading and writing text files of any language. Everything can be done using the `open` function.

To read an existing text file, we might do:

    f = open('ray_bradbury.txt', 'r')

To write text to a new file we might do:

    f = open('ray_bradbury.txt', 'w')

And if the text file already exists, and we want to `append` more lines to the end of the file (as you might with a log file), we might do:

    f = open('ray_bradbury.txt', 'a')

Now, let's see an example of how we would actualy write text to a new text file:

    >>> soft_rains = '''"There will come soft rains and the smell of the ground,
    ... And swallows circling with their shimmering sound;
    ... And frogs in the pools singing at night,
    ... And wild plum trees in tremulous white;
    ... Robins will wear their feathery fire,
    ... Whistling their whims on a low fence-wire;
    ... And not one will know of the war, not one
    ... Will care at last when it is done.
    ... Not one would mind, neither bird nor tree,
    ... if mankind perished utterly;
    ... And Spring herself, when she woke at dawn
    ... Would scarcely know that we were gone."
    ... '''
    ... 
    >>> fout = open('ray_bradbury.txt', 'w')
    >>> fout.write(soft_rains)
    >>> fout.close()
    
It is very important that we remember to use the `close()` statement at the end. Python does a pretty good job of handling these details if you forget. But there is no subsitute for doing it right.

Now, let's say we want to add one extra line to this file:

    >>> author_line = '             - Ray Bradbury'
    >>> 
    >>> fout = open('ray_bradbury.txt', 'w')
    >>> fout.write(author_line)
    >>> fout.close()

But darn, we just erased the original contents of the file. Python thought we wanted a fresh file, so it erased the old one.  That was not what we wanted. Instead, we should have used the `a` flag to append the extra line:

    >>> author_line = '             - Ray Bradbury'
    >>> 
    >>> fout = open('ray_bradbury.txt', 'a')
    >>> fout.write(author_line)
    >>> fout.close()

On the other hand, let's say we wanted to read this file. The most common solution is to read the entire file into a list of strings, where each element of the list is a line in the file:

    >>> fin = open('ray_bradbury.txt', 'r')
    >>> lines = fin.readlines()
    >>> fin.close()
    >>> lines
    ['"There will come soft rains and the smell of the ground,\n', 'And swallows circling with their shimmering sound;\n', 'And frogs in the pools singing at night,\n', 'And wild plum trees in tremulous white;\n', 'Robins will wear their feathery fire,\n', 'Whistling their whims on a low fence-wire;\n', 'And not one will know of the war, not one\n', 'Will care at last when it is done.\n', 'Not one would mind, neither bird nor tree,\n', 'if mankind perished utterly;\n', 'And Spring herself, when she woke at dawn\n', 'Would scarcely know that we were gone."\n', '             - Ray Bradbury']

Another option is to just read the entire file into one big, long string:

    >>> fin = open('ray_bradbury.txt', 'r')
    >>> lines = fin.read()
    >>> fin.close()
    >>> lines
    '"There will come soft rains and the smell of the ground,\nAnd swallows circling with their shimmering sound;\nAnd frogs in the pools singing at night,\nAnd wild plum trees in tremulous white;\nRobins will wear their feathery fire,\nWhistling their whims on a low fence-wire;\nAnd not one will know of the war, not one\nWill care at last when it is done.\nNot one would mind, neither bird nor tree,\nif mankind perished utterly;\nAnd Spring herself, when she woke at dawn\nWould scarcely know that we were gone."\n             - Ray Bradbury'

If the file is of the old fixed-format Fortran type, you might just want to read a certain number of characters at a time. Which you can also do with `readlines`:

    >>> fin = open('ray_bradbury.txt', 'r')
    >>> fin.read(27)
    '"There will come soft rains'
    >>> fin.close()

## Reading and Writing Binary Files

Scientists frequently need to deal with [binary files](https://en.wikipedia.org/wiki/Binary_file). This can, in general, be quite complicated. But Python's `open` function takes care of the basics:

    >>> myfile = open('test_bin.txt', 'wb')
    >>> for c in range(50, 70):
    ...     myfile.write(chr(c))
    ... 
    >>> myfile.close()
    >>> myfile = open('test_bin.txt', 'rb')
    >>> myfile.read()
    '23456789:;<=>?@ABCDE'
    >>> myfile.close()

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

    >>> fin = open('radiation_dose.csv`, 'r')
    >>> lines = fin.readlines()
    >>> fin.close()
    >>> 
    >>> header = lines[0].strip().split(',')
    >>> header
    ['source', 'dose (Sv)', 'dose (BED)']
    >>> for line in lines:
    >>>     values = line.strip().split(',')
    >>>     print(values[0], float(values[1]), int(values[2]))

Notice above the use of `strip()`. This strips all of the line endings and spaces from the end of the line. We do this because later on we want to find the integer value of the last column `int(values[2])`. When doing that we want to do `int('1')`, not `int('1\n')`.

Also notice that `split(',')` above to a long string of text and created a list of strings:

    >>> line = 'source,dose (Sv),dose (BED)\n'
    >>> line.strip()
    'source,dose (Sv),dose (BED)'
    >>> line.strip().split(',')
    ['source', 'dose (Sv)', 'dose (BED)']
    >>> line.strip().split('e')
    ['source,dos', ' (Sv),dos', ' (BED)']

### Import the Standard CSV Library

Of course, so many people have wanted to read CSV files with Python that there is a standard library for it: `import csv`. There are two major ways to use Python's standard `csv` library to read CSV files: you can read the data into a list of lists, or a list of dictinoaries. Both have their merits, so let's try them.

#### Read as Lists

How you read the CSV file should depend on what you want to do. Some times it might be easest just to read each line in the CSV file into an array of strings, for further manipulation:

    >>> import csv
    >>> f = open('radiation_dose.csv', 'r')
    >>> reader = csv.reader(f)
    >>> for row in reader:
    ...     print row
    ... 
    ['source', 'dose (Sv)', 'dose (BED)']
    ['eating a banana', '1.0E-7', '1']
    ['arm x-ray', '1.0e-6', '10']
    ...
    >>> f.close()

This is essentially the same as when we read the CSV file as a raw text file, except a lot of the stripping and splitting has been taken care of for us.

#### Read as Dictionaries

Another popular option is to read each line of the CSV file into a small dictionary of values, with the column headers as keys and the row split into values:

    >>> import csv
    >>> f = open('radiation_dose.csv', 'r')
    >>> dict_reader = csv.DictReader(f)
    >>> for row in dict_reader:
    ...     print row
    ... 
    {'dose (Sv)': '1.0E-7', 'source': 'eating a banana', 'dose (BED)': '1'}
    {'dose (Sv)': '1.0e-6', 'source': 'arm x-ray', 'dose (BED)': '10'}
    {'dose (Sv)': '5.0e-6', 'source': 'dental x-ray', 'dose (BED)': '50'}
    ... 
    >>> f.close()

This is particularly handy if the CSV data will eventually be read into any kind of dictionary. But mostly this is just another way to do things, for convenience sake. Either of these two options in the `csv` library will work fine. Neither is particularly faster or smarter.


## Problem Sets

 * [Advanced Strings](problem_set_1_strings.py)


[Back to Syllabus](../../README.md)
