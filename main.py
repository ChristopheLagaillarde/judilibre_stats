# Program : tbc
# Description : This project give statistics about tbc
# Date : 30/10/22
# Author : Christophe Lagaillarde
# Version : 1.0

import json

import matplotlib
import matplotlib.pyplot as plt
import subprocess

subprocess.run(["./get_decisions.sh"])

json_data = open('judilibre.json')

data = json.load(json_data)
list_of_solution = []

for j in range(99):
    for i in range(len(data[j]['results'])):
        list_of_solution.append(data[j]['results'][i]['solution'])

count_rejet = list_of_solution.count('rejet')
count_other = list_of_solution.count('other')
count_cassation = list_of_solution.count('cassation')
count_irrecevabilite = list_of_solution.count('irrecevabilite')
count_qpcother = list_of_solution.count('qpcother')
count_renvoi = list_of_solution.count('renvoi')
count_rabat = list_of_solution.count('rabat')
count_nonlieu = list_of_solution.count('nonlieu')

dict = {
  "rejet": count_rejet,
  "other": count_other,
  "cassation": count_cassation,
  "irrecevabilite": count_irrecevabilite,
  "qpcother": count_qpcother,
  "renvoi": count_renvoi,
  "rabat": count_rabat,
  "nonlieu": count_nonlieu
}

names = list(dict.keys())
values = list(dict.values())
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
plt.bar(range(len(data[1])), values, tick_label=names)
plt.savefig('result//stats.png', bbox_inches='tight', dpi=400)



