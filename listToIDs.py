import os
import csv
import pandas as pd
from rcsbapi.search import AttributeQuery, TextQuery
from rcsbapi.search import search_attributes as attrs

# Read lists of molecule/protein names and put them in lists
a = pd.read_excel("/home/cat/PycharmProjects/PDB_API/files/ProteinlistaEco.xlsx")
b = pd.read_excel("/home/cat/PycharmProjects/PDB_API/files/ProteinlistaSal.xlsx")
c = pd.read_excel("/home/cat/PycharmProjects/PDB_API/files/ProteinlistaLac.xlsx")
listEco = a.iloc[:,1].tolist()
listSal = b.iloc[:,1].tolist()
listLac = c.iloc[:,1].tolist()



##### E COLI #####
#Empty rId_list for input of new rIds
rId_list = []

for pdbID in listEco:
    q1 = TextQuery(value=pdbID)

    q2 = TextQuery(value="Escherichia Coli")

    query = q1 & q2
    for rId in query():
        if rId not in rId_list:
            rId_list.append(rId)

with open ("files/eco_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["PDB-ID"])
    for rId in rId_list:
        writer.writerow([rId])

print(f"Sparade{len(rId_list)}")
print(rId_list)
print("done")


##### SALMONELLA #####

#Empty rId_list for input of new rIds
rId_list = []

for pdbID in listSal:
    q1 = TextQuery(value=pdbID)

    q2 = TextQuery(value="Salmonella")

    query = q1 & q2
    for rId in query():
        if rId not in rId_list:
            rId_list.append(rId)

with open ("files/sal_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["PDB-ID"])
    for rId in rId_list:
        writer.writerow([rId])

print(f"Sparade{len(rId_list)}")
print(rId_list)
print("done")


##### LACTOBACILLUS #####

#Empty rId_list for input of new rIds
rId_list = []

for pdbID in listLac:
    q1 = TextQuery(value=pdbID)

    q2 = TextQuery(value="Lactobacillus")

    query = q1 & q2
    for rId in query():
        if rId not in rId_list:
            rId_list.append(rId)

with open ("files/lac_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["PDB-ID"])
    for rId in rId_list:
        writer.writerow([rId])

print(f"Sparade{len(rId_list)}")
print(rId_list)
print("done")


