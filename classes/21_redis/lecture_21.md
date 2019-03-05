# Redis

>  What is Redis?

Redis is an in-memory key-value store.

In theory, Redis is just a specialized, in-memory database. But because Redis has more limited storage options (only key-value pairs, not tables or whatever) it is Very Fast. It's also deliciously light-weight. Redis is typically used for:

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

#### Installing Redis for Python

The Python library we will use to iterface with Redis is just called [Redis](https://redislabs.com/lp/python-redis/).

On my Linux box installing it was as easy as:

    pip install redis

#### Starting Redis

Once Redis is installed you can start the Redis server from the commandline:

    redis-server

And you can use the Redis Command Line Interface (CLI) to check that the service is up and running:

    redis-cli ping

In Linux, you can also check the status of the Redis service by doing:

    service redis status


# Redis via the CLI

First, let's learn Redis on its own terms. The Redis Command Line Interface (CLI) has over a hundred commands to drive control and operate data in Redis. We will can learn a lot about Redis by working through some of these commands. Then we will move on to learning how to do all of those same oeprations through the Python `Redis` library.

You can boot up the Redis CLI from the command lineL

    $ redis-cli
    127.0.0.1:6379>

## Basic Redis Commands

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

Okay, so now we know how to use the basic Redis data structures. Let's learn some more of the kinds of tools we'll want to do our work.

#### Choosing a Namespace

Redis doesn't call them "databases", it calls them "namespaces". It's not important distinction. By default Redis dumps you into the `0` namespace. But you can select a namespace by using `SELECT`.

#### Which keys exist?

If you want to list all the keys that exist in your current namespace just type:

    127.0.0.1:6379> KEYS *
    1) "rowling"
    2) "hello"
    3) "hi"
    4) "bond"
    5) "rainbow"
    6) "def"
    ...

But caveat emptor, if there are a million keys in your namespace you just returned way too much stuff. A better solution might be to change your logic to just test if  single key exists. The command `EXISTS` returns `1` for "true" and `0` for "false":

    127.0.0.1:6379> EXISTS rowling
    (integer) 1
    127.0.0.1:6379> EXISTS tolkien
    (integer) 1
    127.0.0.1:6379> EXISTS Pratchett
    (integer) 0

#### Setting keys to disappear on timeout

If you want a key to disappear of N seconds, you can you `EXPIRE`:

    127.0.0.1:6379> set ice "I'm melting..."
    OK
    127.0.0.1:6379> expire ice 10
    (integer) 1

You can use `EXISTS` to check if the key is still there:

    127.0.0.1:6379> exists ice
    (integer) 1

Now wait 11 seconds, and it is gone:

    127.0.0.1:6379> exists ice
    (integer) 0

Setting and expiring keys is so common you can do both at once using the `SETEX` command:

    127.0.0.1:6379> setex ice 10 "I'm melting..."

If you want to know how long a key has left before it expires:

    127.0.0.1:6379> ttl ice
    7

Lastly, you can stop a key from expiring at any time using `PERSIST`:

    127.0.0.1:6379> persist ice


# Redis via Python

Above we learned about the basic Redis functionality. But this is a Python class, so let's go over all those commands an functionality again using Python through the `Redis` library.

## Connecting to Redis via Python

Connecting to a Redis instance is pretty easy via Python:

```python
import redis

r = redis.Redis(host='localhost',
                port=6379)
```

Or, if you have a password set up:

```python
import redis

r = redis.Redis(host='hostname',
                port=port, 
                password='password')
```

## Basic Redis Commands

Let's learn how to use the basic Redis datastructures through Python:

* integer
* string
* hash
* list
* set

### Simple Types

#### Strings

Setting the variable `hello` to the string `World` is easy:

```python
r.set("hello", "world")
r.get("hello")
# world
```

So now we can store a key/value pair of strings we want:

```python
r.set("big_lebowski", "The dude abides")
r.get("big_lebowski")
# "The dude abides"
```

#### Integers

Similarly, we can store integers in Redis:

```python
r.set("count", 1)
# True
r.get("count")
# 1
```

But for integers we have the ability to "increment by 1" with the `incr` command:

```python
r.incr('count')
# 2
r.get("count")
# 2
r.incr('count')
# 3
r.incr('count')
# 4
r.get("count")
# 4
```

#### Floats

Those are really the two primitive types worth trusting in Redis, though it does store off doubles (and calls them float, just like Python):

```python
r.set("pi", 3.14159265)
r.incrbyfloat('pi', 1.111)
r.get("count")
# 4.25259265
```

#### Hashes

