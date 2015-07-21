# Databases with SQLITE3

First off, there are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc.  And because each type of database needs a different interface, there are a lot of different libraries for dealing with databases in Python. Check [here](https://wiki.python.org/moin/DatabaseInterfaces) for a nice listing of the most popular database interfaces in Python.

We are going to discuss `sqlite3` because it is the only database library that comes standard with Python. It is also pretty great, working well with reasonably small, "light" databases.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. But one of the major features of `sqlite3` is that there is no server/service, it is just a file with all the data inside. This is particularly handy for smaller databases and for databases you want to included in an application.

## Creating and Connecting to Databases

We will not covert the topic of databases in great detail, but like most databases, `sqlite3` is a [relational database](https://en.wikipedia.org/wiki/Relational_database). That is, inside the database we have tables of data organized by rows and columns. And these tables can be organized inside schemas.

 * Coming Soon: database diagram

We will use the same command to open an existing database as we would use to create a new database:

    import sqlite3
    conn = sqlite3.connect('secret_agents.db')

The path given can be local or absolute, but make sure this folder is editable by Python.

## Creating a Table

From this point on, we will be leaving the realm of Python. That is, in order to alter a database we must write the SQL-like code that SQLite databases require. From this point on if we want to create, modify, or query information from a SQLite database, we will pass a string through our connection (`conn` above) containing SQL code to the database. This may seem inconvenient, since we just spent all this time learning Python. But if you want to deal with databases, you need to learn to talk on their level.

 * Coming Soon: execute, commit, and roleback

## Schemas & Permissions: Secret Agents Protect their Data

 * Coming Soon

## Basic Queries

 * Coming Soon

#### Joins

 * Coming Soon

![exploits of a mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

## Problem Sets

 * Coming Soon

## Further Reading

 * [Tutorials Point sqlite3 tutorial](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
 * [Zet Code sqlite3 tutorial](http://zetcode.com/db/sqlitepythontutorial/)
 * [Python Central sqlite3 tutorial](http://www.pythoncentral.io/introduction-to-sqlite-in-python/)
 * [Relational Databases](https://en.wikipedia.org/wiki/Relational_database)
 * [Database Schemas](https://www.informit.com/library/content.aspx?b=STY_Sql_24hours&seqNum=25)

[Back to Syllabus](../../README.md)
