# A Complete Example

So far we have seen how to create classes, but not necessarily why they are useful. What follows is an example of a simple Python script that would be more useful if it was written using OOP.

## A Simple FTP Script

What follows is a simple script to download a set number of files from an [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) server. This example will be carried out using the python standard library `ftplib`. If you are interested, there is a great introduction to `ftplib` [here](http://effbot.org/librarybook/ftplib.htm), and the official documentation is [here](https://docs.python.org/2/library/ftplib.html).

But for now, it is sufficient to understand that we are downloading some files from an external computer using a script called `simpleftp.py`. This is a prety simple script, so it is powerful but somewhat limited.

Here is the standard implementation, using functions and a main method:

    import ftplib
    
    # CONNECTION INFORMATION
    FTP_ADDRESS = '127.0.0.1'  # There's no place like home.
    FTP_USER = 'myusername'
    FTP_PASS = 'myF@nc3P@$$1!'
    FTP_IS_PASSIVE = False
    
    # FILE INFORMATION
    FILES = ['uranium238.csv', 'uranium239.csv']
    FTP_DIR = 'download'
    
    
    def main():
        try:
            ftp = ftplib.FTP(FTP_ADDRESS, FTP_USER, FTP_PASS)
            ftp.set_pasv(FTP_IS_PASSIVE)
            cd(ftp, FTP_DIR)
            for fi in FILES:
                f = open(fi, 'wb')
                ftp.retrbinary('RETR ' + fi, f.write)
                f.close()
            ftp.quit()
        except Exception as e:
            print('FTP Failed with:' + str(e))
    
    def cd(ftp, d):
        """Change Directories - create if it doesn't exist"""
        if directory_exists(ftp, d) is False:
            ftp.mkd(d)
        ftp.cwd(d)
    
    def directory_exists(ftp, d):
        '''Determine if the FTP directory exists'''
        file_list = []
        ftp.retrlines('LIST', file_list.append)
        for f in file_list:
            if f.split()[-1] == d and f.upper().startswith('D'):
                return True
        return False
    
    
    if __name__ == "__main__":
        main()

## The OOP Version

And here is the script re-written using OPP:

    import ftplib
    
    # CONNECTION INFORMATION
    FTP_ADDRESS = '127.0.0.1'
    FTP_USER = 'myusername'
    FTP_PASS = 'myF@nc3P@$$1!'
    FTP_IS_PASSIVE = False
    
    # FILE INFORMATION
    FILES = ['uranium238.csv', 'uranium239.csv']
    FTP_DIR = 'download'
    
    
    def main():
        ftp = SimpleFTP(FTP_ADDRESS, FTP_USER, FTP_PASS, FTP_IS_PASSIVE)
        ftp.pull_data(FILES, FTP_DIR)
        
    
    class SimpleFTP(object):
    
        def __init__(self, address, user, pass, passive):
            self.address = address
            self.directory = dir
            self.username = user
            self.password = pass
            self.passive = passive
            self.ftp = None  # Ensure this variable is global
        
        
        def pull_data(self, files, dir):
            '''Download the data you want,
            by listing files you want, and the directory they are in
            '''
            try:
                self.ftp = ftplib.FTP(self.address, self.username, self.password)
                self.ftp.set_pasv(self.passive)
                self.cd(ftp, dir)
                for fi in files:
                    f = open(fi, 'wb')
                    self.ftp.retrbinary('RETR ' + fi, f.write)
                    f.close()
                self.ftp.quit()
            except Exception as e:
                print('FTP Failed with:' + str(e))
    
        def cd(self, dir):
            """Change Directories - create if it doesn't exist"""
            if self.directory_exists(dir) is False:
                ftp.mkd(dir)
            ftp.cwd(dir)
    
        def directory_exists(self, d):
            '''Determine if the FTP directory exists'''
            file_list = []
            self.ftp.retrlines('LIST', file_list.append)
            for f in file_list:
                if f.split()[-1] == d and f.upper().startswith('D'):
                    return True
            return False
    
    
    if __name__ == "__main__":
        main()

## The "Why Bother?"

### Flexibility of Usage

On first glance you may think "The second code isn't any shorter, why bother?" It is true, in this case, the second version of the code isn't shorter or much simpler than the first. But it is a lot more flexible. For instance, imagine you want to download files from multiple directories. Before you would have had to modify the script inputs (files and directory) by hand, and run the script each time. But what if there were files you wanted to download from hundreds of directories? That would be tedious to do by hand, and would not really take advantage of your computer for automation.

But with the new OOP version of the code, you can simply define all your files and directories as variables, and use `pull_data` in succession:

    ftp = SimpleFTP(FTP_ADDRESS, FTP_USER, FTP_PASS, FTP_IS_PASSIVE)
    ftp.pull_data(FILES, FTP_DIR)
    ftp.pull_data(FILES_2, FTP_DIR_2)
    ftp.pull_data(FILES_3, FTP_DIR_3)
    ftp.pull_data(FILES_4, FTP_DIR_4)
    ftp.pull_data(FILES_5, FTP_DIR_5)

Or, if you put all of your `FILES` into a `MASTER_FILES` list-of-lists, and all of y our `FTP_DIR` into a `MASTER_DIRS` list-of-lists:

    ftp = SimpleFTP(FTP_ADDRESS, FTP_USER, FTP_PASS, FTP_IS_PASSIVE)
    for i in range(len(MASTER_FILES)):
        ftp.pull_data(MASTER_FILES[i], MASTER_DIRS[i])

### Flexibility for Importing

Also, the OOP version is easier to import into a different script:

    from simpleftp import SimpleFTP
    
    def main():
        # ftp server info
        add = '127.0.0.1'
        user = 'myusername'
        pass = 'myF@nc3P@$$1!'
        passive = False
    
        # FILE INFORMATION
        files = ['uranium238.csv', 'uranium239.csv']
        dir = 'download'
        
        # ftp data
        ftp = SimpleFTP(add, user, pass, passive)
        ftp.pull_data(fire_data, fir_dir)
        
        # process new fire files with local scripts
        process_fire_data(fire_data)
        
    
    def process_fire_data(fire_files):
        '''Assume some amazing science is done here'''
        pass
    
    if __name__ == "__main__":
        main()

Now we can reuse the SimpleFTP class in all our various work. Using the original, imperative version would be much messier:

    >>> from ftp_download import main as simpleftp
    >>> FTP_ADDRESS = '127.0.0.1'
    >>> FTP_DIR = 'download'
    >>> FTP_USER = 'myusername'
    >>> FTP_PASS = 'myF@nc3P@$$1!'
    >>> FTP_IS_PASSIVE = False
    >>> 
    >>> FTP_DIR = 'download'
    >>> FILES = ['fire_locations.csv', 'fire_events.csv']
    >>> 
    >>> 
    >>> simpleftp()

The first thing to notice is that in order to import and use the non-OOP version of the script you HAD to name a bunch of variables as in the original script ("FTP_DIR" and so forth). But why should you spend your time memorizing or looking up what names other people used for their variables? You don't have time for that.


[Back to Lecture](lecture_06.md)
