import sqlite3, json
import os.path
from os import path

conn = sqlite3.connect('/home/lluaki/Documents/Projects/PulseRateAnalysis/database/PulseRateDB.sqlite')
cur = conn.cursor()

cur.execute(' SELECT * FROM Person')
persons = cur.fetchall()
col = [ "id", "Active","Rest","Smoke","Sex","Exercise","Height","Weight", "Variation",  "IMC"]
personsJs = {}
personsJs['PersonData'] = []
personsJs['Bubbles'] = []
personsJs["Borders"] = []
personsJs["Colors"] = []

getBorder = lambda smoke: 'Black' if(smoke)  else 'White'


def getColor(v):
  color = ()
  if v >=66:
    color = ('250', '0', '0')
  elif v >= 33:
    color = ('0', '250', '0')
  elif v > 0:
    color = ('0', '0', '250')
  else:
    color = ('250', '250', '0')
  return 'rgb('+color[0]+ ','+color[1]+','+color[2]+', 0.7)'

  
for item in persons:
  variation = item[1]-item[2]
  imc = item[7]/(item[6]*item[6])
  obj = {
      col[0] : item[0],
      col[1] : item[1],
      col[2] : item[2],
      col[3] : item[3],
      col[4] : item[4],
      col[5] : item[5],
      col[6] : item[6],
      col[7] : item[7],
      col[8] : variation,
      col[9] : imc
  }
  bb = {
        'x': imc,
        'y':item[5],
        'r': variation/2.5  
  }
  
  border = getBorder(item[3])
  color = getColor(variation/item[2]*100)

  personsJs["Borders"].append(border)
  personsJs["PersonData"].append(obj)
  personsJs["Bubbles"].append(bb)

  personsJs["Colors"].append(color)

file = "/home/lluaki/Documents/Projects/PulseRateAnalysis/assets/Persons.js"
if path.exists(file):
  os.remove(file)
  
fh = open(file, 'x')
fh.write("data = ")

with fh as outfile:
  json.dump(personsJs, outfile)
