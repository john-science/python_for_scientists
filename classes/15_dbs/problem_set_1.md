# Intro to Databases - Problem Set

### Create and Import the Database

#### SQLite

1. The first step is to create the database we built in the lectures. The easiest way to do this would be to download [this](https://github.com/theJollySin/python_for_scientists/blob/master/classes/15_sqlite3/secret_agent_lecture_sqlite3.py) Python script and run it. It will create the database and everything in it. (Another option is to go through the lecture by hand, and write out all the queries yourself, this would take more time but be a useful learning practice.)

2. WARNING: Python will only be able to edit a database file if the file and/or the folder it is in have general write permissions. If you are on a Mac/Linux computer, all you have to do is "chmod 777". If you are on a Windows computer, simply right-click the file and navigate through the menus to add write permissions.

#### Other Database Libraries

Make sure you have a database server up and running and you have permissions to work in it.

### License to Kill

1. Use `INSERT` to add a "License to Kill" for agentIDs 4, 5, 6, 7, 8, and 9 to the `license` table.
2. Use `SELECT` to create a list of all agents (by agentID) who have a "License to Kill" in the `license` table.
3. Use `SELECT` to create a list of all agentIDs from the `agents` table.
4. Using the list generated in parts `2` and `3` above, find a list of all agents (by agentID) who do NOT have a License to Kill.
5. Use `SELECT` and the list generated in part `4` above to create a list of actual agent names for all the agents who don't have a License to Kill.
6. **NEW MATERIAL**: Repeat all of the logic in parts `1` through `5` above using a single query. (HINT: You can use `in` and `not in` to compare the results of two queries, and you can compare queries by putting them in paranthesis.)

### Mission Possible

1. `CREATE` a `TABLE` named `missions`, with four columsns: id (an integer primary key), agentID (an integer), completed (a boolean), and mission_name (a text field).
2. Read the CSV file [top_secret_missions](top_secret_missions.csv] into a list.
3. Loop through each line (except the header) in your CSV list, and use `INSERT` to add a row to the `missions` table for each line.
4. Use a `SELECT` query with a `WHERE` conditional statement to select all the mission names that are not yet completed.

### The World's Greatest Secret Agent

Our secret agents are notoriously competitive. They always arguing about who's the best secret agent in the world. How macho. We'll decide by counting who has completed the most missions.

1. `SELECT` just the agentIDs from the `missions` table.
2. Use the list method `.count()` to count how many missions each of the 8 agents have been on.
3. `SELECT` the agent names and IDs from the `agents` table.
4. Decide which agent wins.
5. **NEW MATERIAL**: `GROUP BY` is a SQL keyword that allows you to do the same type of counting you did in part `2`. (Look [here](http://www.tutorialspoint.com/sqlite/sqlite_group_by.htm) to learn more about the `GROUP BY` keyword. Use `GROUP BY` and `JOIN` to perform parts `1` through `4` with a single query.

## Solutions

 * [Solutions - SQLite](problem_set_1_solutions_sqlite.py)

Back to Lecture - [MySQL](lecture_15_mysql.md) - [PostgreSQL](lecture_15_postgres.md) - [SQLite](lecture_15_sqlite.md)
