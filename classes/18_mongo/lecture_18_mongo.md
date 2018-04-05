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
    >>> import pymongo

Again, we want to be able to connect to a MongoDB daemon:

    >>> from pymongo import MongoClient
    >>> client = MongoClient('localhost', 27017)

And again, we will want to connect to a specific database through that daemon:

    >>> db = client.secret_agents

So far, so good. We can now connect to Mongo daemons and databases using the native Mongo shell and the `PyMongo` Python driver.  In either case, if the `secret_agents` database didn't exist, it would be created on the fly.


## Databases, Collections, and Documents

In SQL-based databases, all data is stored in tables and tables are stored in schemas.  But in a Mongo Database, data is stored in `Documents` and Documents are stored in `Collections`.

Whereas a classic SQL "table" is limited to rows and columns of data, a Mongo "Document" is far less structured:

    {"name": "James Bond",
     "code name" : "007",
     "status": "Active",
     "licenses": ["License to Kill", "License to Tango"]}

The Mongo DB document stores data as key/value pairs, and the values can be another document. Documents are designed to look like JSON objects, which means they can be well represented by Python dictionaries or JavaScript objects.

Unlike SQL schemas, the documents in a Mongo collection do not have to be related in any particular way. There are no restrictions on sharing keys, IDs, or relationships of any kind. While this lack of structure probably makes certain SQL-like operations slower, it provides a lot of freedom. Your data can now be represented in much more natural ways. And you can change the structure of a document without having to worry about changing the structure of all the other documents in that collection.

A Mongo document is a different beast than a SQL table, but since it is based on JSON you probably already have a good intuitive understanding of it.

## Note on ObjectIDs

Throught this lecture you will see that every document in a MongoDB has a unique "ObjectID":

    {"_id": ObjectID(5ab3d8c5836cb47f66966e35)}

I will abbreviate these with shorter versions, for no other reason than it makes them easier to read on GitHub:

    {"_id": ObjectID(...e35)}

## Inserting, Removing, and Updating Documents

### Creating Documents and Collections

To create a collection, simply add a document to it, and if it doesn't exist it will be created.

shell:

    > db.agents.insert({"name": "James Bond"})
    
pymongo:

    >>> db.agents.insert({"name": "James Bond"})

You may also want to get a document from a collection.

shell:

    > db.agents.findOne()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }

pymongo:

    >>> db.agents.find_one()
    {'_id': ObjectId('...e35'), 'name': 'James Bond'}

It will frequently be handy to add multiple documents to a collection at the same time (and it will certainly be faster).

shell:

    > db.agents.insert([{"name": "Scarlet Papava"}, {"name": "Alec Trevelyan"}])

pymongo:

    >>> db.agents.insert_many([{"name": "Scarlet Papava"}, {"name": "Alec Trevelyan"}])

You may frequently want to return all the documents in a collection.  Via the shell this works exactly as expected, in PyMongo (Python v3.x) you will get an iterator instead of a simple list.

shell:

    > db.agents.find()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

pymongo:

    >>> for doc in db.agents.find():
    ...     print(doc)
    ... 
    {'_id': ObjectId('...e35'), 'name': 'James Bond'}
    {'_id': ObjectId('...6dc'), 'name': 'Scarlet Papava'}
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }


### Removing Documents and Collections

An entire collection can be deleted by using the `remove()` or `drop()` methods. The difference is that `drop()` can only drop whole collections at a time, and `remove()` can also be used to remove individual documents. It should be noted that `drop()` truly deletes a collection, but `remove()` will simply unhook it and the data will be saved for a while. Because of this `drop()` is much faster.

shell:

    > db.agents.drop()
    > db.agents.remove()

pymongo:

    >>> db.agents.drop()
    >>> db.agents.remove({})

If, instead, you delete a set of documents from a collection, all of those documents are irreversibly lost.  You do that by passing a query to the `remove()` method.

shell:

    > db.agents.remove({"name": "James Bond"})

pymongo:

    >>> db.agents.remove({"name": "James Bond"})


### Updating Documents

Updating documents is a big topic, so let us break it down into parts.

#### Update

To update an existing document, we use the `update()` method, which replaces a queried object (or set of objects) with a new one. Usually, we want to do some data mangling of the object before placing it in the database. That data mangling can be pretty much anything, and is restricted only by the limitations of the language/shell you are working in.

shell:

    > agent1 = db.agents.findOne()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }
    > agent1.code_name = "007";
    > agent1.home_address = "221 B Baker Street, London"
    > delete agent1.home_address
    > agent1
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007"
    }
    > db.agents.update({"name": "James Bond"}, agent1)

