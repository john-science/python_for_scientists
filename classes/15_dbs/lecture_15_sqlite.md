# SQLite3 Databases

There are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc. And each different type of database has it's own Python library. Today we are going to discuss`sqlite3` because it comes standard with Python. It is particularly well suited for smaller databases. If you're interested, you can look [here](https://wiki.python.org/moin/DatabaseInterfaces) for a listing of the most popular database interfaces in Python.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. But one of the major features of `sqlite3` is that there is no server/service, the entire database is held inside one lightweight file. This is particularly handy for smaller databases and for databases you want to package with an application.

## Creating and Connecting to Databases

There are many books and entire courses covering the topic of databases. It is very important to understand that this is just a light introduction. The purpose of this lecture is not to teach database theory, it is only to explain how to use a single Python database library.

SQLite is a [relational database](https://en.wikipedia.org/wiki/Relational_database). Broadly speaking, that means the data is arranged into tables by rows (records) and columns (attributes).

![secret agent database model](../../resources/secret_agent_db.png)

In SQLite, we will use the same command to open an existing database that we would to create a new database:

    import sqlite3
    con = sqlite3.connect('secret_agents.db')

To run almost any code against your database, you will need to create a cursor:

    cursor = con.cursor()

At the end of your work, it is important to close your database connection:

    con.close()

## Interacting with the Database

Whether you want to create, modify, or retrieve information from a `sqlite3` table, the process will always be the same:

 * connect to the database
 * create a cursor
 * execute SQLite code
 * commit SQLite code

### Creating Tables (CREATE)

For instance, if I wanted to create the `agents` table above I might do:

    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE agents(agentID INTEGER PRIMARY KEY, code_name TEXT, name TEXT)
    ''')
    con.commit()

First notice that a cursor was created using `.cursor()`, we created SQLite code using `.execute()`, and we ran the code against the database using `.commit()`.

You may also noticed something very strange. What is all this `CREATE TABLE` gobbly gook? That's not Python code! Good observation; that is not Python code. When we interact with the database, we do so with a variant of the popular SQL database langauge called SQLite. It might seem unfair that now you have to learn a whole new programming language. But there's nothing for it. If you want to deal with databases, you need to learn to talk to them on their own level.

What the above SQLite code did is pretty simple, it created a new table (using `CREATE TABLE` with three columns:

 * agentID
 * code_name
 * name

These columns all have types `INTEGER`, `FLOAT`, `TEXT`, and `BOOL`. Though there are other possibilities, like `DATETIME`, `TIMESTAMP`, `INT`, and many [more](http://mysql-python.sourceforge.net/MySQLdb-1.2.2/public/MySQLdb.constants.FIELD_TYPE-module.html). And one of them is defined as the `PRIMARY KEY`. A key is a unique identifier in a table. You *can* have a table without a key column, but it's good practice to include them unless you have a very good reason not to.

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
    
    i = 2
    for code, name in other_agents:
        cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                      VALUES(?,?,?)''', (i, code, name))
        i += 1
    
    con.commit()

Notice here that we made several `.execute()` statements before doing the `.commit()`.

### Updating Tables (UPDATE)

For this exercise, let's create another table that lists the status of all of our agents (see the diagram above):

    cursor.execute('''
    CREATE TABLE status(agentID INTEGER PRIMARY KEY, status TEXT)
    ''')
    con.commit()

And fill it with data (all our agents are currently active).

    for i in range(1, 10):
        cursor.execute('''INSERT INTO status(agentID, status)
                      VALUES(?,?)''', (i, "Active"))
    con.commit()

Now let's say one of our secret agents dies and we want to update their status. We would do so using the SQL keyword `UPDATE`:

    cursor.execute('''UPDATE status SET status = ? WHERE agentID = ? ''',
                   ("Deceased", 7))
    con.commit()

#### The Conditional Clause (WHERE)

Notice here we also used the SQL keyword `WHERE`. This fun little piece of syntax allows us add a conditional case so we can set (or get) just certain fields in our table.

### Deleting Data (DELETE)

Let's say we notice a mistake in the database. In this case, we only have 8 agents but there is a ninth agent listed in the `status` database. Well, if enough time has passed, we won't be able to use `.rollback()`. But we can delete any database entry we want using the `DELETE` keyword.

    cursor.execute("DELETE FROM status WHERE agentID=9")
    con.commit()

### Querying Data (SELECT)

Databases wouldn't be very helpful if we couldn't get information out of them. The most basic way to "query" data from a database is using the `SELECT` keyword. Let's use `SELECT` to "query" all of the active agent ids from the `status` table.

    cursor.execute('SELECT agentID,status FROM status WHERE status="Active"')
    active_agent_ids = cursor.fetchall()

There are a couple of things to notice here. First of all, we used `.fetchall()` instead of `.commit()`. This is because the command we are executing in the database is returning information. The values returned are always in the form of tuples, where each column is an item in the tuple. In this case, `active_agent_ids` is a list of tuples.

If we just wanted to get one value that met the conditional criteria of our query, we could use `.fetchone()` instead of `.fetchall()`:

    cursor.execute('SELECT agentID,status FROM status WHERE status="Active"')
    active_agent_id = cursor.fetchone()
    print(active_agent_id)
    # 1

#### The Asterisk (*)

Above, we listed all of the columns we wanted to pull from the table explicitly by saying `SELECT agentID,status FROM`.  But it is frequently the case that we will want to pull *all* the columns from a table, so there is a special syntactic sugar for that. The following two queries are exactly the same:

    cursor.execute('SELECT agentID,status FROM status WHERE status="Active"')
    cursor.execute('SELECT * FROM status WHERE status="Active"')

#### Reduce Number of Rows Returned (LIMIT)

In the above `SELECT` queries, we are returning every row in the table that matches our `WHERE` clause. This is fine here, because we only have 8 agents. But imagine if you are pulling data from a table with millions of rows. And maybe you just want to take a look at an example row to examine the data format. It would be nice to have the power to just pull a couple of rows. To do so, we use the `LIMIT` keyword:

    cursor.execute('SELECT * FROM status WHERE status="Active" LIMIT 1')
    active_agent_ids = cursor.fetchall()
    print(active_agent_ids)
    # (1, "Active")    

### Removing Tables (DROP)

Sometimes we want to remove an entire table (not just a single entry like we did with `DELETE`). To do so, use `DROP`.

First, let's create a table to delete:

    cursor.execute('''
    CREATE TABLE home_addresses(agentID INTEGER PRIMARY KEY, address TEXT)
    ''')
    con.commit()

And we can add a row to that table:

    cursor.execute('''INSERT INTO home_addresses(agentID, address)
                   VALUES(?,?)''',
                   (3, 'Highclere Park\nNewbury, West Berkshire RG20\n9RN'))
    con.commit()

Well, we probably shouldn't save the home addresses of our secret agents. If someone gets ahold of this database, they'd all be in trouble. So let's `DROP` that whole table.

    cursor.execute('''DROP TABLE home_addresses''')
    con.commit()

Done. Our agents don't exist.

![exploits of a mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

### Joining Tables (JOIN)

A [Join](https://en.wikipedia.org/wiki/Join_%28SQL%29) is a special kind of query. As the name suggests, a join query returns a combination of two tables. As you can imagine, there are a lot of ways you might want to combine two tables of data. You probably want to match at least one column in both tables, and then based on this match, return some set of columns from both tables.

The SQL language defines three types of joins: inner, cross, and outer.

#### Inner Join (JOIN)

Earlier, we created a list of all the agents who are currently active. That query worked fine, but it only returned the agent IDs, not there names. That's inconvenient, but we could do a slightly more complicated `SELECT` query to get their names from the other table:

    cursor.execute('SELECT code_name, name FROM agents, status WHERE ' + 
                   'agents.agentID = status.agentID and status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

Which returns:

    [(u'007', u'James Bond'), (u'001', u'Edward Donne'), (u'002', u'Bill Fairbanks'),
     (u'003', u'Jack Mason'), (u'004', u'Scarlett Papava'),
     (u'005', u'Stuart Thomas'), (u'008', u'Bill')]

Perfect, now we see all seven active agents. But notice the use of the `and` keyword above, it allowed us to make a much more complicated query. The key is that it allowed us to query two different tables, and match a single column in each using: `agents.agentID = status.agentID`. These kinds of queries are so common, that SQL / SQLite3 defines a special keyword to help you write them faster: `JOIN`. Using our new keyword, we would write the above query as:

    cursor.execute('SELECT code_name, name FROM agents JOIN status ON ' +
                   'agents.agentID = status.agentID WHERE status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

We could have written `INNER JOIN` here, instead of just `JOIN`. But, as it happens, the inner join is the most common type of join, so it is the default in SQLite3.

#### Cross Join (CROSS JOIN)

The `CROSS JOIN` is the least-common join, but probably the easiest to understand. It creates a combination of every record in the left table with every record in the right table. For instance, if we wanted to combine the agents and status tables, we could do:

    cursor.execute('SELECT code_name, status FROM agents CROSS JOIN status')
    big_mess = cursor.fetchall()
    print(big_mess)

This would return:

    [(u'007', u'Active'), (u'007', u'Active'), (u'007', u'Active'), (u'007', u'Active'),
     (u'007', u'Active'), (u'007', u'Active'), (u'007', u'Deceased'), (u'007', u'Active'),
     (u'001', u'Active'), (u'001', u'Active'), (u'001', u'Active'), (u'001', u'Active'),
     (u'001', u'Active'), (u'001', u'Active'), (u'001', u'Deceased'), (u'001', u'Active'),
     (u'002', u'Active'), (u'002', u'Active'), (u'002', u'Active'), (u'002', u'Active'),
     (u'002', u'Active'), (u'002', u'Active'), (u'002', u'Deceased'), (u'002', u'Active'),
     (u'003', u'Active'), (u'003', u'Active'), (u'003', u'Active'), (u'003', u'Active'),
     (u'003', u'Active'), (u'003', u'Active'), (u'003', u'Deceased'), (u'003', u'Active'),
     (u'004', u'Active'), (u'004', u'Active'), (u'004', u'Active'), (u'004', u'Active'),
     (u'004', u'Active'), (u'004', u'Active'), (u'004', u'Deceased'), (u'004', u'Active'),
     (u'005', u'Active'), (u'005', u'Active'), (u'005', u'Active'), (u'005', u'Active'),
     (u'005', u'Active'), (u'005', u'Active'), (u'005', u'Deceased'), (u'005', u'Active'),
     (u'006', u'Active'), (u'006', u'Active'), (u'006', u'Active'), (u'006', u'Active'),
     (u'006', u'Active'), (u'006', u'Active'), (u'006', u'Deceased'), (u'006', u'Active'),
     (u'008', u'Active'), (u'008', u'Active'), (u'008', u'Active'), (u'008', u'Active'),
     (u'008', u'Active'), (u'008', u'Active'), (u'008', u'Deceased'), (u'008', u'Active')]

Of course, in this case, the result of the cross join is not very meaningful. As you can imagine, if both left and right tables get large, the `CROSS JOIN` can produce absurdly large outputs. BUT, it is one of the standard tools of SQL. Maybe you'll find a good use for it one day.

#### Outer Join (OUTER JOIN)

Finally, we have the `OUTER JOIN`. The SQL language, actually defines three types of `OUTER JOIN`: `LEFT`, `RIGHT`, and `FULL`, but SQLite only supports the `LEFT` variety. In any case, a "LEFT" `OUTER JOIN` in SQLite3 is one where the records from two tables are matched, but all the records in the left table are kept, even if they found no match in the right table.

In order to test this out, let's make a new table to keep the licenses of our agents:

    cursor.execute('''
    CREATE TABLE licenses(id INTEGER PRIMARY KEY, agentID INTEGER, license TEXT)
    ''')
    con.commit()

And let's add some data to the table:

    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(1, 1, "License to Kill")')
    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(2, 4, "License to Kill")')
    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(3, 1, "License to Tango")')
    cursor.commit()

Now let's peform a `LEFT JOIN` to pull out all of the licenses for our agents, along with the agent names.

    print(' - Retrieve all of our agent licenses, along with the agent names.')
    cursor.execute('SELECT code_name,name,license FROM agents LEFT JOIN' +
                   'licenses on agents.agentID = licenses.agentID')
    licenses = cursor.fetchall()
    print(licenses)

And we get back a full listing of our agent licenses:

    [('007', 'James Bond', 'License to Kill'), ('007', 'James Bond', 'License to Tango'),
     ('001', 'Edward Donne', None), ('002', 'Bill Fairbanks', None),
     ('003', 'Jack Mason', 'License to Kill'), ('004', 'Scarlett Papava', None),
     ('005', 'Stuart Thomas', None), ('006', 'Alec Trevelyan', None),
     ('008', 'Bill', None), ('009', 'Evelyn Salt', None)]

We really need to get more of our agents up-to-date on their licenses.

For a nice overview of all the types of joins in sqlite3, check [here](http://zetcode.com/db/sqlite/joins/).


### GROUP BY

The word `GROUP BY` allows you to group the results by one of three parameters:

* `col_name` - The name of one of the table columns
* `expr` - A regular expression
* `position` - A position in the table

You can also have SQLite return the grouped result in `ASC`cending or `DESC`ending order. And you can create a final line at the end that summarizes the previous lines using `WITH ROLLUP`. All of these together give us a generic `GROUP BY` statement that looks like:

    GROUP BY (col_name | expr | position) (ASC | DESC) (WITH ROLLUP)

For instance, we could select the different types of fish available in our table by:

    cursor.execute('SELECT * FROM licenses GROUP BY license')
    cursor.fetchall()

And it will return something like:

    [(1, 1, "License to Kill"),
     (3, 1, "License to Tango")]

Notice that though there are two rows with "License to Kill" in our `licenses` table, only one is returned by the `GROUP BY` query.


### ORDER BY

The clause `ORDER BY` sorts the results of a query, taking almost the same options as `GROUP BY`:

    ORDER BY (col_name | expr | position) (ASC | DESC)

For instance:

    cursor.execute("SELECT * from agents ORDER BY name ASC")
    cursor.fetchall()

The query would return:

    [(7, "006", "Alec Trevelyan"),
     (8, "008", "Bill"),
     (3, "002", "Bill Fairbanks"),
     (1, "001", "Edward Donne"),
     (4, "003", "Jack Mason"),
     (2, "007", "James Bond"),
     (5, "004", "Scarlett Papava"),
     (6, "005", "Stuart Thomas")]


## Example Script

 * [Script](secret_agent_lecture_sqlite3.py) form of this lecture

## Problem Sets

 * [Secret Agent Problem Set](problem_set_1.md)

## Further Reading

 * [Tutorials Point sqlite3 tutorial](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
 * [Zet Code sqlite3 tutorial](http://zetcode.com/db/sqlitepythontutorial/)
 * [Python Central sqlite3 tutorial](http://www.pythoncentral.io/introduction-to-sqlite-in-python/)
 * [Relational Databases](https://en.wikipedia.org/wiki/Relational_database)
 * [SQLite Joins](http://zetcode.com/db/sqlite/joins/)
 * [Database Schemas](https://www.informit.com/library/content.aspx?b=STY_Sql_24hours&seqNum=25)
 * [PostgreSQL vs MySQL vs SQLite](http://hyperpolyglot.org/db)

[Back to Syllabus](../../README.md)

    con.close()

![XKCD Query Comic](https://imgs.xkcd.com/comics/query.png)
