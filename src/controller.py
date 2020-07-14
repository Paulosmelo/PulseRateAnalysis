import sqlite3, json

conn = sqlite3.connect('/home/lluaki/Documents/projects/PulseRateAnalysis/database/PulseRateDB.sqlite')
cur = conn.cursor()

cur.execute(' SELECT * FROM Person')
persons = cur.fetchall()
col = ["id", "Active","Rest","Smoke","Sex","Exercise","Height","Weight", "Variation"]
personsJs = {}
personsJs['Person'] = []

for item in persons:
  obj = {
      col[0] : item[0],
      col[1] : item[1],
      col[2] : item[2],
      col[3] : item[3],
      col[4] : item[4],
      col[5] : item[6],
      col[7] : item[7],
      col[8] : round(item[8])
  }
  personsJs['Person'].append(obj)

file = "/home/lluaki/Documents/projects/PulseRateAnalysis/assets/Persons.json"

with open(file, 'x') as outfile:
  json.dump(personsJs, outfile)
  
print(personsJs)