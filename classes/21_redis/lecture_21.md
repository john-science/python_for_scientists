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
