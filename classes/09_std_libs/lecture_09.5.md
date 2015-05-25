# Batteries Included, Part 2

## os

The `os` library will help you work with the file system on your computer. For instance, if I wanted to create a directories for this class, I could use `mkdir`:

    >>> os.mkdir('python_class')

Or I could make directories inside directories:

    >>> os.makedirs('python_class/class11_batteries_included_2/learning_os/')

And I could "change directories" and move inside what I just created:

    >>> os.chdir('python_class/class11_batteries_included_2/')

And list the contents inside that directory:

    >>> os.listdir('.')
    ['learning_os']

Or I could list the contents in one directory up from where I am:

    >>> os.listdir('../')
    ['class11_batteries_included_2']

And I could go into one more directory and list the contents:

    >>> os.chdir('learning_os/')
    >>> os.listdir('.')
    []

But what if I need to know my current location in the directory tree?

    >>> os.getcwd()
    '/home/thejollysin/python_class/class11_batteries_included_2/learning_os'

Say I want to delete that `learning_os` directory, I would back out using `chdir` and do a `remove`:

    >>> os.chdir('../')
    >>> os.remove('learning_os')

Same thing for the `class11_batteries_included_2` directory and the Python class directory:

    >>> os.chdir('../')
    >>> os.remove('class11_batteries_included_2')
    >>> os.chdir('../')
    >>> os.remove('python_class')

If you are familiar with basic computer admin, you will also find other useful tools in the `os` package. You can get and set environment variables (`getenv` & `putenv`), you can create and remove softlinks between files and folder (`link` & `unlink`), and a lot more.

#### os.path

The `os.path` module helps you handle pathnames in Windows, Linux, and Mac. For instance, what if we tried to `remove` a directory (or file) that doesn't exist?

    >>> os.remove('python_class')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    OSError: [Errno 2] No such file or directory: 'python_class'

Well, it would be nice to first test of the directory (or file) exists before trying to `remove` is:

    >>> if os.path.exists('python_class'):
    ...     os.remove('python_class')

Actually, we might want to do that a lot. So let's make a function to do that for us:

    >>> def safe_remove(full_path):
    ...     '''remove a directory/file,
    ...     if it already exists, do nothing'''
    ...     if os.path.exists(full_path):
    ...         os.remove(full_path)

It sometimes happens that you have the full path to a file and you want to break it into the file name and its directory:

    >>> file_path = '/home/username/python_class/class11_batteries/lecture.txt'
    >>> os.path.basename(file_path)
    'lecture.txt'
    >>> os.path.dirname(file_path)
    '/home/username/python_class/class11_batteries'

## glob

The `glob` module allows you to find all of the files (or directories) matching a certain filename regex, like: `*.jpg`, or `data_*.csv`. It is frequently helpful to have along with the `os` module above. Let's find all of the log files in a log directory:

    >>> from glob import glob
    >>> glob('/path/to/log_dir/*.log')
    ['/path/to/log_dir/something_crazy.log', '/path/to/log_dir/something_else.log']

Or you can just look for all `jpg` files in the current directory by doing:

    >>> from glob import glob
    >>> glob('*.jpg')
    ['kakapo.jpg', 'blue_whale.jpg', 'dodo.jpg', 'black_rhino.jpg']

## sys

The `sys` library has a lot of great stuff in it, but what we are going to focus on is the ability to pass variables to your Python programs. Let's make a really simple example, where all you want your program to do is print squares from 1 to `n`:

    def main():
        '''simple test main function'''
        n = 5
        print_squares(n)
        
    
    def print_squares(n):
        '''print the squares of the numbers
        from 1 to n'''
        for i in range(1, n + 1):
            print(i * i)


    if __name__ == '__main__':
        main()

We will call the above module `print_squares.py`. And it works. We can run it by doing `python print_squares.py`, and it will print the numbers from 1 to 25. But if we want to change `n` to be 100, we have to go in and change the hard-coded number `n`. Not only does this take time, it means the script really isn't independent of the value of `n` you want to run right now. It would be nice if we could make the script a bit more general. Well, that's what the `sys` library is for.

What we want is to have the script be run like:

    python print_squares.py 7

And that will print the squares from 1 to 49.

This is pretty easy to do. It turns out that `sys.argv` is a list of all the command line arguments used to run a Python program. The modified program would look like this:

    import sys

    def main():
        '''simple test main function'''
        n = int(sys.argv[1])
        print_squares(n)
        
    
    def print_squares(n):
        '''print the squares of the numbers
        from 1 to n'''
        for i in range(1, n + 1):
            print(i * i)


    if __name__ == '__main__':
        main()

