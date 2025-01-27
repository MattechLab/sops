To effectively manage and analyze MRI data, including prescan files, raw data, DICOM files, and associated physiological recordings and codes for analysis, we recommend organizing the collected dataset into the following structure:

```bash
MR-Eye/
    ├── code/
    │   ├── git_repo_specific_for_this_project/
    │   │   ├── README.md  # Add a detailed description of the repository here
    │   │   ├── [Your code files for this specific project go here]
    │   │   └── .gitignore  # Include entries to exclude commonly-used packages like Monalisa
    │
    ├── data/
    │   ├── update_protocol_description.md
    │   ├── final_fixed_protocol.md
    │   ├── subject_table.xlsx
    │   ├── pilot_/
    │   │   ├── year-month-date/
    │   │   │   ├── subject00x/
    │   │   │   │   └── [Relevant pilot subject data files]
    │   │   └── [More dated folders as needed]
    │   ├── final_protocol/
    │   │   ├── subject001/
    │   │   │   ├── mri/
    │   │   │   │   ├── dicom/
    │   │   │   │   ├── raw_data/
    │   │   │   │   ├── ismrmd/
    │   │   │   │   └── bids/  # (TBD: Decide on the structure)
    │   │   │   ├── physio/
    │   │   │   │   ├── ET/
    │   │   │   │   │   ├── **.edf
    │   │   │   │   │   ├── **.tsv.gz
    │   │   │   │   │   └── **.json
    │   │   │   │   └── twix/**.mat 
    │   │   │   └── others/
    │   │   └── [Additional subjects as needed]
    │
    ├── output/
    │   └── [Generated output files go here]
    │
    └── README.md  # Main project description with an overview, usage, and other details

```