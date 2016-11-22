# MySQL Databases

There are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc. And each different type of database has it's own Python library. In this lecture we will look at MySQL databases using the `MySQLdb` library. MySQL is one of the most popular database choices for medium-sized projects today, and it is open-source. If you're interested, you can look [here](https://wiki.python.org/moin/DatabaseInterfaces) for a listing of the most popular database interfaces in Python.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. And that is no different for MySQL, look [here](http://dev.mysql.com/doc/refman/5.7/en/installing.html) for instructions on installing and starting a MySQL server on your computer. You will also need to install the `mysql-python` library. If you are using Anaconda, this should be as easy as:

    conda install mysql-python

## Creating a Database

To start off with, we want to create a database and probably a table with some data in it. To make things easier, the first time through we will do this by directly signing into your MySQL Server from the command line (not using Python). But first, let's save this text off into a plain text file called `secret_agents_mysql.sql`:

    CREATE DATABASE `secret_agents`;
    USE secret_agents;

    DROP TABLE IF EXISTS `agents`;
    SET @saved_cs_client     = @@character_set_client;
    SET character_set_client = utf8;

    CREATE TABLE `agents` (
        `agentID` int(11) NOT NULL auto_increment,
        `code_name` varchar(3) NOT NULL default '007',
        `name` varchar(30) NOT NULL default 'James Bond',
        PRIMARY KEY (`agentID`)
    ) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT
    CHARSET=latin1;
    SET character_set_client = @saved_cs_client;

    LOCK TABLES `agents` WRITE;
    INSERT INTO `agents` VALUES (1,'001','Edward Donne');
    UNLOCK TABLES;

Now we log into the MySQL Server:

    $ mysql -u my_user_name -p

And execute our script:

    source secret_agents_mysql.sql

Before we exit out of the the MySQL command line interface and start using Python, try looking around a bit and seeing what is on your Server:

    mysql> SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | secret_agents      |
    | mysql              |
    | performance_schema |
    +--------------------+
    5 rows in set (0.00 sec)

    mysql> USE secret_agents;

    mysql> SHOW TABLES;
    +-------------------------+
    | Tables_in_secret_agents |
    +-------------------------+
    | agents                  |
    +-------------------------+
    1 row in set (0.01 sec)

    mysql> SELECT * from agents;
    +---------+-----------+--------------+
    | agentID | code_name | name         |
    +---------+-----------+--------------+
    |       1 | 001       | Edward Donne |
    +---------+-----------+--------------+
    1 row in set (0.00 sec)

    mysql> SELECT code_name,name from agents LIMIT 1;
    +-----------+--------------+
    | code_name | name         |
    +-----------+--------------+
    | 001       | Edward Donne |
    +-----------+--------------+
    1 row in set (0.00 sec)

When you're done looking around, exit the MySQL command line. From here on out, we will be working in the Python interpreter (or in Python scripts).

## Connecting to Databases

To create a connection to our new `menu` database, we need to use our credentials:

    import MySQLdb
    con = MySQLdb.connect(host='localhost', user='my_user_name', passwd='my_secret', db='menu')

Note that you don't actually need to write `host=` or `user=`, these four items are always in the same order. For now, we will write them explicitly, until they become more familiar.

The "connection" above allows us to talk to a particular database on a particular MySQL Server, but to execute any commands against that server, we will need a cursor:

    cursor = con.cursor()

There are several ways to interact with the database through this cursor, but most of them will require a final execution step:

    cursor.execute()

Finally, when we are done with our database, we need to remember to close the connection:

    con.close()

## CRUD

SQL database applications are called [relational databases](https://en.wikipedia.org/wiki/Relational_database) because they store data in tables and use the four basic functions to deal with the data in their persistent storage:

    Operation | SQL
    :--- | :---
    Create | INSERT
    Read (Retrieve) | SELECT
    Update (Modify) | UPDATE
    Delete (Destroy) | DELETE

## MySQL Queries

All SQL-like queries have a basic structure, like the word-order in a spoken language. In SQL, the verb always comes first.

For instance, if I wanted to say:

    "Give me everything from the fish table"

I would translate that into the MySQL query:

    SELECT * FROM fish;

Let's look at the grammar of this sentence:

* SELECT - query the database, to retrieve information
* * - get everything from the table(s) of interest
* FROM - point to the table(s) of interest
* "fish" - the name of the table
* ; - signifies the end of a SQL statement (sentence)

Note that `SELECT` could be written `select` and `FROM` could be written `from`. The ALL CAPS is not mandatory, but it is a standard among people who write a lot of SQL to make it easier to read which words in a SQL statement are part of the SQL language and which are just names of tables or columns.

### Query Quantifiers

There are several other helpful quantifiers to go along with your `SELECT` statements.

#### asterisk (*)

In the above query, we used the `*` symbol to say we wanted "all the columns" from that table. But there were three other major options:

    SELECT ALL FROM fish;  # same as `*`
    SELECT DISTINCT FROM fish;  # sort the results set into unique values
    SELECT DISTINCTROW FROM fish;  # make sure the entire column is unique

#### WHERE

The word `WHERE` is used to limit the results of a search using a predicate (logical test). `WHERE` statements belong after the table name:

    SELECT * FROM fish WHERE id='5';

In our `fish` table, this would return a single record:

    +----+------+-------+
    | ID | NAME | PRICE |
    +----+------+-------+
    |  5 | bass |  6.75 |
    +----+------+-------+

#### GROUP BY

The word `GROUP BY` allows you to group the results by one of three parameters:

* `col_name` - The name of one of the table columns
* `expr` - A regular expression
* `position` - A position in the table

You can also have MySQL return the grouped result in `ASC`cending or `DESC`ending order. And you can create a final line at the end that summarizes the previous lines using `WITH ROLLUP`. All of these together give us a generic `GROUP BY` statement that looks like:

    GROUP BY (col_name | expr | position) (ASC | DESC) (WITH ROLLUP)

For instance, we could select the different types of fish available in our table by:

    SELECT * FROM fish GROUP BY name;

And it will return something like:

    +----+----------------+-------+
    | ID | NAME           | PRICE |
    +----+----------------+-------+
    |  5 | bass           |  6.75 |
    |  1 | catfish        |  8.50 |
    |  6 | haddock        |  6.50 |
    |  7 | salmon         |  9.50 |
    |  8 | trout          |  6.00 |
    |  3 | tuna           |  8.00 |
    | 10 | yellowfin tuna | 12.00 |
    +----+----------------+-------+

Or we could ask how many different copies of each fish we have on our menu using `count(*)` as a meta-column:

    SELECT name,count(*) FROM fish GROUP BY name;

And we would get something much like:

    +----------------+----------+
    | name           | count(*) |
    +----------------+----------+
    | bass           |        1 |
    | catfish        |        3 |
    | haddock        |        1 |
    | salmon         |        1 |
    | trout          |        1 |
    | tuna           |        3 |
    | yellowfin tuna |        2 |
    +----------------+----------+

#### HAVING

The word `HAVING` can be used exactly like `WHERE`, but that is considered poor programming. You use `HAVING` on aggregate variables (like `sum()` and `count()`, which we will talk about later. For now:

    SELECT * FROM fish GROUP BY name HAVING id>'3';

This should return:

    +----+----------------+-------+
    | ID | NAME           | PRICE |
    +----+----------------+-------+
    |  5 | bass           |  6.75 |
    |  6 | haddock        |  6.50 |
    |  7 | salmon         |  9.50 |
    |  8 | trout          |  6.00 |
    | 10 | yellowfin tuna | 12.00 |
    +----+----------------+-------+

#### ORDER BY

The clause `ORDER BY` sorts the results of a query, taking almost the same options as `GROUP BY`:

    ORDER BY (col_name | expr | position) (ASC | DESC)

For instance:

    SELECT * FROM fish ORDER BY id DESC;

The query would return:

    +----+----------------+-------+
    | ID | NAME           | PRICE |
    +----+----------------+-------+
    | 12 | tuna           |  7.50 |
    | 11 | yellowfin tuna | 13.00 |
    | 10 | yellowfin tuna | 12.00 |
    |  9 | tuna           |  7.50 |
    |  8 | trout          |  6.00 |
    |  7 | salmon         |  9.50 |
    |  6 | haddock        |  6.50 |
    |  5 | bass           |  6.75 |
    |  4 | catfish        |  5.00 |
    |  3 | tuna           |  8.00 |
    |  2 | catfish        |  8.50 |
    |  1 | catfish        |  8.50 |
    +----+----------------+-------+

#### LIMIT

The clause `LIMIT` can be used to retrieve only a set amount of records. For instance:

    SELECT * FROM fish ORDER BY id DESC LIMIT 1;

The query would return:

    +----+----------------+-------+
    | ID | NAME           | PRICE |
    +----+----------------+-------+
    | 12 | tuna           |  7.50 |
    +----+----------------+-------+

However, you can set an upper and lower number of records that you want by using a range of numbers:

    SELECT * FROM fish ORDER BY id DESC LIMIT 1,3;

The query would return:

    +----+----------------+-------+
    | ID | NAME           | PRICE |
    +----+----------------+-------+
    | 12 | tuna           |  7.50 |
    | 11 | yellowfin tuna | 13.00 |
    | 10 | yellowfin tuna | 12.00 |
    +----+----------------+-------+

#### LIMIT vs HAVING

The major difference to pick `HAVING` vs `LIMIT` is performance. Use `HAVING` in most situations in which you are concerned with speed. The idea is that `HAVING` reduces the amount of data SQL is worried about *before* much of the query logic takes place, and `LIMIT` lets all the logic unfold before limiting the number of results.

The only time it will improve performance to use `LIMIT` is when the results returned by your query are very sizable indeed, but you definitely have ample resouces to deal with the large query and results.

#### INTO OUTFILE

The clause `INTO OUTFILE` is particularly useful for people working in MySQL without Python. But even if you are working with a MySQL database through the Python `MySQLdb` library, this might be a quick-and-dirty way to write your query results to a file. It works like you might guess:

    SELECT * FROM fish ORDER BY id DESC LIMIT 1,5 INTO OUTFILE 'fishes.txt';

## Passing a Query to MySQL

Again, to query a MySQL database in Python, you will need to set up a connection and then a cursor:

    import MySQLdb
    con = MySQLdb.connect(host='localhost', user='my_user_name', passwd='my_secret', db='menu')
    cursor = con.cursor()

#### A Simple SELECT Query

To execute a basic "get all" query through Python, we would do:

    command = cursor.execute('SELECT * FROM fish;')

The `command` object holds all of the results in memory (RAM), until you want them. The basic way to access them is to access them all at one time:

    results = cursor.fetchall()

What is a returned in the `results` object is a `tuple` of rows where each row is a `tuple` of the column values:

    >>> print(results)
    ((1L, 'tuna', Decimal('7.50')), (2L, 'bass', Decimal('6.75'), ...)

Since the `results` object is just a `tuple`, you could loop over the rows when processing the data. Or, you could just grab one row at a time using `fetchone()`:

    >>> command = cursor.execute('SELECT * FROM fish;')
    >>> print(cursor.fetchone())
    (1L, 'tuna', Decimal('7.50'))

## Looking at Your Database

The SQL statement for listing the tables in a database is:

    SHOW TABLES in menu;

In our case, we already connected to a specific database (using `MySQLdb.connect`), so we can be less specific:

    >>> command = cursor.execute('SHOW TABLES;')
    >>> results = cursor.fetchall()
    >>> print(results)
    (1, 'catfish', Decimal('8.50'))

## Example Script

 * TODO form of this lecture

## Problem Sets

 * TODO

## Further Reading

 * TODO

[Back to Syllabus](../../README.md)

    con.close()
