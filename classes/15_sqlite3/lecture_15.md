# SQLite3 Databases

There are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc. And each different type of database has it's own Python library. Today we are going to discuss`sqlite3` because it is the only database library that comes standard with Python. It is particularly well suited for smaller databases. If you're interested, you can look [here](https://wiki.python.org/moin/DatabaseInterfaces) for a listing of the most popular database interfaces in Python.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. But one of the major features of `sqlite3` is that there is no server/service, the entire database is held inside one lightweight files. This is particularly handy for smaller databases and for databases you want to included in an application.

## Creating and Connecting to Databases

There are many books and entire courses covering the topic of databases. But we will not cover it in detail here. It is important to know that `sqlite3` is a [relational database](https://en.wikipedia.org/wiki/Relational_database). That is, inside the database we have tables of data organized by rows (records) and columns (attributes).

![secret agent database model](../../resources/secret_agent_db.png)

We will use the same command to open an existing database as we would use to create a new database:

    import sqlite3
    con = sqlite3.connect('secret_agents.db')

(The path given can be local or absolute.)

At the end of your work, it is important to close your database connection:

    con.close()

## Interacting with the Database

Whether you want to create, modify, or retrieve information from a sqlite3 table, the process will always be the same:

 * create a cursor
 * execute SQLite code
 * commit SQLite code

#### Creating Tables (CREATE)

For instance, if I wanted to create a table `agents` I might do:

    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE agents(agentID INTEGER PRIMARY KEY, code_name TEXT, name TEXT)
    ''')
    con.commit()

First notice that a cursor was created using `.cursor()`, we created SQLite code using `.execute()`, and we executed the code using `.commit()`.

You may also noticed something very strange here. What is all this "CREATE TABLE ..." gobbly gook? That's not Python code! Good observation; that is not Python code. When we interact with the database, we do so with a variant of the popular SQL database langauge called SQLite. It might seem unfair that now you have to learn a whole new programming language. But there's nothing for it. If you want to deal with databases, you need to learn to talk to them on their level.

What the above SQLite code did is pretty simple, it created a new table (using `CREATE TABLE` with three columns:

 * agentID
 * code_name
 * name

These columns all have types (`INTEGER`, `FLOAT`, `TEXT`, `BOOL`). And one of them is defined as the `PRIMARY KEY`. A key is a unique identifier in a table. You *can* have a table without a key column, but it's good practice to include them unless you have a very good reason not to.

#### Inserting Data (INSERT)

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

#### Updating Tables (UPDATE)

For this exercise, let's create another table that lists the status of all of our agents:

    cursor.execute('''
    CREATE TABLE status(agentID INTEGER PRIMARY KEY, status TEXT)
    ''')
    con.commit()

And fill it with data (all our agents are currently active).

    for i in xrange(1, 10):
        cursor.execute('''INSERT INTO status(agentID, status)
                      VALUES(?,?)''', (i, "Active"))
    con.commit()

Now let's say one of our secret agents dies and we want to update their status. We would do so using the SQL keyword `UPDATE`:

    cursor.execute('''UPDATE status SET status = ? WHERE agentID = ? ''',
                   ("Deceased", 7))
    con.commit()

Notice here we also used the SQLite keyword `WHERE`. This fun little piece of syntax allows us add a conditional case so we can set (or get) just certain fields in our table.

#### Deleting Data (DELETE)

Let's say we notice a mistake in the database. In this case, we only have 8 agents but there is a ninth agent listed in the `status` database. Well, if enough time has passed, we won't be able to use `.rollback()`. But we can delete any database entry we want using the `DELETE` keyword.

    cursor.execute("DELETE FROM status WHERE agentID=9")
    con.commit()

#### Querying Data (SELECT)

Databases wouldn't be very helpful if we couldn't get information out of them. The most basic way to "query" data from a database is using the `SELECT` keyword. Let's use `SELECT` to "query" all of the active agent ids from the `status` table.

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_ids = cursor.fetchall()

There are a couple of things to notice here. First of all, we used `.fetchall()` instead of `.commit()`. This is because the command we are executing in the database is returning information. The values return are always in the form of tuples, where each column is an item in the tuple. In this case, `active_agent_ids` is a list of tuples.

If we just wanted to get one value that met the conditional criteria of our query, we could use `.fetchone()` instead of `.fetchall()`:

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_id = cursor.fetchone()
    print(active_agent_id)
    # (1, "Active")

#### Removing Tables (DROP)

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

#### Joining Tables (JOIN)

A [Join](https://en.wikipedia.org/wiki/Join_%28SQL%29) is a special kind of query. For instance, earlier we got a list of all the agents who are currently active. That worked fine, but we didn't get agent names, just their IDs. That's inconvenient, but we could do a slightly more complicated `SELECT` query to get their names from the other table:

    cursor.execute('SELECT code_name, name FROM agents, status WHERE ' + 
                   'agents.agentID = status.agentID and status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

Which returns:

    [(u'007', u'James Bond'), (u'001', u'Edward Donne'), (u'002', u'Bill Fairbanks'),
     (u'003', u'Jack Mason'), (u'004', u'Scarlett Papava'),
     (u'005', u'Stuart Thomas'), (u'008', u'Bill')]

(Notice the use of `and` to make more complicated conditional statements.) The key to the above query was that we asked for records where fields in two different tables matched: `agents.agentID = status.agentID`. This turns out to be such a powerful idea that it has it's own name, an **INNER JOIN**. And SQLite has a special keyword for this, `JOIN`, which we can use to re-write the query:

    cursor.execute('SELECT code_name, name FROM agents JOIN status ON ' +
                   'agents.agentID = status.agentID WHERE status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

There are several other kinds of joins worth learning about. An "Outer Join", for instance, is one where records from one table are kept, even if they don't met the joining criteria

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

Okay, now let's peform a `LEFT JOIN` to pull out all of the licenses for our agents, along with the agent names.

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

We really need to get more of our agents up-to-date on their licensing.

For a nice overview of all the types of joins in sqlite3, check [here](http://zetcode.com/db/sqlite/joins/).

![exploits of a mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

## Example Script

 * [Script](secret_agent_lecture.py) form of this lecture

## Problem Sets

 * [Secret Agent Problem Set](problem_set_1_sqlite3.md)

## Further Reading

 * [Tutorials Point sqlite3 tutorial](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
 * [Zet Code sqlite3 tutorial](http://zetcode.com/db/sqlitepythontutorial/)
 * [Python Central sqlite3 tutorial](http://www.pythoncentral.io/introduction-to-sqlite-in-python/)
 * [Relational Databases](https://en.wikipedia.org/wiki/Relational_database)
 * [SQLite Joins](http://zetcode.com/db/sqlite/joins/)
 * [Database Schemas](https://www.informit.com/library/content.aspx?b=STY_Sql_24hours&seqNum=25)

[Back to Syllabus](../../README.md)

    con.close()