Now that we have our primitive data types out of the way, Redis provides us a handy way to store nested key/value pairs: hashes. Similar to before, you can set and get hashes with `HSET` and `HVALS`/`HKEYS`:

```python
r.hset("name", "first", "Emmy")
r.hset("name", "last", "Noether")
r.hkeys("name")
# ["first", "last"]
r.hvals("name")
# ["Emmy", "Noether"]
```

### Doing Multiple Things at Once

First off, you can `SET` and `GET` more than one thing a time use multi-set (`MSET`) and multi-get (`MGET`):

```python
r.mset({'abc': 1, 'def': 3})
r.mget(['abc', 'def'])
# [b'1', b'3']
```

So, if all you wanted to do was store key/value pairs that were simple strings or primitive types, you'd be done here. But since we almost always need more powerful datastructures than that to store our data, let's take a look at two of the other, super powerful and fast, data types that come with Redis.


### Lists

To interact with a list in Redis you can "push" new elements onto the left side of the list (`LPUSH`) or the right side of the list (`RPUSH`) or you can take one element off the left side of the list (`LPOP`) or the right side of the list (`RPOP`). And we can see what elements are on the list using "list range" (`LRANGE`). Let's try it.

We create a new list by "push"ing elements onto the list, just like we would if it already existed:

```python
r.rpush('rainbow', 'blue')
r.rpush('rainbow', 'green')
r.rpush('rainbow', 'yellow')
```

Okay, but now we want the ability to view the elements of the list, which we do with the `LRANGE` function:

```python
r.lrange('rainbow', 0, -1)
# ['blue', 'green', 'yellow']
```


That should seem *really* similar to indexing a list in Python. Except in Redis there are no defaults, so you explicitly have to say the first and last index you want to see:

```python
r.lrange('rainbow', 0, 1)
# ['blue', 'green']
r.lrange('rainbow', 0, 111)
# ['blue', 'green', 'yellow']
```


But, again just like Python, you can also use negative numbers to count from the right end of the list:

```python
r.lrange('rainbow', 1, -1)
# ['green', 'yellow']
r.lrange('rainbow', 1, -2)
# ['green']
```

Cool, so let's say we want to add more elements to the right side of the list:

```python
r.rpush('rainbow', 'orange')
r.rpush('rainbow', 'red')
r.lrange('rainbow', 0, -1)
['blue', 'green', 'yellow', 'orange', 'red']
```

Likewise, we can add elements to the left side of the list:

