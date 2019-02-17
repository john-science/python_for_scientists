# Redis

>  What is Redis?

Redis is an in-memory key-value store.

In theory, Redis is just a specialized, in-memory database. But because Redis has more limited storage options than most databases, it is Very Fast. It's also pretty light-weight. Redis is typically used for:

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


# Redis CLI Commands

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
