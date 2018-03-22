# MongoDB

MongoDB is what is known as a "NoSQL" database. Where most databases are based around inter-related tables, Mongo allows you to store data in practically any format. This leads to much more natural data representations. It also means your whole workflow will be very different from our a typical SQL-like database. There are advantages and disadvantages to this, but Mongo is easier to get use than most database systems, and scales well.

This lecture will target Mongo v3.6 and we will cover both the native Mongo shell syntax and the Python MongoDB API.


## Installation

For installation instructions for the MongoDB database server and client look [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/).

To install the Python MongoDB Driver, try using [Anaconda](http://docs.continuum.io/anaconda/install.html). Anaconda is Python packaged with hundreds of tools and libraries, and it is a great learning tool. The Mongo Driver we will use is:

    conda install pymongo


## Creating and Connecting to Databases

To connect to the MongoDB shell from the commandline, witout specifiying a DB, do:

    $ mongo -nodb
    >

From there, you can connect to a MongoDB server by:

    > conn = new Mongo("some-host:30000")

And then you can connect to a specific database by:

    > db = conn.getDB("myDB")

Or you can combine both of these into:

    > db = new Mongo("some-host:30000/myDB")

Alternatively, you can specific the database directly from the commandline, and it will define the `db` variable for you:

    $ mongo some-host:30000/myDB
    > 

What we saw above is that MongoDB comes with its own interactive shell, much like MySQL or postgres. However, in the case of Mongo, the interactive shell is in JavaScript. You can define normal JavaScript objects, functions, and variables exactly as you would expect here.  (Obviously, teaching JavaScript is outside the scope of this course. Though there are an endless number of great resources for it online.)


## Interacting with the Database

Above we connected to a MongoDB using the native Mongo shell (in JavaScript). That's great, and we need to understand how to do things in the native Mongo shell, but we're here to learn to do thing in Python.  So going forward each time we learn to do something in Mongo we will first see it in the native JavaScript and then we will see how to do it in Python.

First, let's look at the above "connecting to a database" example:

    $ python
    > import pymongo
    >

> TODO


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

 * [Mongo DB home page](https://www.mongodb.com/)
 * [The O'Reily MongoDB book](https://www.goodreads.com/book/show/17943788-mongodb)

[Back to Syllabus](../../README.md)


![XKCD Query Comic](https://imgs.xkcd.com/comics/query.png)
