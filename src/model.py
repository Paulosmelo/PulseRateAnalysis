import sqlite3
import re

#Creating database
conn = sqlite3.connect('/home/lluaki/Documents/projects/PulseRateAnalysis/database/PulseRateDB.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Person")
cur.execute(''' CREATE TABLE Person (
  id INTEGER PRIMARY KEY,
  active INTEGER,
  rest INTEGER,
  smoke BOOLEAN,
  sex BOOLEAN,
  exercise INTEGER,
  height INTEGER,
  weight INTEGER
  )  ''')

fh = open("/home/lluaki/Documents/projects/PulseRateAnalysis/assets/Pulse.csv")

def strip(x):
  return x.strip('"')

for line in fh:
  line = line.split(',')

  if line[0] == '""': continue
  
  line = map(lambda x: int(x) if not(x.startswith('"')) else x, line)
  line = list(line)
  _id = re.findall("\d+", line[0])
  
  cur.execute(''' 
      INSERT INTO Person (id, active, rest, smoke, sex, exercise, height, weight)
      VALUES (?,?,?,?,?,?,?,?)           
  ''', (int(_id[0]), line[1], line[2], line[3], line[4], line[5], round((line[6]*2.54)/100, 2), round(line[7]/2.205)))
  conn.commit()
cur.close()