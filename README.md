# OAS_wrapper
A wrapper to parse Observed Antibody Space (OAS) data for better visualization, annotation and comparison of sequence to germline.

## Functionalities

The scripts include functionalities to:
1. Provide basic metrics and visualizations of sequences and their annotations
2. Provide original IMGT sequences for V, D and J calls made in OAS data using IMGT reference database
3. Align sequence and germline to highlight regions of mismatches, providing positional information e.g.,  
```
   Row 1:  
Original Sequence 1: ATGCCGT  
Original Sequence 2: ATGTCGT  
Aligned and Highlighted Differences:  
ATGC[RED]C[/RED]GT  
ATG[RED]T[/RED]CGT  
Indices of Differences: [3]  
Mapped Regions: [(3, 'CDR2')]  
--------------------------------------------------
```
5. Group data by germline, to infer sequences that originate from germline, including providing information on V, D and J annotations
   
7. Annotate sequence with CDRs and FWRs for easy inference of regions of interest
```
   Row 1:  
Original Sequence: ATGCCGTAACTG  
Annotated Sequence: A(Unannotated)T(CDR1)GC(FWR1)GT(CDR2)AA(FWR2)CT(CDR3)G(Unannotated)  
--------------------------------------------------  
Row 2:  
Original Sequence: GATTACAGTGCTA  
Annotated Sequence: GAT(CDR1)TAC(FWR1)AG(CDR2)TG(FWR2)CTA(CDR3)  
--------------------------------------------------  
```

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data 
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
└── src                <- Source code for use in this project.
```

--------

