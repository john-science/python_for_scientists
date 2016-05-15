# MySQL Databases

There are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc. And each different type of database has it's own Python library. In this lecture we will look at MySQL databases using the `MySQLdb` library. MySQL is one of the most popular database choices for medium-sized projects today, and it is open-source. If you're interested, you can look [here](https://wiki.python.org/moin/DatabaseInterfaces) for a listing of the most popular database interfaces in Python.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. And that is no different for MySQL, look [here](http://dev.mysql.com/doc/refman/5.7/en/installing.html) for instructions on installing and starting a MySQL server on your computer. You will also need to install the `mysql-python` library. If you are using Anaconda, this should be as easy as:

    conda install mysql-python

## Creating a Database

To start off with, we want to create a database and probably a table with some data in it. To make things easier, the first time through we will do this by directly signing into your MySQL Server from the command line (not using Python). But first, let's save this text off into a plain text file called `menu.sql`:

    CREATE DATABASE `menu`;
    USE menu;

    DROP TABLE IF EXISTS `fish`;
    SET @saved_cs_client     = @@character_set_client;
    SET character_set_client = utf8;

    CREATE TABLE `fish` (
        `ID` int(11) NOT NULL auto_increment,
        `NAME` varchar(30) NOT NULL default '',
        `PRICE` decimal(5,2) NOT NULL default '0.00',
        PRIMARY KEY (`ID`)
    ) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT
    CHARSET=latin1;
    SET character_set_client = @saved_cs_client;

    LOCK TABLES `fish` WRITE;
    INSERT INTO `fish` VALUES
    (1,'catfish','8.50'),(2,'catfish','8.50'),(3,'tuna','8.00'),(4,'catfish','5.00'),(5,'bass','6.75'),(6,'haddock','6.50'),(7,'salmon','9.50'),(8,'trout','6.00'),(9,'tuna','7.50'),(10,'yellowfin tuna','12.00'),(11,'yellowfin tuna','13.00'),(12,'tuna','7.50');
    UNLOCK TABLES;

Now we log into the MySQL Server:

    $ mysql -u my_user_name -p

And execute our script:

    source menu.sql

Before we exit out of the the MySQL command line interface and start using Python, try looking around a bit and seeing what is on your Server:

    mysql> SHOW DATABASES;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | menu               |
    | mysql              |
    | performance_schema |
    +--------------------+
    5 rows in set (0.01 sec)

    mysql> SHOW TABLES;
    +----------------+
    | Tables_in_menu |
    +----------------+
    | fish           |
    +----------------+
    1 row in set (0.01 sec)

    mysql> SELECT * from fish LIMIT 1;
    +----+---------+-------+
    | ID | NAME    | PRICE |
    +----+---------+-------+
    |  1 | catfish |  8.50 |
    +----+---------+-------+
    1 row in set (0.00 sec)

    mysql> SELECT NAME,count(*) from fish GROUP BY NAME;
    +----------------+----------+
    | NAME           | count(*) |
    +----------------+----------+
    | bass           |        1 |
    | catfish        |        3 |
    | haddock        |        1 |
    | salmon         |        1 |
    | trout          |        1 |
    | tuna           |        3 |
    | yellowfin tuna |        2 |
    +----------------+----------+
    7 rows in set (0.00 sec)

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

## Example Script

 * TODO form of this lecture

## Problem Sets

 * TODO

## Further Reading

 * TODO

[Back to Syllabus](../../README.md)

    con.close()
