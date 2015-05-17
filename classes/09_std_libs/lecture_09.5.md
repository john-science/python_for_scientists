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

## sys

 * Coming Soon

## gzip

 * Coming Soon

## cPickle

 * Coming Soon

## Problem Sets

 * Coming Soon

## Further Reading

 * Official Docs - os: ([Python 2](https://docs.python.org/2/library/os.html) / [Python 3](https://docs.python.org/3/library/os.html))
 * [effbot - os](http://www.effbot.org/librarybook/os.htm)
 * Official Docs - os.path: ([Python 2](https://docs.python.org/2/library/os.path.html#module-os.path) / [Python 3](https://docs.python.org/3/library/os.path.html#module-os.path))
 * [effbot - os.path](http://www.effbot.org/librarybook/os-path.htm)
 * Official Docs - sys: ([Python 2](https://docs.python.org/2/library/sys.html) / [Python 3](https://docs.python.org/3/library/sys.html))
 * [effbot - sys](http://www.effbot.org/librarybook/sys.htm)
 * Official Docs - gzip: ([Python 2](https://docs.python.org/2/library/gzip.html) / [Python 3](https://docs.python.org/3/library/gzip.html))
 * Official Docs - cPickle: ([Python 2](https://docs.python.org/2/library/pickle.html#module-cPickle) / [Python 3](https://docs.python.org/2/library/pickle.html#module-cPickle))

[Back to Syllabus](../../README.md)
