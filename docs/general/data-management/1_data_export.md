### Collect ET data 
Copy data from the subfolder of PsychoPy program into the hard drive.

!!! tip 
    The subfolder should include the files for one session with the formats like 

    - `000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.EDF` 
    - `000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.csv` 
    - `000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.log`
    
    where '**.EDF' files are eye tracking records, `.csv` and `.log` files logs the task messages and the corresponding timestamps."


### Collect MRI raw data
**Export Twix raw data**
- Twix: Username: medadmin, Password: adm$pwd$4$med$.
- Press `Ctrl+Esc` to open the IDE terminal.
- In the IDE terminal: ideacmdtool -> type `4` -> type `6` //
- Type `Twix` and the Twix data browser opens.
- Select the data you want to copy, right click on the mouse -> Copy Total RAID file -> select destination (your hard drive).
-  The only useful thing is the physio [select the flag on External Signal] <mark>need more explanation </mark>
  
**Export the DICOM data (directly reconstructed images from the scanner)**
- Login as SuperUser by pressing `Tab` + `Delete` + `(Bottone a DX - 9)` to enter the advance mode.
- Export DICOM: select the patient, go to export // File System // Browse -> select `HD`.
- Select the “Enhanced” option (1 DICOM  / volume) instead of Interoperability (1 DICOM / slice).
!!! warning "The default option is `Interoperability`! So we have to change it manually!"