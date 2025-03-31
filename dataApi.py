#DATA API
import os
import csv
from Bio import PDB


def read_pdb_ids_csv(csv_file):
    pdb_ids = []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pdb_ids.append(row[PDB_ID])
    except Exception as e:
        print("Fel vid inläsning av CSV-filen: {e}")
    return pdb_ids

csv_file = 'sal.csv'
# pdb_ids = read_pdb_ids_from_csv(csv_file)

output_dir = "pdb_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)