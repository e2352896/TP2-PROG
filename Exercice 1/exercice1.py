import json
import csv


fichiercsv = 'resultat.csv'

with open('data.json','r') as jsone,open(fichiercsv,'w',newline='') as csve:
    donnees = json.load(jsone)
    ecriture = csv.writer(csve)
    ecriture.writerow(['reel', 'imaginaire'])
    for nombre in donnees:
        ecriture.writerow(nombre)
