# MongoDB

MongoDB is what is known as a "NoSQL" database. Where most databases are based around inter-related tables, Mongo allows you to store data in practically any format. This leads to much more natural data representations. It also means your whole workflow will be very different from our a typical SQL-like database. There are advantages and disadvantages to this, but Mongo is easier to get use than most database systems, and scales well.

This lecture will target Mongo v3.6 and we will cover both the native Mongo shell syntax and the Python MongoDB API.


## Installation

For installation instructions for the MongoDB database server and client look [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/). You will have to install Mongod/Mongo before you can install the Python driver for Mongo.

To install the Python MongoDB Driver, try using [Anaconda](http://docs.continuum.io/anaconda/install.html). Anaconda is Python packaged with hundreds of tools and libraries, and it is a great learning tool. The Mongo Driver we will use is:

    conda install pymongo


## Starting the MongoDB Daemon

Before you can connect to a Mongo database, you need a Mongo daemon (or service). That daemon needs to be run on some server/port configuration. In the wild, you may build a web app with a shared MongoDB server on your local network, and you may have multiple ports running for different uses. But for our purposes it will suffice to use the default localhost on port 27017.

On my computer, to start the Mongo demon the first time, I had to do:

    $ sudo mkdir /data/db
    $ sudo chmod 755 /data -R
    $ sudo mongod --repair
    $ sudo mongod


## Creating and Connecting to Databases

To connect to the MongoDB shell from the commandline, witout specifiying a DB, do:

    $ mongo -nodb
    >

From there, you can connect to a MongoDB server by:

    > conn = new Mongo("127.0.0.1:27017")

And then you can connect to a specific database by:

    > db = conn.getDB("secret_agents")

Or you can combine both of these into:

    > db = new Mongo("127.0.0.1:27017/secret_agents")

Alternatively, you can specific the database directly from the commandline, and it will define the `db` variable for you:

    $ mongo 127.0.0.1:27017/secret_agents
    > 

What we saw above is that MongoDB comes with its own interactive shell, much like MySQL or postgres. However, in the case of Mongo, the interactive shell is in JavaScript. You can define normal JavaScript objects, functions, and variables exactly as you would expect here.  (Obviously, teaching JavaScript is outside the scope of this course. Though there are an endless number of great resources for it online.)


## Using the Python Driver

Above we connected to a MongoDB using the native Mongo shell (in JavaScript). That's great, and we need to understand how to do things in the native Mongo shell, but we're also here to learn to do things in Python.  So going forward each time we learn to do something in Mongo we will first see it in the native JavaScript and then we will see how to do it using the Python `PyMongo` Driver.

First, let's look at the above "connecting to a database" example. Hopefully the installation is complete and we can import the driver library:

    $ python
    > import pymongo

Again, we want to be able to connect to a MongoDB daemon:

    > from pymongo import MongoClient
    > client = MongoClient('localhost', 27017)

And again, we will want to connect to a specific database through that daemon:

    > db = client.secret_agents

So far, so good. We can now connect to Mongo daemons and databases using the native Mongo shell and the `PyMongo` Python driver.  In either case, if the `secret_agents` database didn't exist, it would be created on the fly.


## Databases, Collections, and Documents

> TODO: Let's talk about some Mongo lingo.


## Creating, Updating, and Deleting Documents

TODO

## Querying

TODO

## Indexing

TODO

## Special Indexes

TODO

## Aggregation

TODO

## Application Design

TODO

## Replication

TODO

## Sharding

TODO

## Server Admin

TODO


## Further Reading

 * [Mongo DB home page](https://www.mongodb.com/) - Official website
 * [The O'Reily MongoDB book](https://www.goodreads.com/book/show/17943788-mongodb) - What I used
 * [Official PyMongo tutorial](http://api.mongodb.com/python/current/tutorial.html) - Seems good

[Back to Syllabus](../../README.md)


![XKCD Query Comic](https://imgs.xkcd.com/comics/query.png)
