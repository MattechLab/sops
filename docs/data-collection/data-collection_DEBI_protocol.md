???+ quote "Note for writers"
      precisely point out what is connected to what by which kind of cables.

## Overall experimental setting
- The Syncbox transmits the signal to the PsychoPy laptop using the 'S' key and sends pulses to the scanner, as illustrated below:

![](../assets/debi_protocol/selected/19-pc-trigger-signal.png)
![](../assets/debi_protocol/selected/19-scanner-signal.png)

## Configure the IP address
If you are connecting your PC to the eye tracker (ET) for the first time, you need to reconfigure the IP address.
On windows:
- Go to `Control Panel` -> `Network and Internet` -> `Network Connections`
- Double-click on the `Ethernet` connection.
- Select `Internet Protocol Version 4 (TCP/IPv4)` and click `Properties`.
- Update the IP address to `100.1.1.2` and the subnet mask `255.255.255.0`.<mark> (Photos from Helene's sop)</mark>
 
![](../assets/debi_protocol/selected/0-e-ip.jpg)
![](../assets/debi_protocol/selected/0-e2-ip.png)

## Prepare ET set up outside the scanner room
### Setting up the projector
Turn on the Sony projector located in the back room of the scanner room.
![](../assets/debi_protocol/selected/1-projector-e.png)

Ensure the projector beam is directed into the scanner room.
### Set up the Psychopy laptop on the table
- Insert the hdmi into the Psychopy laptop to monitor the visual stimuli on the screen. The hdmi should be from the 3-cable bundle (which connects PC, projector and the Psychopy laptop).
![](../assets/debi_protocol/selected/2-e-psychopy-laptop.png)

- If the monitor does not automatically switch the screen source, use the button below to manually change it. 
![](../assets/debi_protocol/selected/3-e-button-monitor.jpg)

- Ensure that the PC beneath the monitor remains turned on.
![](../assets/debi_protocol/selected/3-e-pc-under-screen.png)

- Connect the USB cable from the Syncbox to the PsychoPy laptop.
![](../assets/debi_protocol/selected/4-e-usb-from-syncbox.png)
![](../assets/debi_protocol/selected/4-e2-usb-from-syncbox.png)

- Plug the Ethernet from the ET computer to the psychopy laptop.
![](../assets/debi_protocol/selected/5-e-ethernet.png)
!!! danger "Make sure the IP address is reset if the laptop is connected to the ET PC for the first time!" 
### Set up the syncbox
- Ensure the SyncBox cable (RJ45) already plugged onto the interface to the scanner room.
![](../assets/debi_protocol/selected/6-rj45-plugged.png)
- Plug the other end of the cable into the SyncBox.
![](../assets/debi_protocol/selected/6-e2-rj45-plugged.png)
- Turn on the syncbox
- Go to the `Simulation`, and we can see the `Start Sesson` on the page.
![](../assets/debi_protocol/selected/7-e-start-sync.png)
![](../assets/debi_protocol/selected/7-e2-start-sync.png)
- Configure the TR time to 2500 ms according to our sequence. The TR determines the interval between two triggers.
![](../assets/debi_protocol/selected/7-e3-tr-sync.png)
## Set up the ET workstation
- Make sure the ET PC is charged
![](../assets/debi_protocol/selected/8-e-charge-ET-PC.png)
- Before turning on the ET computer, ensure it is connected to the PsychoPy laptop (this should have been done in the previous step).
- Turn on the ET PC.
- Initialize the ET software from the ET work station here by typing "elcl.exe" in the terminal
![](../assets/debi_protocol/selected/8-e-ET-initial.png)
### Prepare the ET
- All the lenses, mirrors, and other equipment are in the box in JB's office.
![](../assets/debi_protocol/selected/9-e-box.png)
- Install the <mark>50mm</mark> lens onto the eye tracker (the compatible lens has a silver screw on it) <mark>(photos from Oscar's SOP)</mark>
![](../assets/debi_protocol/selected/10-e1-cover-mri-compatible-lens.png)
![](../assets/debi_protocol/selected/10-e2-cover-mri-compatible-lens.png)
<mark>what value is the default position of the screw for convenient focus ?</mark>
!!! tip "The default position of the screw for convenient focus is typically set to `1`. However, the exact value can vary depending on the specific participant and setup for each time. It's recommended to start with the screw at value `1` and adjust from there for optimal focus during setup. If you're following a specific SOP, it might provide additional details for your equipment."
![](../assets/debi_protocol/selected/11-install-lens-ET.png)

### Place the infrared-mirror onto the head coil
- Detach the standard mirror's frame from the head coil, if it is placed there. 
- Take the infrared mirror out of the «fMRI usage» box. It should be always protected by a mask unless in use.
!!! warning "This infrared mirror is the most delicate part, because the morror cannot be replaced nor cleaned. This mirror is EXTREMELY EXPENSIVE."
![](../assets/debi_protocol/selected/12-e-infered-mirror.png)
- Get two gloves (e.g., from the box hanging at the entrance of the scanner room)
- Put the gloves on, and **DON'T TOUCH ANYTHING**. You must have the standard mirror dismounted and ahead of this step. 
- **WITH THE GLOVES** proceed to extract the infra-red mirror from its box, being extremely careful. **YOU CAN ONLY TOUCH THE MIRROR WITH GLOVES**, because it cannot be cleaned up. Watch out for FINGERPRINTS and once taken out of the protection mask, IMMEDIATELY AND CAREFULLY ATTACH IT to the head coil.
<mark>[A photo of the head coil with the mirror correctly installed is missing]</mark>
## Preparation in the scanner room
### Connect three external cables to ET and scanner

![](../assets/debi_protocol/selected/13-e-cables.png)
- Two plugs for the black and one plug for the orange to ET 
![](../assets/debi_protocol/selected/13-e-ET-cables.png)
- Connect the external cable from the syncbox to the scanner.
<mark>No photo here due to magnetic field</mark>

### Place the eye tracker and screen

- Place the glass plate (stored in JB's office) on the scanner
- Position the ET on the glass plate according to the stickers on the plate.
- Place the half-circle one-direction screen, which is on the table behind the scanner, onto the glass plate. Position it between the projector and the eye tracker to reflect the projector's image.
![](../assets/debi_protocol/selected/14-half-circle-screen.png)
### Place the participant
#### Place the subject on the bed
- Apply a blanket, ear plugs and sand bags to the participant.
- Adjust the head coil and the mirror. If necessary, apply some pads to adjust the participant's head position to ensure the forehead tightly positioned against the head coil.
- Ensure the participant does not cross their legs.
- Provide the participant with the emergency button and explain that they can press it in case of an emergency.
#### Adjust the scanner before send the subject inside
- Twist the knob to adjust the height of the bed and  wait for it to stop.
- Gently move the participant with the manual controls. Stop when the head is under the head-localizer. Instruct the participant to close his eyes.
- Turn on the red light to localize the head. Put one hand on the head coil, then turn the knob left or right to align the red light with the mark on the head coil. Once aligned, turn off the red light and instruct the participant to open their eyes.
- Turn off the ventilation and set the scanner light to the minimum level.
- SSend the participant into the scanner, then proceed to the console at the back of scanner.
#### Adjust the lens of eye tracker
- Point the lens of eye tracker towards the participant's right eye.
- <mark>[Add the default position of the lens for convenient adjustment]</mark>
- Rotate the lens until the pupil is in focus on the screen during camera mode. Adjust until the image is sharp, with both the pupil and eyelashes well defined.
![](../assets/debi_protocol/selected/17-e-no-pupil.jpg)
![](../assets/debi_protocol/selected/17-e-good-pupil.jpg)
<mark>ask for Mauro's consent</mark>
## ET Calibration
#### Inform the participant
Inform the participant that you are leaving the room and will shortly come back for a final preparation.
#### Open psychopy in the psychopy laptop. 
If you are connecting the eye tracker to the experimental laptop for the first time, you will need to configure it (see Section 0).
#### Run the experiment on psychopy
Click the `Run Experiment` button, or run the experiment from the terminal by typing:
`python experiment.py`
  
!!! important "Make sure that once the experiment start after the calibration, the data are being stored to the xx.EDF file. There should be a message about that displayed <mark>at the ET’s PC screen</mark>. <mark>(According to Helene's, but we did not notice there was such message popping out before)</mark>"

#### Run the calibration
Once the stimulation begins, follow the messages on the screen to run the calibration, make sure the following options are selected correctly

- Calibration Type: `5 points calibration`
- Sampling rate: `1k`
- Tracking mode: `Pupil-CR`
- Pupil Tracking: `Ellipse`
- Camera Position: `Right`"

#### Apply threshold to find the pupil
- On the ET PC, click `Apply Threshold` (top left corner, as shown in the figure below). Ensure that the pupil is detected and that you see the blue cross on the eye. If you encounter issues, check the lighting inside the scanner (ensure it's not too bright or too dim) and verify the participant's position inside the coil. Once the calibration starts, accept the calibration points when they turn green by clicking `Accept Fixation`.
- If the calibration was successful, you will see the sentence `calibration successful` at the bottom in green. Check the stability of the accepted points and overall score of the calibration. 
!!!tip "If the calibration points form a cross, it is the perfect calibration."
![](../assets/debi_protocol/selected/16-e-good-cross.jpg)
 
#### Follow up with the validation. 
!!! tip "What you should see in an ideal situation is: the reference dot on the center of the screen and another dot that corresponds to the pupil calibration. The calibration dot is more or less stable moving a little around the reference dot."
!!! warning "If the calibration dot is unstable and is moving around far from the reference dot, the experimenter should go back clicking the restart button, adjust the contrast and redo the calibration. Once the calibration dot is quite stable, proceed with the validation clicking the accept fixation."

![](../assets/debi_protocol/selected/18-e-validation.jpg)
#### Go into the scanner room and inform the participant
  Inform the participant that you are leaving the room and will now close the door to start. Let them also know that you are going to communicate with them very shortly to check that communications through the speaker are functioning.
#### Exit the Scanning Room.
#### Close the Scanning Room door.
## Running the scanning session
### Run the Experiment
- At the end of the ET calibration we are ready to run the experiment.
- Wait for the sentence “In this task you will see a color dot. Please keep your eyes on the fixation point. The program is ready for the scanner trigger. Press s to proceed manually.”
  
!!! important "Due to the upgrade of the scanner, it cannot immediately start the acquisition after receives the trigger signal from the syncbox. Thus, we need to extract the temporal information of the scanner and ET respectively. In order to make such post-processing easier, we need to first start the acquisition, and then the eye tracker. Thus, the first trigger recorded in the pmu in the raw data will be exactly the same trigger that starts the eye tracker."

!!! danger "The order: start of scanner -> press the button of syncbox is important and cannot be exchanged."

- Now two people need to get ready beside the syncbox and the scanner.
- One person first start the scanner acquisition.
- Then, another person press  `start session` on the sync box clicking the round button. 
- The stimulation will start with the ET recording. 


### Acquire a high-resolution anatomical image

wip

### Acquire T1w-LIBRE image and T1w-VIBE image
### Acquire T2w-LIBRE image and T2w-TSE image
### Session Completed
- At the end of the stimulation, click “t” on the experimental laptop and click the round button on the SyncBox to stop the running session.
- The exam is over, inform the participant that the session has concluded.
- You can proceed with the tear-down protocol.
## Session Tear-Down (Unchanged as Helene's)
### Showing the Participant Out
- Enter the scanner room, and announce yourself to the participant saying that you will get out the participant in a few seconds.
- Extract the participant by pressing the extraction button and then gently rolling the central knob. Alternatively, you can just press the Home button.  
- Remove the upper side of the head coil:
  - Unplug the head coil from the bed connector.
  - Lift the lever that releases the upper part of the coil and put it aside (e.g., inside the bore or on a chair next to the scanner).
- Assist the participant to remove the headphones.
- Help the participant sit down.
- Help the participant step down and accompany them out to the control room.
- Help the participant recover their personal belongings and change clothes if necessary.
- Give the participant the corresponding compensation for the participation and transportation.
- Ask the participant to sign the receipt of the amount of the financial compensation.
### Cleaning up the Scanning Room
- Enter the scanner room, and announce yourself to the participant saying that you will get out the participant in a few seconds.
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
- Exit and close the external door.
!!! warning "Everything that is removed for the experiment needs to be put back in place at the end of the experiment, i.e., position of the bed, coil, emergency button, ears cover."
### Cleaning up the Control Room
- Switch off the laptop and ET PC Tower. Plug back the SyncBox and the VGA projector where they were. Make sure you leave it connected exactly as you found it.
- Switch off the projector.