# Package Management VirtualEnv

VirtualEnv is the most pervasive [package management system](https://en.wikipedia.org/wiki/Package_manager) for Python. If you install *any* third-party apps or ever work on more than one Python project, and you don't use a package management system, you will end up in [dependency hell](https://en.wikipedia.org/wiki/Dependency_hell):

![Dependency Hell](https://imgs.xkcd.com/comics/python_environment.png)


## Installation

As usual, you are on your own for installing VirtualEnv. If you installed Anaconda, it came with that. If you are on a Linux machine, you can probably do something like:

    sudo pip install virtualenv

or:

    sudo easy_install virtualenv

On a Mac you can do something like:

    homebrew install virtualenv

For this lecture, I am just going to assume you're not on a Windows machine.  If you are, I am not sure how to help you.


## Example 1 - A Data Scientist's Env

Let's say a data scientist is sharing code with you. You use Python 3.7 and she's still using 3.6. She uses a new version of NumPy, but an older version of Pandas. You do the opposite. You want to use her code, but you don't want to wreck your whole system to do it.

Enter VirtualEnv.

First, let's make a directory to drop her code into:

    mkdir data_work
    cd data_work

Now let's create a VirtualEnv to mimic her environment:

    virtualenv --python=python3.6 data_env

Now we can start using that environment:

    source data_env/bin/activate

After that, you will see your commandline will helpfully remind you that you're in an env by listing the name of the env before your command prompt:

    (data_env) $
    (data_env) $ ls whatever

Okay, now through this text into a file called `requirements.txt`:

    pandas == 0.20.0
    numpy == 1.16.2
    matplotlib >= 2.0.0

Now run this `pip` command (this is a standard way to install third-party libraries in Python and is not specific to VirtualEnv):

    pip install -r requirements.txt

Okay! Now we have a Virtual Environment with all our packages installed, and we can use it:

    (data_env) $ python
    >>> import numpy
    >>> numpy.__version__
    '1.16.2'
    >>> import matplotlib
    >>> matplotlib.__version__
    '2.1.2'

And when your done using your friends code you can leave that all behind with by just typing `deactivate` from the command line:

    (data_env) $ deactivate


## Example 2 - A Web Developer's Env

Okay, for our second example say you are looking at the code for a little web app a colleague is making. For some reason, she uses Python 2.7, not the 3.6 your data scientist uses or even the 3.7 you use. And she uses an older version of NumPy , and installs Django (for making websites). Again, you don't want to wreck your own code, and now you don't want to wreck your data scientist area either.

VirtualEnv to the rescue!

First, let's make a directory to drop her code into:

    mkdir web_work
    cd web_work

Now let's create a VirtualEnv to mimic her environment:

    virtualenv --python=python3.6 web_env

Now we can start using that environment:

    source web_env/bin/activate

Okay, now through this text into a file called `requirements.txt`:

    django==1.11.20
    numpy == 1.15.0

Now run this `pip` command (this is a standard way to install third-party libraries in Python and is not specific to VirtualEnv):

    pip install -r requirements.txt

Okay! Now we have a Virtual Environment with all our packages installed, and we can use it:

    (web_env) $ python
    >>> import numpy
    >>> numpy.__version__
    '1.15.0'
    >>> import django
    >>> django.__version__
    '1.11.20'

Again, when you want to go back to your own code, you can just type `deactivate` from the command line:

    (web_env) $ deactivate


## Clean Up

Cleaning up a VirtualEnv is actually really easy. We've already seen that all you need to do to stop using a VirtualEnv is `deactivate`. Well, if you are done with a VirtualEnv forever, all you have to do is delete the folder you created for the env.

In Mac / Linux:

    rm -rf data_env/
    rm -rf web_env/

Or in Windows, just right-click the folder and delete it.

Ditching a VirtualEnv that easy!


## Further Reading

* [A Practical Primer](https://web.archive.org/web/20160404222648/https://iamzed.com/2009/05/07/a-primer-on-virtualenv/)
* [Python-Guide.org Tutorial](https://docs.python-guide.org/dev/virtualenvs/)
* [Gentle VirtualEnv Intro](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [VirtualEnv Documentation](https://virtualenv.pypa.io/en/stable/)
* [iTek blog Tutorial](https://itekblog.com/virtualenv-tutorial/)

[Back to Syllabus](../../README.md)
