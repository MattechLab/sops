The data workflow can be divided into two parts: (figure is editing)
https://docs.google.com/drawings/d/1J4RUVk647YXuAsq7B-6wf6nKiEy5rKnjl5h4MKooOrw/edit

- MRI data. The raw MRI data should be first stored on the HES-SO server. 
    - We recommend to convert the raw MRI data to BIDS. Since from there, the BIDS compliant data can be quality controlled and pre-processed using the corresponding packages (e.g. MRIQC, fMRIPrep, dMRIPrep) to allow computation of analysis-grade derivatives (e.g. functional or structural connectivity). 
    - <mark> The code snippets for converting MRI raw data into BIDS</mark>
- Eye tracking data. The eye tracking data is automatically generated and store in the PsychoPy laptop. We should store the edf data in the folder of the MRI dataset.

- Twix physio data. If we need to extract the physio information from the raw data, we should also store the physio data in the subfolder `Twix` inside the dataset folder.
  
- Example folder structure should be followed as below:

```
MREye_Track
├── Twix
├── EDF
└── MRI_folders
    ├── subject001
    ├── subject002
    └── subject003
```