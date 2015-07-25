
import sqlite3


def main():
    print('\nCreate the MI6 secret agent database.\n')
    con = sqlite3.connect('secret_agents.db')

    print('Creating a table for all of our secret agents.')
    cursor = con.cursor()
    cursor.execute('''
    CREATE TABLE agents(agentID INTEGER PRIMARY KEY, code_name TEXT, name TEXT)
    ''')
    con.commit()

    print(' - Adding James Bond to the database.')
    cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                   VALUES(?,?,?)''', (1, "007", "James Bond"))
    con.commit()

    # Our other agents
    # Only one female agent? We're really not much of an agency.
    other_agents = [("001", "Edward Donne"), ("002", "Bill Fairbanks"),
                    ("003", "Jack Mason"), ("004", "Scarlett Papava"),
                    ("005", "Stuart Thomas"), ("006", "Alec Trevelyan"),
                    ("008", "Bill")]

    print(' - Adding the rest of our agents to the database.\n')
    i = 2
    for code, name in other_agents:
        cursor.execute('''INSERT INTO agents(agentID, code_name, name)
                       VALUES(?,?,?)''', (i, code, name))
        i += 1

    con.commit()

    print('Create a new table for our agent status')
    cursor.execute('''
    CREATE TABLE status(agentID INTEGER PRIMARY KEY, status TEXT)
    ''')
    con.commit()

    print(' - Add all agents to the status table as "Active".')
    for i in xrange(1, 10):
        cursor.execute('''INSERT INTO status(agentID, status)
                       VALUES(?,?)''', (i, "Active"))
    con.commit()

    print(' - Agent Alec Trevelyan died. Change his status.')
    cursor.execute('''UPDATE status SET status = ? WHERE agentID = ? ''',
                   ("Deceased", 7))
    con.commit()

    print(' - There is no Agent #9, remove that bad data from the database.\n')
    cursor.execute("DELETE FROM status WHERE agentID=9")
    con.commit()

    print('Select all Active agents from the status table.')
    cursor.execute('SELECT agentID FROM status WHERE status="Active"')
    active_agent_ids = cursor.fetchall()
    print(len(active_agent_ids))

    print('Select the first Active agent you can find from the status table.')
    cursor.execute('SELECT agentID, status FROM status WHERE status="Active"')
    active_agent_id = cursor.fetchone()
    print(active_agent_id)

    print('\nCreate a table for the home addresses of all of our agents.')
    cursor.execute('''
    CREATE TABLE home_addresses(agentID INTEGER PRIMARY KEY, address TEXT)
    ''')
    con.commit()

    print(" - Add Bill Farbanks' address to the database.")
    cursor.execute('''INSERT INTO home_addresses(agentID, address)
                   VALUES(?,?)''',
                   (3, 'Highclere Park\nNewbury, West Berkshire RG20\n9RN'))
    con.commit()

    print(' - No one must know where our agents live, remove that table!\n')
    cursor.execute('DROP TABLE home_addresses')
    con.commit()

    print("Let's get all the Active agents from the status table, along with their name from the agents table.")
    cursor.execute('SELECT code_name, name FROM agents, status WHERE agents.agentID = status.agentID and status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

    print("\nLet's get all the Active agents from the status table, along with their name from the agents table using JOIN.")
    cursor.execute('SELECT code_name, name FROM agents JOIN status ON agents.agentID = status.agentID WHERE status.status="Active"')
    active_agents = cursor.fetchall()
    print(active_agents)

    print('\nCreating table for agent licenses')
    cursor.execute('''
    CREATE TABLE licenses(id INTEGER PRIMARY KEY, agentID INTEGER, license TEXT)
    ''')
    con.commit()

    print(' - Giving our agents some license')
    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(1, 1, "License to Kill")')
    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(2, 4, "License to Kill")')
    cursor.execute('INSERT into licenses(id, agentID, license) VALUES(3, 1, "License to Tango")')
    con.commit()

    print(' - Retrieve all of our agent licenses, along with the agent names.')
    cursor.execute('SELECT code_name,name,license FROM agents LEFT JOIN licenses on agents.agentID = licenses.agentID')
    licenses = cursor.fetchall()
    print(licenses)

    # close the database connection
    con.close()


if __name__ == '__main__':
    main()