Or if we are only querying for a single document it might be easier to do the `update()` based on `_id`:

    > db.agents.update({"_id": ObjectId("...e35")}, agent1)

pymongo:

    >>> agent1 = db.agents.find_one()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }
    >>> agent1["code_name"] = "007";
    >>> agent1.["home_address"] = "221 B Baker Street, London"
    >>> delete agent1.home_address
    >>> agent1
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007"
    }
    >>> db.agents.update({"name": "James Bond"}, agent1)

Or, again, since we know that each `_id` is unique we can play it safe by updating using that:

    >>> from bson.objectid import ObjectId
    >>> db.agents.update({"_id": ObjectId("...e35")}, agent1)

#### Modifiers

You might have noticed above that when we did `update`, `remove`, or `find` we have only been able to query for documents that exactly match a very small set of parameters. But that's no good, right? What if we want to match documents with a more complicated set of conditions? What if we want to pull all agents older than 50? What if we want to retrieve all agents whose last name starts with "B"?  What if we want to add one to an agents age, because she just had her birthday?  This is where query modifiers come in.

`$set` sets the value of a field. If that field does not exist, it is created.

shell:

    > db.agents.find({"name": "Scarlet Papava"})
    { "_id" : ObjectId("...6dc"), "code_name" : "004", "name" : "Scarlet Papava" }
    > db.agents.update({"name": "Scarlet Papava"}, {"$set": {"number_of_kills": 1}})
    > db.agents.find({"name": "Scarlet Papava"})
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava", "number_of_kills" : 1, ... }
    
pymongo:

    >>> db.agents.update({"name": "Scarlet Papava"}, {"$set": {"number_of_kills": 1}})

`$inc` is used to "increment" an integer by one.

shell:

    > db.agents.update({"name": "Scarlet Papava"}, {"$inc": {"number_of_kills": 1}})
    > db.agents.find({"name": "Scarlet Papava"})
    { "_id" : ObjectId("...6dc"),"name" : "Scarlet Papava", "number_of_kills" : 2, ... }
    
pymongo:

    >>> db.agents.update({"name": "Scarlet Papava"}, {"$inc": {"number_of_kills": 1}})

`$unset` removes a field from a document, and does not throw an error if the field does not yet exist.

shell:

    > db.agents.update({"name": "Scarlet Papava"}, {"$unset": {"number_of_kills": 1}})

pymongo:

    >>> db.agents.update({"name": "Scarlet Papava"}, {"$unset": {"number_of_kills": 1}})


#### Array Modifiers

Mongo has an extensive collection of modifiers specific to arrays. Arrays are ordered, indexed collections of arbitary data. Think of them like linked lists, where you can "push" and "pull" the last element of the list.

`$push` adds one element to the end of an array.

shell:

    > db.agents.update({"name": "James Bond"}, {"$set": {"languages": ["English"]}})
    > db.agents.findOne({"name": "James Bond"})
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007",
        "languages" : [ "English" ]
    }
    > db.agents.update({"name": "James Bond"}, {"$push": {"languages": "Russian"}})
    > db.agents.findOne({"name": "James Bond"})
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007",
        "languages" : [ "English", "Russian" ]
    }


pymongo:

    >>> db.agents.update({"name": "James Bond"}, {"$set": {"languages": ["English"]}})
    >>> db.agents.update({"name": "James Bond"}, {"$push": {"languages": "Russian"}})


`$each` allows you to push multiple elements to the end of an array.

shell:

    > db.agents.update({"name": "James Bond"},
          {"$push": {"languages": {"$each": ["Spanish", "Mandarin"]}}})
    > db.agents.findOne({"name": "James Bond"})
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007",
        "languages" : [ "English", "Russian", "Spanish", "Mandarin" ]
    }


pymongo:

    >>> db.agents.update({"name": "James Bond"},
            {"$push": {"languages": {"$each": ["Spanish", "Mandarin"]}}})


`$slice` lets you ensure as you push elements onto an array that the array doens't grow past a certain size.

shell:

    > db.agents.update({"name": "James Bond"},
          {"$push": {"languages": {"$each": ["Urdu", "Arabic"], "$slice": -4}}})
    > db.agents.findOne({"name": "James Bond"})
    {
        "_id" : ObjectId("...e35"),
        "name" : "James Bond",
        "code_name" : "007",
        "languages" : [ "Spanish", "Mandarin", "Urdu", "Arabic" ]
    }

pymongo:

    >>> db.agents.update({"name": "James Bond"},
            {"$push": {"languages": {"$each": ["Urdu", "Arabic"], "$slice": -4}}})


`$sort` sorts the results of `find()` operation on an array.

shell:

    > db.agents.findOne({"name": "James Bond"}).languages.sort()

