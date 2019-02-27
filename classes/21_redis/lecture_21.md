# Redis

>  What is Redis?

Redis is an in-memory key-value store.

In theory, Redis is just a specialized, in-memory database. But because Redis has more limited storage options than most databases, it is Very Fast. It's also deliciously light-weight. Redis is typically used for:

* [queues](https://en.wikipedia.org/wiki/Queueing_theory)
* [caches](https://en.wikipedia.org/wiki/Cache_(computing))
* [pub / subs](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)

## Install and Start

We will actually need to install two things for this lecture:

1. Redis itself
2. A Python library for interacting with Redis

#### Installing Redis

Look [here](https://redis.io/topics/quickstart) for instruction on installing Redis on any modern computer.

On my Linux box it was as easy as:

    sudo apt-get install redis-server

#### Installing RQ

The Python library we will use to iterface with Redis is [rq](https://python-rq.org/).

On my Linux box installing it was as easy as:

    pip install rq

#### Starting Redis

Once Redis is installed you can start the Redis server from the commandline:

    redis-server

And you can use the Redis Command Line Interface (CLI) to check that the service is up and running:

    redis-cli ping

In Linux, you can also check the status of the Redis service by doing:

    service redis status


# Redis via the CLI

First, let's learn Redis on its own terms. The Redis Command Line Interface (CLI) has over a hundred commands to drive control and operate data in Redis. We will can learn a lot about Redis by working through some of these commands. Then we will move on to learning how to do all of those same oeprations through the Python `rq` library.

You can boot up the Redis CLI from the command lineL

    $ redis-cli
    127.0.0.1:6379>

## CLI Commands, by Data Structure

Redis stores key-values pairs. The keys can be (simple) strings, but the the values can be one of a few (really performant) data structures:

* integer
* string
* list
* set
* sorted sets

So let's use some variables of each of these types and see how they work.

### Simple Types

Setting the variable `hello` to the string `World` is easy:

    127.0.0.1:6379> set hello World
    OK
    127.0.0.1:6379> get hello
    "World"

So now we can store a key/value pair of strings we want:

    127.0.0.1:6379> set big_lebowski "The dude abides"
    OK
    127.0.0.1:6379> get big_lebowski
    "The dude abides"

Similarly, we can store integers in Redis:

    127.0.0.1:6379> set count 1
    OK
    127.0.0.1:6379> get count
    "1"

But for integers we have the ability to "increment by 1" with the `incr` command:

    127.0.0.1:6379> incr count
    (integer) 2
    127.0.0.1:6379> get count
    "2"
    127.0.0.1:6379> incr count
    (integer) 3
    127.0.0.1:6379> incr count
    (integer) 4
    127.0.0.1:6379> get count
    "4"

Those are really the two primitive types worth trusting in Redis, though it does store off doubles (and calls them float, just like Python):

    127.0.0.1:6379> set pi 3.14159265
    OK
    127.0.0.1:6379> incrbyfloat pi 1.111
    "4.25259265"
    127.0.0.1:6379> get pi
    "4.25259265"

### A Couple More Basics

First off, you can `SET` and `GET` more than one thing a time use multi-set (`MSET`) and multi-get (`MGET`):

    127.0.0.1:6379> MSET abc 1 def 3
    OK
    127.0.0.1:6379> MGET def abc
    1) "3"
    2) "1"

Now that we have our primitive data types out of the way, Redis provides us a handy way to store nested key/value pairs: hashes. Using hashes looks a lot like `SET` and `GET` for primitive types above, but you use `MSET` and `MGET`

> TODO

Okay, but you're a busy person, and when you interact with your Redis database you don't just want to send one tiny little command you have a LOT of things you want to do all in one go. For that, you will use `MULTI` to start you series of commands and `EXEC` to execute everything all in one go:

    127.0.0.1:6379> MULTI
    OK
    127.0.0.1:6379> set hi mom
    QUEUED
    127.0.0.1:6379> incr count
    QUEUED
    127.0.0.1:6379> EXEC
    1) OK
    2) (integer) 6

So, if all you wanted to do was store key/value pairs that were simple strings or primitive types, you'd be done here. But since we almost always need more powerful datastructures than that to store our data, let's take a look at two of the other, super powerful and fast, data types that come with Redis.


### Lists

TODO


### Sets

TODO


## Other Important Commands

Redis doesn't call them "databases", it calls them "namespaces". It's not important distinction. By default Redis dumps you into the `0` namespace. But you can select a namespace by using `SELECT`.

TODO: EXPIRY and such


# Redis via Python

TODO

## Choose Your Data Base

TODO

## CLI Commands, by Data Structure

TODO

### Simple Types

TODO

### Lists

TODO

### Sets

TODO

## Other Important Commands

TODO: EXPIRY and such


# Further Reading

 * [Redis official homepage](https://redis.io/)
 * [Redis data types](https://redis.io/topics/data-types-intro)
 * [rq](https://python-rq.org/) - our Python library of choice
 
[Back to Syllabus](../../README.md)