```python
r.lpush('rainbow', 'indigo')
r.lpush('rainbow', 'violet')
r.lrange('rainbow', 0, -1)
['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

Some of these command names are a little obtuse if you don't already know what they are. Sure. But once you know "Left Push" == "LPUSH", they are super easy to use. So there's some trade off there.

Unlike Python lists, which you can split and chop in lots of ways, Redis lists are only really editable in one fast, efficient way: by popping elments off either end of the list. For instance, we can *pop* elements off the left end of the list. That will return a single element to us to use, but also shorten the list by one. For example:

```python
r.lpop('rainbow')
# 'violet'
r.lrange('rainbow', 0, -1)
# ['indigo', 'blue', 'green', 'yellow', 'orange', 'red']
r.lpop('rainbow')
# b'indigo'
r.lrange('rainbow', 0, -1)
# ['blue', 'green', 'yellow', 'orange', 'red']
```

It works the same way for *popping* things off the right side of the list:

```python
r.rpop('rainbow')
# 'red'
r.lrange('rainbow', 0, -1)
# ['blue', 'green', 'yellow', 'orange']
r.rpop('rainbow')
# 'orange'
r.lrange('rainbow', 0, -1)
# ['blue', 'green', 'yellow']
```


### Sets

Redis sets are must like Python sets, they are an unordered collection of unique objects. To create a new set, or add elements to an existing one, use `SADD`, and determine what elments are already in a set, use `SMEMBERS`:

```python
r.sadd('tolkien', 'elves')
r.sadd('tolkien', 'wizards')
r.smembers('tolkien')
# {'elves', 'wizards'}
```

But uniquenes is the name of the game here. It doesn't matter how many times we add a string to the set, it will still only ever be in the set once:

```python
r.sadd('tolkien', 'elves')
r.sadd('tolkien', 'elves')
r.sadd('tolkien', 'wizards')
r.smembers('tolkien')
# {b'elves', b'wizards'}
r.sadd('tolkien', 'swords')
r.smembers('tolkien')
# {'elves', 'swords', 'wizards'}
```

Just to help give us another exampl, let's create another set:

```python
r.sadd('rowling', 'wizards')
r.sadd('rowling', 'wands')
r.sadd('rowling', 'goblins')
r.smembers('rowling')
# {'wands', 'goblins', 'wizards'}
```

Okay, now that we have two sets we can start comparing them, using all the basic set operations. For instance, if we want to see what elements two sets have in common (the "interesection" of the sets), we use `SINTER`:

```python
r.sinter('tolkien', 'rowling')
# {'wizards'}
```
To figure out what elements are in the left set that aren't in the right set, (the "difference"), we use `SDIFF`:

```python
r.sdiff('tolkien', 'rowling')
# {'elves', 'swords'}
```

And there is no "right difference", so to find that we have to switch the order of the sets being compared:

```python
r.sdiff('tolkien', 'rowling')
# {'wands', 'goblins'}
```

To make a big set with all the elements of both, we use `SUNION`. But the result is still a set, so notice how "wizards" still only appears once:

```python
r.sunion('rowling', 'tolkien')
# {'elves', 'swords', 'wizards', 'goblins', 'wands'}
```

There are lots of less commmonly used set operations you can look up, but one that seems useful to me is the ability to automatically store off the union of two sets as a new set:

```python
r.sunionstore('fantasy', 'rowling', 'tolkien')
r.smembers('fantasy')
# {'elves', 'swords', 'wizards', 'goblins', 'wands'}
```

## Other Important Commands

#### Choosing a Namespace

By default Redis dumps you into the `0` namespace. But you can select a namespace by using `r.select()`.

#### Which keys exist?

If you want to list all the keys that exist in your current namespace just type:

```python
r.keys()
# ['abc', 'fantasy', 'rowling', 'hi', 'bob', ...]
```

But caveat emptor, if there are a million keys in your namespace you just returned way too much stuff. A better solution might be to change your logic to just test if  single key exists. The command `r.exists()` returns a True/False:

```python
r.exists('rowling')
# 1
r.exists('tolkien')
# 1
r.exists('Pratchett')
# 0
```

#### Setting keys to disappear on timeout

If you want a key to disappear of N seconds, you can you `r.expire()`:

```python
r.set('ice', "I'm melting...")
r.expire('ice', 10)
```

You can use `r.exists()` to check if the key is still there:

```python
r.exists('ice')
# 1
```

Now wait 11 seconds, and it is gone:

```python
r.exists('ice')
# 0
```

Setting and expiring keys is so common you can do both at once using the `r.setex()` command:

```python
r.setex('ice', 10, "I'm melting...")
```

If you want to know how long a key has left before it expires:

```python
r.ttl('ice')
# 7
```

Lastly, you can stop a key from expiring at any time using `r.persist()`:

```python
r.persist('ice')
```


## RQ - A Typical Redis Use Case

Since Redis is a little funny in the database world, it might be helpful to see an example of Redis getting used in practice. We are going to create a queueing system. We want the ability to send long processes at our server, and let them execute one at a time until they're all done.

First, we need to install the `rq` library. It will be something like:

    pip install rq

Or perhaps:

    conda install rq

Now we need to start a "Worker", that will listen at various named queues:

    rq worker high normal low

Okay, now we can send jobs to queues with three different names: `high`, `medium`, or `low`.

First, let's pretend we have a big function that does a lot of heavy-lifting work around the office:

```python
def my_fancy_function(data, url):
    # ... stuff
    return thing
```

Now we can use `rq` and Redis to send our job to the queueing system to get run:

    from rq import Queue
    from redis import Redis
    from somewhere import my_fancy_function

    # tell RQ what Redis connection to use
    redis_conn = Redis()
    q = Queue('high', connection=redis_conn)

    # delay execution of our function
    job = q.enqueue(my_fancy_function, big_data, 'http://www.example.com')
    print(job.result)   # => None

    # now, wait a while, until the worker is finished
    time.sleep(10)
    print(job.result)   # lots of exiciting things

And, of course, the function you're trying to run might not return anything. It might just write a lot of data to text files, or create a bunch of plots. In which case, you may still want to return an error code, just to make sure you know if everything ran all right.

But that's it! You now have a queueing system that is infinitely flexible, totally free, and easy to use. Redis made it possible.


# Further Reading

 * [Redis official homepage](https://redis.io/)
 * [Redis data types](https://redis.io/topics/data-types-intro)cl
 * [Redis Python library](https://redislabs.com/lp/python-redis/)
 * [Redis with Python tutorial](https://www.bogotobogo.com/python/python_redis_with_python.php)
 * [rq](https://python-rq.org/) - our Python library of choice for building queues
 
[Back to Syllabus](../../README.md)
