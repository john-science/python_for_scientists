
import sqlite3


def main():
    print('Connecting to Secret Agent Database...')
    con = sqlite3.connect('secret_agents.db')
    cursor = con.cursor()

    print('\nLicense to Kill, part 1: Give out some licenses.')
    for agent in xrange(4, 10):
        cursor.execute('''INSERT INTO licenses(id, agentID, license)
               VALUES(?,?,?)''', (agent, agent, "License to Kill"))
    con.commit()

    print('\nLicense to Kill, part 2: Who has a License to Kill?')
    cursor.execute('''SELECT agentID from licenses
                   WHERE license="License to Kill"''')
    deadly_agents = cursor.fetchall()
    print([da[0] for da in deadly_agents])

    print('\nLicense to Kill, part 3: Calling all agents.')
    cursor.execute('''SELECT agentID from agents''')
    all_agents = cursor.fetchall()
    print([aa[0] for aa in all_agents])

    print("\nLicense to Kill, part 4: Who's NOT deadly?")
    not_deadly = list(set(all_agents).difference(set(deadly_agents)))
    print([nd[0] for nd in not_deadly])


    print('\nLicense to Kill, part 5: Not-Deadly agents.')
    for agent_id in not_deadly:
        cursor.execute('SELECT name from agents WHERE agentID=' + str(agent_id[0]))
        a = cursor.fetchone()
        print('\t' + a[0])

    print('\nLicense to Kill, part 6: All-in-One.')
    cursor.execute('''SELECT name from agents WHERE agentID not in
                   (SELECT agentID from licenses)''')
    undeadly = cursor.fetchall()
    for undead in undeadly:
        print('\t' + undead[0])

    print('\nMission Possible, part 1: Mission Log')
    cursor.execute('''CREATE TABLE missions(id INTEGER PRIMARY KEY,
                   agentID INTEGER, completed BOOL, mission_name)''')
    con.commit()

    print('\nMission Possible, part 2: Read the Mission File')
    f = open('top_secret_missions.csv', 'r')
    lines = f.readlines()
    f.close()

    print('\nMission Possible, part 3: Mission Loading')
    for ln in lines[1:]:
        line = ln.strip().split(',')
        cursor.execute('''INSERT INTO missions(id,agentID,completed,mission_name)
                       VALUES(?,?,?,?)''', (line[0], line[1], line[2], line[3]))
    con.commit()

    print('\nMission Possible, part 4: What missions are still active?')
    cursor.execute('SELECT mission_name from missions WHERE completed=="False"')
    active_missions = cursor.fetchall()
    for mis in active_missions:
        print('\t' + mis[0])

    print("\nThe World's Greatest Secret Agent, part 1: Selection")
    cursor.execute('SELECT agentID from missions')
    missions_by_agent = cursor.fetchall()
    missions_by_agent = [mba[0] for mba in missions_by_agent]

    print("\nThe World's Greatest Secret Agent, part 2: Counting")
    mission_count = {}
    for i in range(1, 9):
        mission_count[i] = missions_by_agent.count(i)
    print('\tAgent\tMission Count')
    for i in range(1, 9):
        print('\t' + str(i) + '\t' + str(mission_count[i]))

    print("\nThe World's Greatest Secret Agent, part 3: Names")
    cursor.execute('SELECT agentID,name from agents')
    agent_ids = cursor.fetchall()
    print(agent_ids)

    print("\nThe World's Greatest Secret Agent, part 4: Decisions")
    print('\tScarlett Papava wins!')

    print("\nThe World's Greatest Secret Agent, part 5: Advanced Grouping")
    '''
    We could do this, but it doesn't return the agent names:

    >>> cursor.execute('SELECT agentID,count(agentID) from missions GROUP BY agentID')
    <sqlite3.Cursor object at 0x7fc675ff9e30>
    >>> cursor.fetchall()
    [(1, 22), (2, 14), (3, 17), (4, 5), (5, 25), (6, 5), (8, 13)]

    So, instead, we do:
    '''
    cursor.execute('''SELECT name,count(missions.agentID) from missions JOIN agents
                   on agents.agentID==missions.agentID GROUP BY missions.agentID''')
    win_list = cursor.fetchall()
    for agent_name, win_count in win_list:
        print('\t' + agent_name + ': ' + str(win_count))
    print('\n\tScarlett Papava wins!')

    con.close()


if __name__ == '__main__':
    main()
