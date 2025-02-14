# **Data Collection for Resting-state audiovisual fMRI protocol**

## **Overall experimental setting** 

The experimental setup includes:

- [X] **Syncbox**: A NordicLabs Syncbox receives TTL (transistor-transistor logic) triggers 
from the scanner. This box can forward the triggers converted into other formats and/or 
manipulate them (e.g., filter, generate, etc.).
- [X] **Eye tracker (ET)**: We use the EyeLink 1000 Plus (SR Research Ltd., Ottawa, Canada). 
Our particular variant “Long Range” is composed of three main elements: 
  <ul>
      <li>inside the scanner's bore, we place an arm that holds an infrared lens and camera 
sensor on one side and an infrared lamp that illuminates the right eye of the subject 
through</li>
      <li>a special mirror to reflect the infrared spectrum;</li>
      <li>a PC tower that receives the camera recordings, post-processes the images, and 
calculates the final parameters of interest (position of the eye, pupil size, etc.).</li>
      <li>The ET is also connected to the experimental laptop.</li>
    </ul>
- [X] **Experimental laptop**: It is the laptop where the Psychopy software is installed and 
with it the task programs are executed. This laptop also stores the data recorded by the ET at 
the end of the experiment.

#### **ONE DAY BEFORE SCAN DATE**

- Verify that all Psychopy experiments run correctly.
- Verify that all the tools necessary for the data collection run correctly → check that the 
eyelink machine is correctly working.

???+ quote "Configuration"
    - If you connect the eye tracker to the experimental laptop for the first time, you need to configure it.
	- Go to the experimental laptop.
	- Double click on the ethernet connection inside the control panel.
    
	  ![control_panel1.png](../assets/images/control_panel1.png "control_panel1")
	  
	- Change the IP address → double click on the internet protocol version and change IP address with IP 100.1.1.2 and sub with 255.255.255.0.

- Print the informed consent form.
- Print the MRI safety screener (EN|FR).
- Print a receipt form for each participant that will get scanned.

## **Session preparation**
The following section describes how to prepare the session on the day of the scan BEFORE the 
participant arrives. 
!!! caution "Try to arrive at the Control Room at least 30 min ahead of the session start time."

### **Setup Preparation Inside the Scanner room**
- Memorize where the other tools for the recordings are to put those back in place at the end 
(coil, emergency button, headphones).

#### **Setting up the projector**
- Before entering the scanner room, go to the room where the projector is installed.
- Switch the projector ON by hitting the power button located on its right side.
- Verify the aim of the projector's beam by looking through the tube into the Scanning Room.
- Verify the projection corresponds to the Psychopy laptop screen.
- Before exiting the projector room, grab the plexiglass panel where the ET arm will be placed 
inside the scanner.
- Take the panel to the Control Room.
- Go to the scanner room and take the half-circle one-direction screen from the table behind 
the scanner and put it on the back of the scanner.


#### **Setting up the eye-tracker**
- From the CIBM EEG lab, take the box with the «fMRI usage» label, containing the lenses, as 
well as the plastic base for placing the Eye-Tracker inside the MRI hole, and the special 
mirror.
- ET arm preparation: 
  <ul>
    <li>Take out of the lenses box the MR-Compatible lense. It is easy to recognize it, from 
its two golden screws (see figure A and B)</li>

    <li>Un-screw any present lenses, being very careful: one hand must be hold under the lens, 
to avoid crashes, as it is a bit tricky to screw and un-screw it. In case a lens it’s 
already present, un-screw it and put it back to its plastic bag, inside the lenses box (see
 figure C). </li>
  </ul>
	![lens](../assets/images/lens.png "lens")
  
- Bring the plexiglass panel inside the scanning room and place it at the end of the scanner's 
bore. A sign indicates the top side that MUST face up. The plastic feet must face down to avoid
 the panel from sliding. To ensure the repeatable positioning of the ET, place the end of the 