pymongo:

    >>> sorted(db.agents.find_one({"name": "James Bond"})["languages"])
    

You can use arrays as sets as long as you do a uniqueness check every time you add an element to the array. For this you use `$addToSet` when doing a push.

shell:

    > db.agents.findOne({"name": "James Bond"}).languages.sort()
    [ "Arabic", "Mandarin", "Spanish", "Urdu" ]
    > db.agents.update({"name": "James Bond"}, {"$addToSet": {"languages": "English"}})
    > db.agents.update({"name": "James Bond"}, {"$addToSet": {"languages": "English"}})
    > db.agents.update({"name": "James Bond"}, {"$addToSet": {"languages": "English"}})
    > db.agents.findOne({"name": "James Bond"}).languages.sort()
    [ "Arabic", "English", "Mandarin", "Spanish", "Urdu" ]


pymongo:

    >>> db.agents.update({"name": "James Bond"}, {"$addToSet": {"languages": "English"}})


#### Upserts

In MongoDB, as in other databases, an `upsert` is an update is added to the database even if the initial query is not found. Here notice we add a third arguement to the `update` command to identify this as an "upsert = True" update:

shell:

    > db.agents.update({"name": "Me"}, {"languages": ["English", "Old Norse"]}, {"upsert": true})
    > db.agents.find()
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }
    ...
    { "_id" : ObjectId("...86e"), "languages" : [ "English", "Old Norse" ] }
    > db.agents.remove({"_id" : ObjectId("...86e")})  // just clean up

pymongo:

    >>> db.agents.update({"name": "Me"}, {"languages": ["English", "Old Norse"]}, upsert=True)


#### Multiple Documents

By default, the `update` method only updates the first document it finds that matches the update criteria.  But if we want to update ALL documents that match the update criteria, we will use the fourth arguement to the `update` command:

shell:

    > db.agents.update({"name" : {"$exists": true}},
          {"$set": {"Status": "Active"}}, false, true)
    > db.agents.find()
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava", "Status" : "Active", ... }
    { "_id" : ObjectId("...e35"), "name" : "James Bond", "Status" : "Active", ... }
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan", "Status" : "Active", ... }

pymongo:

    >>> db.agents.update({"name" : {"$exists": True}},
            {"$set": {"Status": "Active"}}, upsert=False, multi=True)


### Write Concerns

The default write concern is "awknowledged", and that means when you run a command against MongoDB, you get a response back. So if it fails, you know.  There is an "unawknowledged" option, whereby you get no response back at all.

This seems like a terrible option to me. Maybe it's useful in low-priority logging situations? Maybe.


## Querying (`find`)

The primary tools for pulling data from MongoDB are `find` and `findOne`/`find_one`. The first parameter you pass it is a document you try to match to all the documents in a collection.  The second parameter is a document used to select only certain keys to be returned from each document.

shell:

    > db.agents.findOne()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }

    > db.agents.findOne({}, {"name": 1})
    { "name" : "James Bond" }

    > db.agents.find()
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

    > db.agents.find({}, {"name": 1})
    { "name" : "James Bond" }
    { "name" : "Scarlet Papava" }
    { "name" : "Alec Trevelyan" }

pymongo:

    >>> db.agents.find_one()
    {'_id': ObjectId('...e35'), 'name': 'James Bond'}

    >>> for doc in db.agents.find():
    ...     print(doc)
    ... 
    {'_id': ObjectId('...e35'), 'name': 'James Bond'}
    {'_id': ObjectId('...6dc'), 'name': 'Scarlet Papava'}
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

Okay, let us add some data to our `agents` database before we continue:

shell:

    > db.agents.update({"name": "James Bond"}, {"$set": {"number_of_kills": 100}})
    > db.agents.update({"name": "Scarlet Papava"}, {"$set": {"number_of_kills": 25}})
    > db.agents.update({"name": "Alec Trevelyan"}, {"$set": {"number_of_kills": 123}})
    > 
    > db.agents.update({"name": "James Bond"}, {"$set": {"age": 36}})
    > db.agents.update({"name": "Scarlet Papava"}, {"$set": {"age": 25}})
    > db.agents.update({"name": "Alec Trevelyan"}, {"$set": {"age": 45}})

pymong:

    same as shell

There are four extra conditional keywords you can use to increase the specificity of your queries:

* `$lt` - less than
* `$lte` - less than or equal to
* `$gt` - greater than
* `$gte` - greater than or equal to

These four conditionals are used as part of the first paratmeter in your `find` query:

shell:

    > db.agents.find({"age": {"$gt": 30, "$lte": 65}}, {"name": 1})
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

