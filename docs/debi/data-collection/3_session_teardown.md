### Session Tear-Down

#### Showing the Participant Out

- Enter the scanner room, and announce yourself to the participant saying that you will get out the participant in a few seconds.
- Extract the participant by pressing the extraction button and then gently rolling the central knob. Alternatively, you can just press the Home button.  
- Remove the upper side of the head coil:
  - Unplug the head coil from the bed connector.
  - Lift the lever that releases the upper part of the coil and put it aside (e.g., inside the bore or on a chair next to the scanner).
- Help the participant sit down.
- Help the participant step down and accompany them out to the control room.
- Help the participant recover their personal belongings and change clothes if necessary.
- Give the participant the corresponding compensation for the participation and transportation.
- Ask the participant to sign the receipt of the amount of the financial compensation.

#### ET setting

- Place the half-circle screen back to the table behind the scanner.
- Unplug the two cables (signal and power) connected to the ET arm.
- Roll the two ET cables and put them in the cupboard inside the Scanning room.
- Remove the mirror frame from its rails mounted on the head coil and lay it on the bed.
- Put the gloves on and cover the infrared mirror with a mask for storage.

#### Clearing up the Scanner

- Unplug the cable on the scanner from SyncBox and roll it back to the shelf.
- Remove used blankets and bed-sheets ONE-BY-ONE: extend them to let any forgotten items fall on the floor before you fold it; and dispose of them in the adequate bin (soiled linen bag if they are fabric and trash if they are disposable).
- Dispose of all single-use sanitary protections (padding covers, earplugs, etc.).
- Put the pillows back in their designated storage places.
- Remove the head coil and put it in the scanner's bore.
- Remove the back padding elements and put them back in their designated storage.
- Reinstall the spine coil.
- Wipe the bed and the head coil (bottom and upper parts).
- Lock the head coil back with its bottom part without plugging the connectors.
- Put the head coil away with the other head-coils on the shelf next to the scanner.
- Return the bed to its Home position by pressing the button (more info).
- Take the ET arm, the infrared mirror and the plexiglass panel outside to the control room and store them in the ET/fMRI box.
- Exit and close the external door.
!!! warning "Everything that is removed for the experiment needs to be put back in place at the end of the experiment, i.e., position of the bed, coil, emergency button, ears cover."

#### Collect ET data

- Copy data from the subfolder of PsychoPy program into the hard drive.
!!! tip "The subfolder should include the files for one session with the formats like
`000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.EDF`
`000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.csv`
`000001_fixed_dot-16_grid_T1w_2024-10-14_17h24.37.511.log`
where '**.EDF' files are eye tracking records, `.csv` and `.log` files logs the task messages and the corresponding timestamps."

#### Collect MRI raw data

#### Export Twix raw data

- Twix: Username: █████████, Password: ████████████.
- Press `Ctrl+Esc` to open the IDE terminal.
- In the IDE terminal: ideacmdtool -> type `4` -> type `6` //
- Type `Twix` and the Twix data browser opens.
- Select the data you want to copy, right click on the mouse -> Copy Total RAID file -> select destination (your hard drive).
- The only useful thing is the physio [select the flag on External Signal] <mark>need more explanation </mark>
  
#### Export the DICOM data (directly reconstructed images from the scanner)

- Login as SuperUser by pressing `Tab` + `Delete` + `(Bottone a DX - 9)` to enter the advance mode.
- Export DICOM: select the patient, go to export // File System // Browse -> select `HD`.
- Select the “Enhanced” option (1 DICOM  / volume) instead of Interoperability (1 DICOM / slice).
!!! warning "The default option is `Interoperability`! So we have to change it manually!"

#### Cleaning up the Control Room

- Plug back the SyncBox and the VGA projector where they were. Make sure you leave it connected exactly as you found it.
- Cover the eye tracker lens with the lid.
- Unscrew the 50mm lens from the eye tracker and place it back to the bag with the tag `50mm Lens for MRI use` on it.
- Make sure the infrared mirror covered with a mask and everything stored safely in the ET/MRI box.
- Store the ET/MRI box back to the office.
- Switch off ET PC.
- Switch off the projector.