# OAS_wrapper
A wrapper for visualization and basic statiscal analysis of  Observed Antibody Space (OAS) data

## Functionalities

The scripts include functionality to do basic statistics and visualization of the OAS data. In addition, functions to add few relevant columns (i.e., sequence of original VDJ assignments)
Store VDJ assignments (convert fasta file to map file), and use the mapping to include new column in OAS CSV file. Do this for both heavy and light chains (V/D/J-Heavy and V/J-Light).
## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data 
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
└── src                <- Source code for use in this project.
    │
    ├── main.py    <- Makes OAS_wrapper a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py

```

--------

