# Python Standard Libraries, Part 2


## os

#### 1. List the contents of your current directory.

    >>> os.listdir('.')

#### 2. Show the full path of your current directory.

    >>> os.getcwd()

#### 3. Make a directory called `delete_me`.

    >>> os.mkdir('delete_me')

#### 4. Change directories to move inside of `delete_me`.

    >>> os.chdir('delete_me')

#### 5. List the contents of your current directory.

    >>> os.listdir('.')

#### 6. Show the full path of your current directory.

    >>> os.getcwd()

#### 7. Move up one directory.

    >>> os.chdir('../')

#### 8. Remove the `delete_me` directory.

    >>> os.remove('delete_me')


## glob

Create two text files in your current directory: nasa_science.txt and nasa_future.txt.

#### 1. List all the contents of your current directory.

    >>> os.listdir('.')

#### 2. List all of the files in your current directory that start with "nasa" and end with ".txt".

    >>> from glob import glob
    >>> glob('nasa*.txt')
    ['nasa_science.txt', 'nasa_future.txt']

#### 3. Remove all files in your current directory that start with "nasa" and end with ".txt".

    >>> files = glob('nasa*.txt')
    >>> for f in files:
    ...     os.remove(f)
    

## sys

#### 1. Write a module that prints out the number of command line arguments entered after the program name.

    import sys

    def main():
        print(len(sys.argv) - 1)
    
    if __name__ == '__main__':
        main()

#### 2. Write a module that takes a list of numbers from the user and averages them.

    import sys

    def main():
        numbers = argv[1:]
        total = sum(numbers)
        average = total / len(numbers)
        
        print(average)
    
    if __name__ == '__main__':
        main()

## zipfile

Before doing anything else, create three text files in your local directory: 1.txt, 2.txt, and 3.txt.

#### 1. Zip all three of your text files into an archive named "problem_set_2.zip".

    >>> from zipfile import ZipFile, ZIP_DEFLATED
    >>> z = ZipFile("problem_set_2.zip", 'w')
    >>> 
    >>> for f in ['1.txt', '2.txt', '3.txt']:
    ...     z.write(f, f, ZIP_DEFLATED)
    ... 
    >>> z.close()

#### 2. List the contents of "problem_set_2.zip".

    >>> from zipfile import ZipFile
    >>> contents = ZipFile('problem_set_2.zip', 'r')
    >>> print(contents.namelist())
    1.txt
    2.txt
    3.txt

#### 3. Unzip "problem_set_2.zip".

    >>> z2 = ZipFile('problem_set_2.zip')
    >>> for f in z2.namelist():
    ...     z2.extract(f)


## gzip

Before doing anything else, create a text file in your local directory: test.txt.

#### 1. Gzip your text file into an archive named "test.txt.gz".

    >>> import gzip
    >>> t1 = open('test.txt', 'rb')
    >>> gz = gzip.open('test.txt.gz', 'wb')
    >>> gz.writelines(t1)
    >>> gz.close()
    >>> t1.close()

#### 2. Un-gzip your "test.txt.gz" archive.

This is actually a two-step process. First, we read the data from the gzipped file. Then we write a new output file, like we would write any output file in Python.

    >>> f = gzip.open('test.txt.gz', 'rb')
    >>> file_content = f.read()
    >>> f.close()
    >>> 
    >>> f_new = open('new_test.txt', 'wb')
    >>> f_new.write(file_content)
    >>> f_new.close()



[Back to Problem Set](problem_set_2_batteries.md)
