import json
import pandas as pd

data_unit_file = "SRR5060321_Heavy_Bulk.csv.gz"

metadata = ','.join(pd.read_csv(data_unit_file, nrows=0).columns)
metadata = json.loads(metadata)

sequences = pd.read_csv(data_unit_file, header=1)