pymongo:

    >>> list(db.agents.find({"age": {"$gt": 30, "$lte": 65}}, {"name": 1}))
    [{'_id': ObjectId('...e35'), 'name': 'James Bond'},
     {'_id': ObjectId('...6dd'), 'name': 'Alec Trevelyan'}]

Multiple different queries can be combined into one using the conjunction operators: `$or`, `$in`, `$nin`, or `$not`. Each of these does basically what you would expect, but the syntax needs some explanation.

shell:

    > db.agents.find({"age": {"$in": [25, 30]}}, {"name": 1})
      { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }
    > db.agents.find({"age": {"$nin": [25, 30]}}, {"name": 1})
      { "_id" : ObjectId("...e35"), "name" : "James Bond" }
      { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }
    > db.agents.find({"age": {"$not": {"$nin": [25, 30]}}}, {"name": 1})
      { "_id" : ObjectId("....6dc"), "name" : "Scarlet Papava" }
    > db.agents.find({"$or": [{"age": {"$gte": 40}},
                       {"number_of_kills": {"$gt": 50}}]}, {"name": 1})
      { "_id" : ObjectId("...e35"), "name" : "James Bond" }
      { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

pymongo:

    >>> list(db.agents.find({"age": {"$in": [25, 30]}}, {"name": 1}))
      [{'_id': ObjectId('...6dc'), 'name': 'Scarlet Papava'}]
    >>> list(db.agents.find({"age": {"$nin": [25, 30]}}, {"name": 1}))
      [{'_id': ObjectId('...e35'), 'name': 'James Bond'},
       {'_id': ObjectId('...6dd'), 'name': 'Alec Trevelyan'}]
    >>> list(db.agents.find({"age": {"$not": {"$nin": [25, 30]}}}, {"name": 1}))
      [{'_id': ObjectId('...6dc'), 'name': 'Scarlet Papava'}]
    >>> list(db.agents.find({"$or": [{"age": {"$gte": 40}},
               {"number_of_kills": {"$gt": 50}}]}, {"name": 1}))
      [{'_id': ObjectId('...e35'), 'name': 'James Bond'},
       {'_id': ObjectId('...6dd'), 'name': 'Alec Trevelyan'}]

There are also handy conditionals for queries specifically about arrays. First though, let's add some data to our database for testing:

shell:

    > db.agents.update({"name": "Scarlet Papava"},
        {"$set": {"languages": ["English", "Russian", "French"]}})
    > db.agents.update({"name": "Alec Trevelyan"},
        {"$set": {"languages": ["English", "Russian", "Latin"]}})

pymongo:

    >>> db.agents.update({"name": "Scarlet Papava"},
        {"$set": {"languages": ["English", "Russian", "French"]}})

The most common array conditional keywords are:

* `$all` - test if an array has all the elements in a provided array
* `$size` - find the size of the given array
* `$slice` - return the first (or last) N elements from an array

The `$size` keyword is used just like every other keyword:

shell:

    > db.agents.find({"languages": {"$size": 5}}, {"name": 1})
    { "_id" : ObjectId("...e35"), "name" : "James Bond" }

pymongo:

    >>> list(db.agents.find({"languages": {"$size": 5}}, {"name": 1}))
    [{'_id': ObjectId('...e35'), 'name': 'James Bond'}]

Mongo also provides `$skip`, `$limit`, and `$sort` keywords, which do about what you'd expect, and are syntactically easy to use:

shell:

    > db.agents.find({"languages": {"$size": 3}}, {"name": 1})
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }

    > db.agents.find({"languages": {"$size": 3}}, {"name": 1}).skip(1)
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }
    > db.agents.find({"languages": {"$size": 3}}, {"name": 1}).limit(1)
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }
    > db.agents.find({"languages": {"$size": 3}}, {"name": 1}).sort({"name": 1})
    { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }
    { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }

pymongo:

    >>> list(db.agents.find({"languages": {"$size": 3}}, {"name": 1}))
        [{ "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" },
         { "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }]

    >>> list(db.agents.find({"languages": {"$size": 3}}, {"name": 1}).skip(1))
        [{ "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" }]
    >>> list(db.agents.find({"languages": {"$size": 3}}, {"name": 1}).limit(1))
        [{ "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }]
    >>> db.agents.find({"languages": {"$size": 3}}, {"name": 1}).sort({"name": 1})
        [{ "_id" : ObjectId("...6dd"), "name" : "Alec Trevelyan" },
         { "_id" : ObjectId("...6dc"), "name" : "Scarlet Papava" }]


## Indexing

TODO


## Special Indexes

TODO

#### Capped Collections

TODO

#### TTL Indexes

TODO

#### Other Indexes

MongoDB also supports special indexes for searching in text and geospatial problem sets.  They look well-implemented but are so use-case specific I will not cover them here.


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
