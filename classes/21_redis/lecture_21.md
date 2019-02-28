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
* hash
* list
* set

So let's use some variables of each of these types and see how they work.


### Simple Types

#### Strings

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

#### Integers

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

#### Floats

Those are really the two primitive types worth trusting in Redis, though it does store off doubles (and calls them float, just like Python):

    127.0.0.1:6379> set pi 3.14159265
    OK
    127.0.0.1:6379> incrbyfloat pi 1.111
    "4.25259265"
    127.0.0.1:6379> get pi
    "4.25259265"

#### Hashes

Now that we have our primitive data types out of the way, Redis provides us a handy way to store nested key/value pairs: hashes. Similar to before, you can set and get hashes with `HSET` and `HVALS`/`HKEYS`:

    127.0.0.1:6379> hset name first "Emmy" last "Noether"
    (integer) 0
    127.0.0.1:6379> hkeys name
    1) "first"
    2) "last"
    127.0.0.1:6379> hvals name
    1) "Emmy"
    2) "Noether"


### Doing Multiple Things at Once

First off, you can `SET` and `GET` more than one thing a time use multi-set (`MSET`) and multi-get (`MGET`):

    127.0.0.1:6379> MSET abc 1 def 3
    OK
    127.0.0.1:6379> MGET def abc
    1) "3"
    2) "1"

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

Just like Python, Redis supports a list data structure. (And, just like Python, this is a [doubly-linked list](https://en.wikipedia.org/wiki/Doubly_linked_list).) To interact with a list in Redis you can "push" new elements onto the left side of the list (`LPUSH`) or the right side of the list (`RPUSH`) or you can take one element off the left side of the list (`LPOP`) or the right side of the list (`RPOP`). And we can see what elements are on the list using "list range" (`LRANGE`). Let's try it.

We create a new list by "push"ing elements onto the list, just like we would if it already existed:

    127.0.0.1:6379> rpush rainbow blue green yellow
    (integer) 3

Okay, but now we want the ability to view the elements of the list, which we do with the `LRANGE` function:

    127.0.0.1:6379> lrange rainbow 0 -1
    1) "blue"
    2) "green"
    3) "yellow"

That should seem *really* similar to indexing a list in Python. Except in Redis there are no defaults, so you explicitly have to say the first and last index you want to see:

    127.0.0.1:6379> lrange rainbow 0 1
    1) "blue"
    2) "green"
    127.0.0.1:6379> lrange rainbow 0 111
    1) "blue"
    2) "green"
    3) "yellow"

But, again just like Python, you can also use negative numbers to count from the right end of the list:

    127.0.0.1:6379> lrange rainbow 1 -1
    1) "green"
    2) "yellow"
    127.0.0.1:6379> lrange rainbow 1 -2
    1) "green"

Cool, so let's say we want to add more elements to the right side of the list:

    127.0.0.1:6379> rpush rainbow orange
    (integer) 4
    127.0.0.1:6379> rpush rainbow red
    (integer) 5
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "blue"
    2) "green"
    3) "yellow"
    4) "orange"
    5) "red"

Likewise, we can add elements to the left side of the list:

    127.0.0.1:6379> lpush rainbow indigo
    (integer) 6
    127.0.0.1:6379> lpush rainbow violet
    (integer) 7
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "violet"
    2) "indigo"
    3) "blue"
    4) "green"
    5) "yellow"
    6) "orange"
    7) "red"

Some of these command names are a little obtuse if you don't already know what they are. Sure. But once you know "Left Push" == "LPUSH", they are super easy to use. So there's some trade off there.

Unlike Python lists, which you can split and chop in lots of ways, Redis lists are only really editable in one fast, efficient way: by popping elments off either end of the list. For instance, we can *pop* elements off the left end of the list. That will return a single element to us to use, but also shorten the list by one. For example:

    127.0.0.1:6379> lpop rainbow
    "violet"
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "indigo"
    2) "blue"
    3) "green"
    4) "yellow"
    5) "orange"
    6) "red"
    127.0.0.1:6379> lpop rainbow
    "indigo"
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "blue"
    2) "green"
    3) "yellow"
    4) "orange"
    5) "red"

