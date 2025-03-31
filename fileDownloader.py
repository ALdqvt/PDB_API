import os
import sys
import urllib
import requests

import pandas as pd
import urllib3


def read_csv(filename, directory):
    """Reads a CSV file from the specified directory and returns the first column as a list."""
    file_path = os.path.join(directory, filename)
    full_path = os.path.abspath(file_path)

    try:
        df = pd.read_csv(full_path, header=None)
        print(f" Read CSV from: {full_path}")
        return df[0].tolist()  # Return first column as a list
    except Exception as e:
        print(f" Error reading CSV: {e}")
        return None  # Return None if reading fails


# def download_pdb(pdbcode, datadir, downloadurl="https://files.rcsb.org/download/"):
#     """
#     Downloads a PDB file from the Internet and saves it in a data directory.
#     :param pdbcode: The standard PDB ID e.g. '3ICB' or '3icb'
#     :param datadir: The directory where the downloaded file will be saved
#     :param downloadurl: The base PDB download URL, cf.
#         `https://www.rcsb.org/pages/download/http#structures` for details
#     :return: the full path to the downloaded PDB file or None if something went wrong
#     """
#     pdbfn = pdbcode + ".pdb"
#     url = downloadurl + pdbfn
#     outfnm = os.path.join(datadir, pdbfn)
#     try:
#         urllib3.request.urlretrieve(url, outfnm)
#         return outfnm
#     except Exception as err:
#         print(str(err), file=sys.stderr)
#         return None



def download_pdb(pdb_id, output_dir='/home/cat/pymol/pdbs/'):
    """
    Download a PDB file from the RCSB PDB website.

    Parameters:
    - pdb_id: str, the PDB ID of the file to download.
    - output_dir: str, the directory where the file will be saved.
    """
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = f"{output_dir}/{pdb_id}.pdb"
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {pdb_id}.pdb to {file_path}")
    else:
        print(f"Failed to download {pdb_id}.pdb")

list_eco = read_csv("eco_output.csv", "files")
list_sal = read_csv("sal_output.csv", "files")
list_lac = read_csv("lac_output.csv", "files")



for pdb_id in list_eco:
    download_pdb(pdb_id)


