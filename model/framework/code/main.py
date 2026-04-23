# imports
import os
import csv
import sys

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
from models import RNNLM

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

model_path = os.path.join(root, "..", "..", "checkpoints")
model_config_file = os.path.join(model_path, 'config.yaml')
model = RNNLM.load_model(model_path, "cpu")

scores = []
for smiles in smiles_list:
    try:
        score = model.test(smiles)
    except Exception:
        score = None
    scores += [score]

outputs = [float(s) if s is not None else None for s in scores]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["druglikeness_score"])  # header
    for o in outputs:
        writer.writerow(["" if o is None else o])