# OAS_wrapper
A wrapper for visualization and basic statiscal analysis of  Observed Antibody Space (OAS) data

## Functionalities

The scripts include functionality to do basic statistics and visualization of the OAS data. 

# Column summaries:
column_summary.py -> Given OAS dataset as input, the function provides basic statistics on the unique and total counts of a column of interest.

```
# Usage:
summary_table = column_summary("observed_antibody_space.csv", ["Antibody_ID", "Antigen_Name", "Binding_Affinity"])
print(summary_table)
```
# Length distributions:
plot_string_length_distribution.py -> Given OAS dataset as input, the function provides basic visualization plots of length distributions of different fields e.g., V, D, J, FWR1-FWR4, CDR1-CDR3 etc.

```
# Usage: 
plot_string_length_distribution("observed_antibody_space.csv", ["Antibody_ID", "Antigen_Name", "Binding_Affinity"])
```


tabulate_query_sequence.py -> Given query sequence and IMGT database, the V/D/J sequences along with other relevant information is obtained for the query sequence. 

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data 
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
└── src                <- Source code for use in this project.
```

--------

