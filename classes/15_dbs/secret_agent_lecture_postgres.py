
import pg


def main():
    print('\nCreate the MI6 secret agent database.\n')
    con = pg.connect(dbname='secret_agents', port=5432)

    print('Creating a table for all of our secret agents.')
    con.query('''DROP TABLE IF EXISTS agents''')
    con.query('''
    CREATE TABLE agents(agentID INTEGER PRIMARY KEY, code_name TEXT, name TEXT)
    ''')

    print(' - Adding James Bond to the database.')
    con.query('''INSERT INTO agents(agentID, code_name, name)
              VALUES('%s', '%s', '%s')''' % (1, "007", "James Bond"))

    # Our other agents
    # Only one female agent? We're really not much of an agency.
    other_agents = [("001", "Edward Donne"), ("002", "Bill Fairbanks"),
                    ("003", "Jack Mason"), ("004", "Scarlett Papava"),
                    ("005", "Stuart Thomas"), ("006", "Alec Trevelyan"),
                    ("008", "Bill")]

    print(' - Adding the rest of our agents to the database.\n')
    i = 2
    for code, name in other_agents:
        con.query('''INSERT INTO agents(agentID, code_name, name)
                  VALUES('%s', '%s', '%s')''' % (i, code, name))
        i += 1

    print('Create a new table for our agent status')
    con.query('''DROP TABLE IF EXISTS status''')
    con.query('''CREATE TABLE status(agentID INTEGER PRIMARY KEY, status TEXT)''')

    print(' - Add all agents to the status table as "Active".')
    for i in xrange(1, 10):
        con.query('''INSERT INTO status(agentID, status)
                  VALUES('%s', '%s')''' % (i, "Active"))

    print(' - Agent Alec Trevelyan died. Change his status.')
    con.query('''UPDATE status SET status = '%s' WHERE agentID = '%s' ''' %
              ("Deceased", 7))

    print(' - There is no Agent #9, remove that bad data from the database.\n')
    con.query("DELETE FROM status WHERE agentID=9")

    print('Select all Active agents from the status table.')
    active_agent_ids = con.query("SELECT agentID FROM status WHERE status='Active'").getresult()
    print(len(active_agent_ids))

    print('Select the first Active agent you can find from the status table.')
    active_agent_id = con.query("SELECT agentID, status FROM status WHERE status='Active'").getresult()[0]
    print(active_agent_id)

    print('\nCreate a table for the home addresses of all of our agents.')
    con.query('''DROP TABLE IF EXISTS home_addresses''')
    con.query('''CREATE TABLE home_addresses(agentID INTEGER PRIMARY KEY, address TEXT)''')

    print(" - Add Bill Farbanks' address to the database.")
    con.query('''INSERT INTO home_addresses(agentID, address)
              VALUES('%s', '%s')''' %
              (3, 'Highclere Park\nNewbury, West Berkshire RG20\n9RN'))

    print(' - No one must know where our agents live, remove that table!\n')
    con.query('DROP TABLE home_addresses')

    print("Let's get all the Active agents from the status table, along with their name from the agents table.")
    active_agents = con.query("SELECT code_name, name FROM agents, status WHERE agents.agentID = status.agentID and status.status='Active'").getresult()
    print(active_agents)

    print("\nLet's get all the Active agents from the status table, along with their name from the agents table using JOIN.")
    active_agents = con.query("SELECT code_name, name FROM agents JOIN status ON agents.agentID = status.agentID WHERE status.status='Active'").getresult()
    print(active_agents)

    print('\nCreating table for agent licenses')
    con.query('''DROP TABLE IF EXISTS licenses''')
    con.query('''CREATE TABLE licenses(id INTEGER PRIMARY KEY, agentID INTEGER, license TEXT)''')

    print(' - Giving our agents some license')
    con.query("INSERT into licenses(id, agentID, license) VALUES(1, 1, 'License to Kill')")
    con.query("INSERT into licenses(id, agentID, license) VALUES(2, 4, 'License to Kill')")
    con.query("INSERT into licenses(id, agentID, license) VALUES(3, 1, 'License to Tango')")

    print(' - Retrieve all of our agent licenses, along with the agent names.')
    licenses = con.query('SELECT code_name,name,license FROM agents LEFT JOIN licenses on agents.agentID = licenses.agentID').getresult()
    print(licenses)

    print(' - Retrieve all the possible licenses we have given to agents; grouped together.')
    licenses = con.query('SELECT licenses FROM licenses GROUP BY licenses').getresult()
    print(licenses)

    print(' - Retrieve all agents, sorted by their names.')
    agents = con.query("SELECT * from agents ORDER BY name ASC").getresult()
    print(agents)

    # close the database connection
    print('')
    con.close()


if __name__ == '__main__':
    main()
