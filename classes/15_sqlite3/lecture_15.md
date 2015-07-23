# SQLite3 Databases

First off, there are a lot of different kinds of databases: SQL, MySQL, Postgres, Mongo, etc.  And because each type of database needs a different interface, there are a lot of different libraries for dealing with databases in Python. Check [here](https://wiki.python.org/moin/DatabaseInterfaces) for a nice listing of the most popular database interfaces in Python.

We are going to discuss `sqlite3` because it is the only database library that comes standard with Python. It is also pretty great, working well with reasonably small, "light" databases.

Most databases are [servers](https://en.wikipedia.org/wiki/Server_%28computing%29) or [services](https://en.wikipedia.org/wiki/Windows_service) that are run on your computer. But one of the major features of `sqlite3` is that there is no server/service, it is just a file with all the data inside. This is particularly handy for smaller databases and for databases you want to included in an application.

## Creating and Connecting to Databases

We will not covert the topic of databases in great detail, but like most databases, `sqlite3` is a [relational database](https://en.wikipedia.org/wiki/Relational_database). That is, inside the database we have tables of data organized by rows and columns. And these tables can be organized inside schemas.

![relational database model](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Relational_Model.svg/543px-Relational_Model.svg.png)

We will use the same command to open an existing database as we would use to create a new database:

    import sqlite3
    con = sqlite3.connect('secret_agents.db')

The path given can be local or absolute, but make sure this folder is editable by Python.

And it is very important to close all database connections when you are done with them:

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

You may also noticed something very strange here. What is all this "CREATE TABLE ..." gobbly gook? That's not Python code! Correct, this is note Python code. When we interact with the database we do so with a variant of the popular SQL database langauge called SQLite. You may think it is unfair to through an entirely new programming language into the mix this far into the class. But there's nothing for it. If you want to deal with databases, you need to learn to talk to them on their level.

What the above SQLite code did is pretty simple, it created a new table with three columns:

 * agentID
 * code_name
 * name

Note that it is usually a good idea to create a first column for each table that can serve as the "PRIMARY KEY". This will help you create relations between different tables, and data, later. Also notice that each column in the table has a type (INTEGER, FLOAT, TEXT, BOOL), and we can even mandate that some columns have unique values.

#### Inserting Data (INSERT)

Right now the table is empty, so let's learn how to add values. Well, there's one agent we can add:

    cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                   VALUES(?,?,?)''', (1, "007", "James Bond"))
    con.commit()

Well, we wouldn't be much of an agency with only one agent, so let's create several `INSERT` statements and commit them all.

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

#### Reverting Changings (ROLLBACK)

Let's say we made a typo working with our database:

    cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                   VALUES(?,?,?)''', (9, "009", "Evelyn Salt"))
    con.commit()

Luckily, we can revert our last `.commit()` using `.rollback()`:

    con.rollback()

Problem solved. It's like Evelyn Salt never existed.

#### Updating Tables (UPDATE)

For this exercise, let's create another table that says the status of all of our agents:

    cursor.execute('''
    CREATE TABLE status(agentID INTEGER PRIMARY KEY, status TEXT)
    ''')
    con.commit()

And fill is with data (all our agents are currently active).

    for i in xrange(1, 10):
        cursor.execute('''INSERT INTO status(agentID, status)
                      VALUES(?,?)''', (i, "Active"))
    con.commit()

Now let's say one of our secret agents dies and we want to update their status, we would use the SQL keyword `UPDATE`:

    cursor.execute('''UPDATE status SET status = ? WHERE agentID = ? ''',
                   ("Deceased", 7))
    con.commit()

Notice here we also used the SQLite keyword `WHERE`. This fun little piece of syntax allows us add a conditional case so we can set or get just certain fields in our table.

#### Deleting Data (DELETE)

Let's say we notice a mistake in the database. In this case, we only have 8 agents but there is a ninth agent listed in the `status` database. Well, if enough time has passed, we won't be able to use `.rollback()`. But we can delete any database entry we want using the `DELETE` keyword.

    cursor.execute("DELETE FROM status WHERE agentID=9")
    con.commit()

#### Querying Data (SELECT)

Databases wouldn't be very helpful if we couldn't get information out of them. The most basic way to "query" data from a database is using the `SELECT` keyword. Let's use `SELECT` to "query" all of the active agent ids from the `status` table.

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_ids = cursor.fetchall()

There are a couple of things to notice here. First of all, we used `.fetchall()` instead of `.commit()`. This is because the command we are executing in the database is returning information. This is also the reason need to have `active_agent_ids`, we need a place to store our values.

If we just wanted to get one value that the conditional criteria of our query, we could use `.fetchone()` instead of `.fetchall()`:

    cursor.execute('SELECT FROM status WHERE status="Active"')
    active_agent_id = cursor.fetchone()
    print(active_agent_id)
    # (1, "Active")

#### Removing Tables (DROP)

Sometimes we want to remove an entire table (not just a single entry like we did with `DELETE`). To remove an entire table, we use `DROP`.

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

A [Join](https://en.wikipedia.org/wiki/Join_%28SQL%29) is just a special kind of query. For instance, earlier we got a list of all the agents who are currently active. That worked fine, but we didn't get agent names, just their IDs. That's inconvenient, but we could do a slightly more complicated `SELECT` query to get their names from the other table:

    cursor.execute('SELECT code_name, name FROM agents, status WHERE ' + 
                   'agents.agentID = status.agentID and status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

Which returns:

    [(u'007', u'James Bond'), (u'001', u'Edward Donne'), (u'002', u'Bill Fairbanks'),
     (u'003', u'Jack Mason'), (u'004', u'Scarlett Papava'),
     (u'005', u'Stuart Thomas'), (u'008', u'Bill')]

The key there was that we asked for records where fields in two different tables matched: `agents.agentID = status.agentID`. This turns out to be such a powerful idea that it has it's own name, an **INNER JOIN**. And SQLite has a special keyword for this, `JOIN`, which we can use to re-write the query:

    cursor.execute('SELECT code_name, name FROM agents JOIN status ON ' +
                   'agents.agentID = status.agentID WHERE status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

There are several other kinds of joins worth learning about. An "Outer Join", for instance, is one where records from one table are kept, even if they don't met the joining criteria. For a nice introduction to joins in the Python implementation of sqlite3, look [here](http://zetcode.com/db/sqlite/joins/).

![exploits of a mom](https://imgs.xkcd.com/comics/exploits_of_a_mom.png)

## Schemas & Permissions: Secret Agents Protect their Data

 * Coming Soon

## Example Script

 * [Script](secret_agent_lecture.py) form of this lecture

## Problem Sets

 * Coming Soon

## Further Reading

 * [Tutorials Point sqlite3 tutorial](http://www.tutorialspoint.com/sqlite/sqlite_python.htm)
 * [Zet Code sqlite3 tutorial](http://zetcode.com/db/sqlitepythontutorial/)
 * [Python Central sqlite3 tutorial](http://www.pythoncentral.io/introduction-to-sqlite-in-python/)
 * [Relational Databases](https://en.wikipedia.org/wiki/Relational_database)
 * [SQLite Joins](http://zetcode.com/db/sqlite/joins/)
 * [Database Schemas](https://www.informit.com/library/content.aspx?b=STY_Sql_24hours&seqNum=25)

[Back to Syllabus](../../README.md)