It works the same way for *popping* things off the right side of the list:

    127.0.0.1:6379> rpop rainbow
    "red"
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "blue"
    2) "green"
    3) "yellow"
    4) "orange"
    127.0.0.1:6379> rpop rainbow
    "orange"
    127.0.0.1:6379> lrange rainbow 0 -1
    1) "blue"
    2) "green"
    3) "yellow"

List in Redis, just like in Python, are super handy and easy to use. But the slightly more limited functionality in Redis means that Redis list are also super fast. Which is nice.

*SIDE NOTE*: For the more computer science inclined, it is useful to note that people typically use Redis lists as either [queues](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) or [stacks](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). Remember, a queue is [FIFO](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) so it would mean designing your code to use `RPUSH` and `LPOP`. And to create a [stack (LIFO)](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) you would just use `LPUSH` and `LPOP`.


### Sets

Redis sets are must like Python sets, they are an unordered collection of unique objects. To create a new set, or add elements to an existing one, use `SADD`, and determine what elments are already in a set, use `SMEMBERS`:

    127.0.0.1:6379> sadd tolkien elves wizards
    (integer) 2
    127.0.0.1:6379> smembers tolkien
    1) "wizards"
    2) "elves"

But uniquenes is the name of the game here. It doesn't matter how many times we add a string to the set, it will still only ever be in the set once:

    127.0.0.1:6379> sadd tolkien elves
    (integer) 0
    127.0.0.1:6379> sadd tolkien elves
    (integer) 0
    127.0.0.1:6379> sadd tolkien wizards
    (integer) 0
    127.0.0.1:6379> smembers tolkien
    1) "wizards"
    2) "elves"
    127.0.0.1:6379> sadd tolkien swords
    (integer) 1
    127.0.0.1:6379> smembers tolkien
    1) "swords"
    2) "wizards"
    3) "elves"

Just to help give us another exampl, let's create another set:

    127.0.0.1:6379> sadd rowling wizards wands goblins
    (integer) 3
    127.0.0.1:6379> smembers rowling
    1) "wands"
    2) "wizards"
    3) "goblins"
    127.0.0.1:6379> 
    127.0.0.1:6379> 

Okay, now that we have two sets we can start comparing them, using all the basic set operations. For instance, if we want to see what elements two sets have in common (the "interesection" of the sets), we use `SINTER`:

    127.0.0.1:6379> sinter tolkien rowling
    1) "wizards"

To figure out what elements are in the left set that aren't in the right set, (the "difference"), we use `SDIFF`:

    127.0.0.1:6379> sdiff tolkien rowling
    1) "elves"
    2) "swords"

And there is no "right difference", so to find that we have to switch the order of the sets being compared:

    127.0.0.1:6379> sdiff rowling tolkien
    1) "wands"
    2) "goblins"

To make a big set with all the elements of both, we use `SUNION`. But the result is still a set, so notice how "wizards" still only appears once:

    127.0.0.1:6379> sunion tolkien rowling
    1) "wizards"
    2) "elves"
    3) "swords"
    4) "wands"
    5) "goblins"

There are lots of less commmonly used set operations you can look up, but one that seems useful to me is the ability to automatically store off the union of two sets as a new set:

    127.0.0.1:6379> sunionstore fantasy tolkien rowling
    (integer) 5
    127.0.0.1:6379> smembers fantasy
    1) "wizards"
    2) "elves"
    3) "swords"
    4) "wands"
    5) "goblins"

Set theory is a big topic, and there are lots of little subtleties we are glossing over, but this is the major flavor of sets in Redis. They are really easy to use and very performant.


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
