import pandas as pd
from rdkit import Chem

# Load the dataset from CSV
dataset_path = "data/dataset_HTN.csv"  
output_path = "data/HTNwithSMILES.csv"  

df = pd.read_csv(dataset_path)

# Extract drug names from the dataset
drug_names = df['drug_name'].tolist()

# Define a dictionary to store drug names and their corresponding SMILES
drug_smiles = {}

# Iterate over drug names and generate SMILES
for drug_name in drug_names:
    mol = Chem.MolFromSmiles(drug_name)
    if mol:
        drug_smiles[drug_name] = Chem.MolToSmiles(mol)

# Write drug names and their corresponding SMILES to an output file
with open(output_path, 'w') as f:
    f.write("Drug Name,SMILES\n")
    for drug_name, smiles in drug_smiles.items():
        f.write(f"{drug_name},{smiles}\n")

print(f"SMILES representations have been written to {output_path}.")
