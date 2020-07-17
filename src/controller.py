import sqlite3, json
import os.path
from os import path

conn = sqlite3.connect('/home/lluaki/Documents/projects/PulseRateAnalysis/database/PulseRateDB.sqlite')
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
maxImc = lambda imc: 60 if(imc >= 60)  else imc

def getColor(imc, sex):
  perc = maxImc(imc)/60
  if sex:
    return ( 50-(50*perc), 50-(50*perc), 250-(100*perc))
  else:
    return (250-(100*perc), 50-(50*perc), 50-(50*perc))

  
for item in persons:
  variation = (item[1]-item[2])/item[2]*100
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
        'y': item[5],
        'r': round(variation)/2      
  }
  border = getBorder(item[3])
  color = getColor(imc, item[4])
  

  personsJs["Borders"].append(border)
  personsJs["PersonData"].append(obj)
  personsJs["Bubbles"].append(bb)
  personsJs["Colors"].append('rgb('+ str(color[0])+ ','+ str(color[1])+','+str(color[2])+', 0.4)')

file = "/home/lluaki/Documents/projects/PulseRateAnalysis/assets/Persons.js"
if path.exists(file):
  os.remove(file)
  
fh = open(file, 'x')
fh.write("data = ")

with fh as outfile:
  json.dump(personsJs, outfile)
