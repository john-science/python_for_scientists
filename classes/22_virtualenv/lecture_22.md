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

Okay, now through this text into a file called `requirements.txt`:

    pandas == 0.20.0
    numpy == 1.16.2
    matplotlib >= 3.0.0

Now run this `pip` command (this is a standard way to install third-party libraries in Python and is not specific to VirtualEnv):

    pip install -r requirements.txt

Okay! Now we have a Virtual Environment with all our packages installed, and we can use it:

    $ python

> TODO: Continue

## Example 2 - A Web Developer's Env

> TODO: python2.7

    dango==1.11.20
    numpy==1.15.0

## Clean Up

> TODO


## Further Reading

* [A Practical Primer](https://web.archive.org/web/20160404222648/https://iamzed.com/2009/05/07/a-primer-on-virtualenv/)
* [Python-Guide.org Tutorial](https://docs.python-guide.org/dev/virtualenvs/)
* [Gentle VirtualEnv Intro](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [VirtualEnv Documentation](https://virtualenv.pypa.io/en/stable/)
* [iTek blog Tutorial](https://itekblog.com/virtualenv-tutorial/)

[Back to Syllabus](../../README.md)