plexiglass such that its edge aligns with the edge of the illuminated MRI rails.
- Exit the Scanning Room and fetch the ET arm.
- Enter the Scanning Room and place the ET arm on top of the plexiglass panel with the two 
posterior feet of the ET arm aligned within the two corner markers made of scotch tape.
!!! danger "Hold the ET arm FIRMLY because the magnetic field imposes some resistance"

- Unroll and connect the cables (two plugs for the black, one plug for the orange).
![cables2](../assets/images/cables2.png "ET_system")

- Take the half-circle one-direction screen from the table behind the scanner and put it on the
 back of the scanner behind the ET system (don't push the plexiglass yet).  
![ET_system](../assets/images/ET_system.png "ET_system")


#### **Setting up the coils**
- If any head coil from the last exam is still plugged, remove it:
  <ul>
    <li>If it is the 64-channel coil, you can just temporarily move it into the scanner's bore.
</li>
    <li>Otherwise, store it on the shelf where the other coils are and bring the 64-channel one
 in the proximity of the bed (e.g., inside the scanner's bore). Make sure to remove other 
coil's fitting elements.</li>
  </ul>
- Remove the spine coil by lifting the corresponding latch, then sliding it toward the head of 
the bed, lift it from the bed and place it on the floor ensuring it is not obstructing any 
passage or unstable.
- Place the two back padding elements filling the spine coil socket.
- Place the 64-channel head-and-neck coil into its socket at the head end of the bed.
- Attach the dedicated InfraRed mirror to the coil:   
![infrared](../assets/images/infrared.jpg "infrared")
  <ul>
    <li>Exit from the Scanning Room.</li>
    <li>Fit in a pair of new latex gloves.</li>
    <li>Extract the dedicated InfraRed mirror from the ET box CAREFULLY.</li>
    <li>Remove the mirror protection EXTRA-CAREFULLY.</li>
    <li>Take the mirror, enter the Scanning Room and lock the mirror onto the frame of the 
head-coil.</li>
	<li>Cut two long pieces of paper scotch and with your gloves on, put the infrareds mirror 
in the upper mirror (the top one, pointing towards the upper hole of the scanner). Put it 
more or less in the center, although this position may need to be adjusted (being careful 
and with the same precautions explained before) and stick it with the paper scotch. Do not 
touch the surface of the infrareds mirror.</li>
	<li>Put aside the top part of the coil.</li>
  </ul>
	!!! danger "THIS IS THE MOST DELICATE PART, THE MIRROR CANNOT BE REPLACED NOR CLEANED, IT IS EXTREMELY EXPENSIVE. DO NOT REMOVE IT OUT FROM ITS CUSTODY YET."
	
	!!! danger "YOU CAN TOUCH THE MIRROR ONLY WITH GLOVES, AS IT CAN’T BE CLEAN LIKE THE OTHER MRI-COMPATIBLE PART. SO NO FINGER PRINTS, ANYTHING CAN BE LEFT ON TOP OF IT."

#### **Setting up cables and headphones**
- Open the door of the cable section between the control room and the scanner room.
- Connect the scanner machine to the sharing system.
- Prepare the headphones to connect to the scanner machine. The type of headphone was choose 
based on the comfortability for the participant. Here are the two possible models:
![headphones](../assets/images/headphones.jpg "headphones"){ width=80% }

#### **Final setting inside the scanning room**
- Cover the MRI bed with a clean sheet.
- Prepare padding: under-knee padding, neck-and-head padding, under-elbows padding, head-sides 
padding, top-head wedge padding.
  <ul>
    <li>Wrap a sanitary cover around each padding.</li>
    <li>Place a double neck-and-head padding inside the coil, to ensure the eyes are close to 
the coil's windows.</li>
  </ul>
- Prepare a blanket to cover the participant.
- Prepare a new pair of earplugs.
- Completely disable the light inside of the scanner and the ventilation of the scanning room 
to facilitate the best performance of the ET.


### **Setup Preparation Inside the Control Room**

#### **Setting up experiment instruments**
- Place the experimental laptop on the designed desk and connect all the as showed in the 
following picture. Specifically, connect the experimental laptop to:
  <ul>
    <li>Plug the power adaptor to the laptop, and the adaptor to the power outlet on the wall.<
/li>
    <li>The screen switch box with the corresponding HDMI cable (This should project your 
screen on the screen of CHUV's tower).</li>
    <li>The RJ-45/Ethernet cable from the ET computer into the RJ-45 socket of the experimental
 laptop.</li>
    <li>Connect the SyncBox to the laptop with the USB cable. It is normally plugged into 
CHUV's stimuli workstation, it must be re-plugged in there after the session.</li>
  </ul>
	![computer_connections3.png](../assets/images/computer_connections3.png 
"Gcomputer_connections3")
  
- Switch the laptop on and open the psychopy code.
- Click the switch button to share your PC.
- Switch the SyncBox on using the button on the right side called *power*.
- Change the SyncBox correctly to send the triggers (Corresponding to push the key-button *“S”*
 from keyboard). Take the SyncBox and go on *“Simulation”* mode.
- Then, change the parameters in the main menu modifying the pulse length at 100ms and the TR 
time at 650ms. 
- Push the enter button and the syncbox will be now waiting for the scanner's trigger signal to
 forward it.  
![syncbox](../assets/images/syncbox.png "syncbox"){ width=63% }

- Open the door of the cable wardrobe between the recording room and the scanner room where the
 ET power is also placed, and connect the syncbox in the following way:  
![syncbox_connection6](../assets/images/syncbox_connection6.jpg "syncbox_connection6"){width=40% }
![syncbox_connection7](../assets/images/syncbox_connection7.jpg "syncbox_connection7"){width=40% }

- Switch on the ET’s PC using the power-om button at the front
- Select "Eyelink" when given the option of which operating system to launch.
  <li>Verify the IP address assigned to the Ethernet interface of the experimental laptop is 
correct:
    <ul>
      <li>Check the output of the following command and verify that IP/mask is 100.1.1.2/24, 
and the protocol is IP version 4.</li>
      <li>Check whether the link is properly established.</li>
    </ul>
  </li>

## **Setup Preparation at the technician position**
- Change the parameters for the audio system in the *“Scan Application”* section as reported in
 the following figure at the pc and at the box.  
![audio_system17](../assets/images/audio_system17.jpg "audio_system17"){ width=40% }
![audio_system16](../assets/images/audio_system16.jpg "Gas Analyzer front"){ width=42.38% }
!!! Danger "Ensure that the volume is sufficiently high so that the participant can clearly hear the sounds."

- Switch audio to the scanner room clicking *“input”* button:
![audio_system18](../assets/images/audio_system18.jpg "Gas Analyzer front"){ width=60% }

## **Participant Preparation**
!!!caution "When the Participant Arrives"

### **Participant Reception**

- Meet the participant at an easily locatable place (e.g., the reception desk of the Radiology 
Unit) and show them the way into the control room. Allow sufficient time before the experiment 
for the preparation.
- Show the participant the scanning room and explain to them how the device is controlled from 
outside.
- Ask the participant to fill out the consent form and MRI safety screener, and verbally 
confirm responses and discuss further doubts, paying attention to frequently forgotten devices 
and implants, like orthodontia.
- Remind the participant to use the bathroom at this moment if they need.
- Describe to the participant how the session will develop and explain clearly the task. Let 
them interrupt you to ask for clarifications and answer all the questions that may arise.

???+ quote "Script for the session"
      “We are going to acquire two types of images. The first type is anatomical imaging that we use to study the morphology of the brain. The second type is a functional MRI, which we use to understand how the brain activates as a response to stimuli we will present to you. During the whole duration of the exam, please do not create closed loops by crossing your legs or holding your hands together. It is possible that your peripheral nerves get stimulated at some points, so you will feel twitching of muscles, for instance, of your  pectorals. Do not panic, it is okay, but if it feels too uncomfortable, please squeeze  the alarm button. 
	  
	  For the anatomical MRI we just ask you to relax and try to stay as still and comfortable as possible. Like a photographic camera, the largest problem making analyses difficult is motion. As opposed to a photo camera, the imaging of the brain happens very slow so there is a lot of opportunity for involuntary movements (e.g., when you blink or you take a deeper breath) or semi-voluntary (e.g., you need to swallow). During the functional MRI you will see a a 7-minutes abstract video with a relaxing sound which is repeated three times during the experiment, for a total duration of 21 minutes. For the entire period of the experiment you should takes the eye open. The experiment has a duration of 30 minutes more and less. Before to start with scanning we will need to calibrate the  eyetracker, therefore we will ask you to fix different points on the screen.

      *Is everything clear to you? Do you have any questions?*”

- Offer the participant a box to deposit everything they have in their pockets and all 
jewelry/hair accessories, and indicate that before continuing, we need to make sure we do not 
introduce any dangerous objects into the magnet room. Therefore, it is important to inform the 
participant to remove every metallic accessory.
- Ask to remove shoes at the entrance of the scanning room.

### **Participant Preparation in the Scanning Room**

- Instruct the participant to lay on the MRI bed and adjust the participant inside. With the 
paddings, their head position MUST be adjusted and elevated so that the nose and the forehead 
of the participant are both close to the upper coil. This procedure ensures the ET has the 
clearest possible view of the eye.
- This part needs to be repeated taking out and putting back the upper part of the head-coil, 
adjusting the pillow at every step, until the head is fixed and the nose and front of the 
participant touch the coil. In case of need, ask the participant to *"say yes"* with the head 
(chin on neck) and keep this position, place the pillows, place the coil and check that the 
participants' front touches the coil. Now the nose can also be a bit far from the coil. Tell 
the participant to relax the neck, so the nose should go a bit up and touch the coil.  
- Put the headphones on the ears.
- Give the participant the emergency button. Make the participant try it, so they can see it 
works. To switch off the alarm, there’s a button on the scanner (circular, both on the left and
 on the right of the hole).
- Once the previous part is ensured, the participant is ready. If the participant is cold, put 
a blanket on top of him.
- Connect the coil's cable to the corresponding socket on the table.
- Gently move the participant with the manual regulation. Stop when the head is under the 
head-localizer. Ask the participant to close the eyes, localize the head with the infrareds.
- Switch off the infrareds, now the participant can open the eyes. You can move the participant
 (always gently as before) inside the scanner, until the mm counter marks “Isometric”.
- Go behind the scanner, push the plastic base until it touches the bed. Hold on the 
Eye-Tracker.
- Regulate the Eye-tracker position until you see from the projector screen the Eye. In case of
 need, you can adjust the strength of the infrared light (emitter). This is the black box on 
the other side with respect to the lens. Under the emitter there are two little screws. 
Unscrew, move the emitter front/back, check the contrast of the face image, re-screw. Once the 
eye is well seen, the image is zoomed (externally by the operator in front of the PC-tower) to 
the pupil. The right lens needs to be manipulated rotating the roller, like what you would do 
with your reflex to obtain the focus. If the position of the Eye-tracker is not satisfying, you
 can move the base. 
- If the pupil is correctly seen, as well as the eye, you can go out. The calibration needs to 
start.

### **Final Preparations**

- Inform the participant that we will proceed with a final preparation and that he/she has to 
follow some point with its eyes, without moving his head.
- Tell the participant to move the eyes ONLY after the point moves (do not anticipate).
- Proceed with the calibration.

???+ quote "ET Calibration"
    - [X] Open psychopy in the experimental laptop.If you connect the eye tracker to the experimental laptop for the first time, you need to configure it.
	- [X] Double click on the psychopy file of the rs protocol to open it.
	- [X] Run the experiment on psychopy clicking the “run experiment” button. IMPORTANT: make sure that once the experiment start after the calibration, the data are being stored to the xx.EDF file. There should be a message about that displayed at the ET’s PC screen.
	- [X] Once the stimulation begins, you follow the messages on the screen to run the calibration (make sure the 5 points calibration has been selected).
	- [X] At the ET PC: apply threshold (left upper corner, as on the left figure), make sure that the pupil was found, and you see the blue cross on the eye. In case of troubles, check if there is enough light inside the scanner and not too much, check the position of the participant inside the coil. Once the calibration starts accept calibration points when green (Accept fixation).
	  
    ![ET_calibration8](../assets/images/ET_calibration8.png "ET_system")
	  ![ET_calibration9](../assets/images/ET_calibration9.png "ET_system")
	  ![ET_calibration10](../assets/images/ET_calibration10.png "ET_system")

	- [X] If the calibration was successful, you will see the sentence ‘calibration successful’ at the bottom in green. Check the stability of the accepted points and overall score o the calibration.
	- [X] Follow up with the validation. What you should see in an ideal situation is: the reference dot on the center of the screen and another dot, which correspond to the pupil calibration, that it is more and less stable moving a little around the reference dot. If the calibration dot is unstable and is moving around far from the reference dot the experimenter should go back clicking the restart button, adjust the contrast and redo the calibration. Once the calibration dot is quite stable proceed with the validation clicking the accept fixation. 
	
	!!! danger "The ET software needs to show a cross performed during the calibration. If not, the ET inside the scanner needs to be adjusted. If not, the head of the participant needs to be adjusted again. If not, the mirror needs to be moved up or down (being careful as mentioned before). Just a few mm can ruin the calibration and the eye-position."

- Inform the participant that you are leaving the room and will now close the door to start. 
Let them also know that you are going to communicate with them very shortly to check that 
communications through the speaker are functioning.
- Exit the Scanning Room.
- Close the Scanning Room door.

## **Running the Scanning Session**

!!!caution "You MUST know the security procedures in case of problem and keep yourself updated with changes." 

### **Before Initiating the Session: Run the Experiment**

- At the end of the ET calibration we are ready to run the experiment.
- Double click on the PsychoPy file of the checkerboard protocol to open it.
![psychopy2](../assets/images/psychopy2.png "psychopy2"){ width=70% }
!!!tip "Run the experiment on psychopy using the coder rather than clicking the “run experiment” button otherwise the EDF files of the ET were not saved."

- Wait for the sentence *“In this task you will see a color dot. Please keep your eyes on the 
fixation point. The program is ready for the scanner trigger. Press s to proceed manually.”*
- Then click *“start session”* on the sync box clicking the round button. 
![gaz-analyser-front](../assets/images/run_experiment11.jpg "Gas Analyzer front"){ width=40% }
![gaz-analyser-front](../assets/images/run_experiment12.jpg "Gas Analyzer front"){ width=40% }
- The sensory stimulation and the ET trigger will start with the scanning. At the end of the 
experiment click *“t”* on the experimental laptop and click the round button on the SyncBox to 
stop the running session.

### **During the Session**

- Check in with the participant.
- Check in that everything is correctly working (e.g., The pupil is correctly detected, sounds are played and heart from the participant, volume is loud enough, triggers correctly works, etc.).
- Watch for motion and arousal state using the ET's camera. If you detect motion or the 
participant falls asleep at inadequate points, use the speaker to inform them.

#### **Acquire a Localizer**

- Indicate the participant that the scanning will soon start.
- Wait for the participant confirmation and set the speaker off afterward.
- Launch the AAhead_scout_64ch-head-coil protocol by pressing Continue.
- Once the localizer is concluded, click on the image stack icon with left click and drag the 
image with a 1 onto the image viewer. That will open the interpolated localizer on the viewer.
- If the quality looks good, check the box stating Localizer looked ok. If not, re-acquire the 
localizer.  
![localizer](../assets/images/localizer.jpg "localizer"){ width=80% }

#### **Acquire a High-Resolution Anatomical Image**

- Run the wip19_mprage_1iso_cs4p2 protocol by pressing *Continue*.
???+ quote "Anatomical image Acquisition" 
    - While you are still running the MPRAGE sequence open the parameters of the sequence (showed in the figure) and ensure that:  
	![parameter](../assets/images/parameters.jpg "parameter"){ width=80% }	
    - [X]	under ***Sequence*** in the subsection ***Part1***, the *shot per slice* should be set at 419. This is crucial so that so that the acquisition time is more and less 1 minute.
    - [X]	under ***Routine***, *TR* and *TE* should be set at the minimum value. 
    - [X]	under ***Contrast*** in the subsection ***common***, the *fat-water* should be set as standard and the *flip angle* should be set at 5 degree.
    - [X]	under ***Contrast*** in the subsection ***filter***, click on the three dots and tick the *“unfiltered images”*.
    - [X]	under ***System*** in the subsection ***coils***, select Body the coils HC3, HC5, HC4, HC6, HC7 for BOLD_HC.
    - [X]	under ***System*** in the subsection ***miscellaneous***, put the coil selection as manual.
    - [X]	under ***Physio***, make sure that RECONSTRUCTION is off. 
    - Finally, click copy and go button


#### **Acquire Functional Image**

- Inform the participant that we will start with the fMRI block, therefore the participant will
 start hearing sounds.
- Run the BEAT_LIBREoff_RS protocol by pressing *Continue*.

## **Session Completed**

- The exam is over, inform the participant that the session has concluded.
- At the end of the stimulation click “t” on the experimental laptop and click the round button
 on the SyncBox to stop the running session.
- You can proceed with the tear-down protocol.

## **Session Tear-Down**

### **Showing the Participant Out**

- Enter the scanner room, and announce yourself to the participant saying that you will get out
 the participant in a few seconds.
- Extract the participant by pressing the extraction button and then gently rolling the central
 knob. Alternatively, you can just press the Home button.
  <li>Remove the upper side of the head coil:
    <ul>
      <li>Unplug the head coil from the bed connector.</li>
      <li>Lift the lever that releases the upper part of the coil and put it aside (e.g., 
inside the bore or on a chair next to the scanner).</li>
    </ul>
  </li>
- Assist the participant to the headphones.
- Help the participant sit down.
- Help the participant step down and accompany them out to the control room.
- Help the participant recover their personal belongings and change clothes if necessary.
- Give the participant the corresponding compensation for the participation and transportation.
- Ask the participant to sign the receipt of the amount of the financial compensation.

### **Cleaning up the Scanning Room**
- Remove used blankets and bed-sheets ONE-BY-ONE: extend them to let any forgotten items fall 
on the floor before you fold it; and dispose of them in the adequate bin (soiled linen bag if 
they are fabric and trash if they are disposable).
- Dispose of all single-use sanitary protections (padding covers, headphones, etc.).
- Put the pillows back in their designated storage places.
- Take the upper part of the coil. Take the plastic container of the infrared mirror. Take the 
gloves. Put them on.
- Remove the scotch. Put the mirror back in its custody. Then back in its plastic bag.
- Place it back in the fMRI external box, with extreme care.
- Clean the coil mirror from the scotch. Clean the coil.
- Remove it and put it back in place.
- Remove the back padding elements and put them back in their designated storage.
- Reinstall the spine coil.
- Wipe the bed and the head coil (bottom and upper parts).
- Lock the head coil back with its bottom part without plugging the connectors.
- Put the head coil away with the other head-coils on the shelf next to the scanner.
- Put the projector screen back in place.
- Unplug the Eye tracker from the Optic Fiber and the Power. Put those extremities aside far 
from the scanner. Take the Eye-Tracker back outside. Put it in a stable place.
- Remove the plastic base, put that outside next to the box.
- Return the bed to its Home position by pressing the button (more info).
- Exit and close the external door.


!!!danger "Everything that is removed for the experiment needs to be put back in place at the end of the experiment, i.e., position of the bed, coil, emergency button, ears cover."

### **Cleaning up the Control Room**

- Switch off the laptop and ET PC Tower. Plug back the SyncBox and the VGA projector where they
 were. Make sure you leave it connected exactly as you found it.
- Fix the rolled cable with the scotch on the PC Tower base.
- Take the ET, Remove (always with and hand under the lens) the MRI compatible LENS. Put it 
back to its contained inside the box. 
- Put back the regular Lens. 
- Bring back the box and the base at CIBM EEG lab. Put the keys back under old Nora’s desk.
- Fix the ET with the scotch at the chariot.
- Switch off the projector.

!!!tip "Congratulations you are concluded your data collection and you can go at home and relax yourself!"