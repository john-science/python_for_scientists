# MySQL Databases

There are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc. And each different type of database has it's own Python library. In this lecture we will look at MySQL databases using the `MySQLdb` library. MySQL is one of the most popular database choices for medium-sized projects today, and it is open-source. If you're interested, you can look [here](https://wiki.python.org/moin/DatabaseInterfaces) for a listing of the most popular database interfaces in Python.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. And that is no different for MySQL, look [here](http://dev.mysql.com/doc/refman/5.7/en/installing.html) for instructions on installing and starting a MySQL server on your computer. You will also need to install the `mysql-python` library. If you are using Anaconda, this should be as easy as:

    conda install mysql-python


## Creating and Connecting to Databases

There are many books and entire courses covering the topic of databases. It is very important to understand that this is just a light introduction. The purpose of this lecture is not to teach database theory, it is only to explain how to use a single Python database library.

MySQL is a [relational database](https://en.wikipedia.org/wiki/Relational_database). Broadly speaking, that means the data is arranged into tables by rows (records) and columns (attributes).

![secret agent database model](../../resources/secret_agent_db.png)

In MySQL, to create a connection to our database server, we need to use our credentials:

    import MySQLdb
    con = MySQLdb.connect(host='localhost', user='my_user_name', passwd='my_secret')

Note that you don't actually need to write `host=` or `user=`, these items are always in the same order. For now, we will write them explicitly, until they become more familiar.

To run almost any code against your database, you will need to create a cursor:

    cursor = con.cursor()

At the end of your work, it is important to close your database server connection:

    con.close()

## Interacting with the Database

Whether you want to create, modify, or retrieve information from a `MySQL` table, the process will always be the same:

 * connect to the database
 * create a cursor
 * execute MySQLdb code

### Creating Databases (CREATE DATABASE)

We want to create the database shown in the diagram above. To do that, we need to create our database connection, create a cursor, and run our first query against the database:

    import MySQLdb
    con = MySQLdb.connect(host='localhost', user='my_user_name', passwd='my_secret')
    cursor = con.cursor()
    cursor.execute('CREATE DATABASE `secret_agents`;')
    cursor.execute('USE secret_agents';)

The `CREATE` command is clear, but the `USE` command is not so obvious. We can `CREATE` as many databases as we want, but in order to go inside that database and interact with it, we need to execute a `USE` command first. And later, if we want to interact with a different database, we will execute another `USE` command.

### Creating Tables (CREATE TABLE)

For instance, if I wanted to create the `agents` table above I might do:

    cursor = con.cursor()
    cursor.execute('''CREATE TABLE `agents` (
                        `agentID` int(11) NOT NULL auto_increment,
                        `code_name` varchar(3) NOT NULL default '007',
                        `name` varchar(30) NOT NULL default 'James Bond',
                        PRIMARY KEY (`agentID`))
                   ''')

First notice that a cursor was created using `.cursor()`, we created SQLite code using `.execute()`, and we ran the code against the database using `.commit()`.

You may also noticed something very strange. What is all this `CREATE TABLE` gobbly gook? That's not Python code! Good observation; that is not Python code. When we interact with the database, we do so with a variant of the popular SQL database langauge called MySQLdb. It might seem unfair that now you have to learn a whole new programming language. But there's nothing for it. If you want to deal with databases, you need to learn to talk to them on their own level.

What the above MySQLdb code did is pretty simple, it created a new table (using `CREATE TABLE` with three columns:

 * agentID
 * code_name
 * name

These columns all have types `INT` and `VARCHAR`. Though there are other possibilities, like `DATETIME`, `TIMESTAMP`, `INT`, and many [more](http://mysql-python.sourceforge.net/MySQLdb-1.2.2/public/MySQLdb.constants.FIELD_TYPE-module.html). And one of them is defined as the `PRIMARY KEY`. A key is a unique identifier in a table. You *can* have a table without a key column, but it's good practice to include them unless you have a very good reason not to.

### Inserting Data (INSERT)

Right now the table is empty, so let's add values using `INSERT`. There's obviously one agent we can add:

    cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                   VALUES(?,?,?)''', (1, "007", "James Bond"))
    con.commit()

But we wouldn't be much of an agency with only one agent, so let's create several `INSERT` statements and commit them all:

    # Only one female agent? We're really not much of an agency.
    other_agents = [("001", "Edward Donne"), ("002", "Bill Fairbanks"),
                    ("003", "Jack Mason"), ("004", "Scarlett Papava"),
                    ("005", "Stuart Thomas"), ("006", "Alec Trevelyan"),
                    ("008", "Bill")]

    cursor.executemany('''INSERT INTO agents(agentID, code_name, name)
                       VALUES(?,?,?)''', other_agents)

Notice here that we made several `.execute()` statements at once by passing a list as a secondary argument to `.executemany()`.


### Updating Tables (UPDATE)

For this exercise, let's create another table that lists the status of all of our agents (see the diagram above):

    cursor.execute('''CREATE TABLE `status` (
                        `agentID` int(11) NOT NULL auto_increment,
                        `status` varchar(30) NOT NULL default 'Inactive',
                        PRIMARY KEY (`agentID`))
                   ''')

And fill it with data (all our agents are currently active).

    for i in xrange(1, 10):
        cursor.execute('''INSERT INTO status(agentID, status)
                      VALUES(?,?)''', (i, "Active"))

Now let's say one of our secret agents dies and we want to update their status. We would do so using the SQL keyword `UPDATE`:

    cursor.execute('''UPDATE status SET status = ? WHERE agentID = ? ''',
                   ("Deceased", 7))

Notice here we also used the MySQL keyword `WHERE`. This fun little piece of syntax allows us add a conditional case so we can set (or get) just certain fields in our table.

### Deleting Data (DELETE)

Let's say we notice a mistake in the database. In this case, we only have 8 agents but there is a ninth agent listed in the `status` database. Well, if enough time has passed, we won't be able to use `.rollback()`. But we can delete any database entry we want using the `DELETE` keyword.

    cursor.execute("DELETE FROM status WHERE agentID=9")

### Querying Data (SELECT)

Databases wouldn't be very helpful if we couldn't get information out of them. The most basic way to "query" data from a database is using the `SELECT` keyword. Let's use `SELECT` to "query" all of the active agent ids from the `status` table.

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_ids = cursor.fetchall()

There are a couple of things to notice here. First of all, we used `.fetchall()`, because the command we are executing in the database is returning information. The values returned are always in the form of tuples, where each column is an item in the tuple. In this case, `active_agent_ids` is a list of tuples.

If we just wanted to get one value that met the conditional criteria of our query, we could use `.fetchone()` instead of `.fetchall()`:

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_id = cursor.fetchone()
    print(active_agent_id)
    # (1, "Active")

### Removing Tables (DROP)

Sometimes we want to remove an entire table (not just a single entry like we did with `DELETE`). To do so, use `DROP`.

First, let's create a table to delete:

    cursor.execute('''CREATE TABLE `home_addresses` (
                        `agentID` int(11) NOT NULL auto_increment,
                        `address` varchar(90) NOT NULL default '',
                        PRIMARY KEY (`agentID`))
                   ''')

And we can add a row to that table:

    cursor.execute('''INSERT INTO home_addresses(agentID, address)
                   VALUES(?,?)''',
                   (3, 'Highclere Park\nNewbury, West Berkshire RG20\n9RN'))

Well, we probably shouldn't save the home addresses of our secret agents. If someone gets ahold of this database, they'd all be in trouble. So let's `DROP` that whole table.

    cursor.execute('''DROP TABLE home_addresses''')

Done. Our agents don't exist.

![exploits of a mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)


### Joining Tables (JOIN)

A [Join](https://en.wikipedia.org/wiki/Join_%28SQL%29) is a special kind of query. As the name suggests, a join query returns a combination of two tables. As you can imagine, there are a lot of ways you might want to combine two tables of data. You probably want to match at least one column in both tables, and then based on this match, return some set of columns from both tables.

The SQL language defines three types of joins: inner, cross, and outer.

#### Inner Join (JOIN)

TODO

#### Cross Join (CROSS JOIN)

TODO

#### Left Outer Join (LEFT OUTER JOIN)

TODO

#### Right Outer Join (RIGHT OUTER JOIN)

TODO

#### asterisk (*)

In the above query, we used the `*` symbol to say we wanted "all the columns" from that table. But there were three other major options:

    SELECT ALL FROM fish;  # same as `*`
    SELECT DISTINCT FROM fish;  # sort the results set into unique values
    SELECT DISTINCTROW FROM fish;  # make sure the entire column is unique

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

## Example Script

 * TODO form of this lecture

## Problem Sets

 * TODO

## Further Reading

 * [The MySQL Language](https://www.tutorialspoint.com/mysql/index.htm)

[Back to Syllabus](../../README.md)

    con.close()
