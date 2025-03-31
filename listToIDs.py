import os
import csv
import pandas as pd
from rcsbapi.search import AttributeQuery, TextQuery
from rcsbapi.search import search_attributes as attrs


a = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaEco.xlsx")
b = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaSal.xlsx")
c = pd.read_excel("/home/turtle/PycharmProjects/PythonProject/files/ProteinlistaLac.xlsx")

listEco = a.iloc[:,1].tolist()
listSal = b.iloc[:,1].tolist()
listLac = c.iloc[:,1].tolist()
rId_list = []

for val in listLac:
    q1 = TextQuery(value=val)

    #q2 = AttributeQuery(
    #    attribute= "rcsb_entity_source_organism.common_name",
    #    operator= "contains_phrase",
    #    value="Salmonella",
    #)

    query = q1
    for rId in query():
        rId_list.append(rId)

with open ("files/lac_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["PDB-ID"])
    for rId in rId_list:
        writer.writerow([rId])

print(f"Sparade{len(rId_list)}")

print(rId_list)
print("done")