That's all, we just change two lines, and now our program can take values from the command line. Easy. But let's learn more about `sys.argv` by writing a short module:

    import sys
    
    def main():
        print('sys.argv:')
        print(sys.argv)
        print('length sys.argv')
        print('len(sys.argv))
        print('One at a time:')
        
        for key, value in enumerate(sys.argv):
            print(key, value)
    
    
    if __name__ == '__main__':
        main()

If we save the short module above to a file called `test_sys_argv.py`, we can run it to learn more about how `sys.argv` works:

    >>> python test_sys_argv.py
    sys.argv:
    ['test_sys_argv.py']
    length sys.argv:
    1
    One at a time:
    (0, 'test_sys_argv.py')

Here we see that `sys.argv` includes the NAME of the Python program in the command line arguments, but it doesn't include the word `python`. Let's try adding a couple command line arguments:


    >>> python test_sys_argv.py 124 Kakapo 1984
    sys.argv:
    ['test_sys_argv.py', '124', 'Kakapo', '1984']
    length sys.argv:
    4
    One at a time:
    (0, 'test_sys_argv.py')
    (1, '124')
    (2, 'Kakapo')
    (3, '1984')

Here we see a more interesting case with several command line arguments. Now we can see that command line arguments are space-separated. But it is important to notice that both `124` and `1984` were both parsed as *strings*, not numbers. That's why in `print_squares.py` we had to put an `int()` around the `sys.argv[1]`, in order to convert the number from the command line string.

## zipfile

Sometimes we will want to read or write zip files from a Python script. A zip file is a single compressed file that can include one or more regular files. Zipping a file is done to save hard drive space and speed up file transfer.

#### Listing Contents

First, let's see how to list the regular files inside a zip file:

    >>> from zipfile import ZipFile
    >>> contents = ZipFile("path/to/example.zip", "r")
    >>> for name in contents.namelist():
    ...     print(name)
    ...
    file1.jpg
    file2.csv
    file3.txt

#### Reading a Zip File

Frequently, we will want to read the data from a zipfile. For this example, let's imagine our zip file only includes one other file, a CSV:

    >>> from zipfile import ZipFile
    >>> contents = ZipFile("path/to/example.zip", "r")
    >>> print(contents.namelist())
    [file1.csv]
    >>> file1 = contents.namelist()[0]
    >>> data = contents.read(file1)

#### Zipping Files

Finally, let's zip all the files in a directory. This will use examples of `os` and `glob` that we saw above:

    >>> from glob import glob
    >>> import os
    >>> from zipfile import ZipFile, ZIP_DEFLATED
    >>> 
    >>> file = ZipFile("test.zip", "w")
    >>> 
    >>> for name in glob("inputs/*"):
    >>>     file.write(name, os.path.basename(name), ZIP_DEFLATED)
    ...
    >>> file.close()

## gzip

The `*.zip` files we saw above are great, but if you are on a Linux or Mac computer you'll probably see `*.gz` files more often. The idea is the same, these are just two different ways to compress files. In general, `.zip` is more widely supported, but `.gz` has better compression.

Since this is going to be a bit like `zipfile` above, we'll be brief.

#### Reading a Compressed File

If we wanted to read a single compressed GZIP file:

    >>> import gzip
    >>> f = gzip.open('your_text_file.txt.gz', 'rb')
    >>> file_content = f.read()
    >>> f.close()

#### Create a GZIP

If we wanted to write our own data to a GZIP, all we need to do is convert that content to a string and do:

    >>> import gzip
    >>> content = 'Your content here.'
    >>> f = gzip.open('your_text_file.txt.gz', 'wb')
    >>> f.write(content)
    >>> f.close()

#### GZIP Existing Files

If the file already exists, and we just want GZIP it:

    >>> import gzip
    >>> fin = open('your_file.txt', 'rb')
    >>> fout = gzip.open('your_file.txt.gz', 'wb')
    >>> fout.writelines(fin)
    >>> fout.close()
    >>> fin.close()


## Problem Sets

 * [Standard Libraries, Part 2 - Problem Set](problem_set_2_batteries.md)

## Further Reading

 * Official Docs - os: ([Python 2](https://docs.python.org/2/library/os.html) / [Python 3](https://docs.python.org/3/library/os.html))
 * [effbot - os](http://www.effbot.org/librarybook/os.htm)
 * Official Docs - os.path: ([Python 2](https://docs.python.org/2/library/os.path.html#module-os.path) / [Python 3](https://docs.python.org/3/library/os.path.html#module-os.path))
 * [effbot - os.path](http://www.effbot.org/librarybook/os-path.htm)
 * Official Docs - sys: ([Python 2](https://docs.python.org/2/library/sys.html) / [Python 3](https://docs.python.org/3/library/sys.html))
 * [effbot - sys](http://www.effbot.org/librarybook/sys.htm)
 * Official Docs - glob: ([Python 2](https://docs.python.org/2/library/glob.html) / [Python 3](https://docs.python.org/3/library/glob.html))
 * [Module of the Week - glob](http://pymotw.com/2/glob/)
 * [Every Day Scripting - glob](https://everydayscripting.wordpress.com/2008/12/24/pythons-glob-module-is-really-cool/)
 * Official Docs - zipfile: ([Python 2](https://docs.python.org/2/library/zipfile.html) / [Python 3](https://docs.python.org/3/library/zipfile.html))
 * [effbot - zipfile](http://effbot.org/librarybook/zipfile.htm)
 * Official Docs - gzip: ([Python 2](https://docs.python.org/2/library/gzip.html) / [Python 3](https://docs.python.org/3/library/gzip.html))

[Back to Syllabus](../../README.md)
