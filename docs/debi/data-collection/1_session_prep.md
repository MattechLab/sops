## Session Preparation

### Documentation

- [ ] Prepare the informed consent form ([EN](../../assets/files/informed_consent/form-en.pdf)|[FR](../../assets/files/informed_consent/form-fr.pdf)|[DE](../../assets/files/informed_consent/form-de.pdf))
- [ ] Prepare an MRI safety screener ([EN](../../assets/files/mri_safety/safety_form-en.pdf)|[FR](../../assets/files/mri_safety/safety_form-fr.pdf))
- [ ] Prepare a pen and a [receipt form](../../assets/files/reimbursement.pdf) that the participant will sign when they are given the compensation

### Configure the IP address

If you are connecting your PC to the eye tracker (ET) for the first time, you need to reconfigure the IP address.
On windows:

- Go to `Control Panel` -> `Network and Internet` -> `Network Connections`
- Double-click on the `Ethernet` connection.
- Select `Internet Protocol Version 4 (TCP/IPv4)` and click `Properties`.
- Update the IP address to `100.1.1.2` and the subnet mask `255.255.255.0`.

![0-e-ip](../../assets/debi_protocol/selected/0-e-ip.jpg){: style="width: 80%;display: block; margin: 0 auto;"}
![0-e2-ip](../../assets/debi_protocol/selected/0-e2-ip.png){: style="width: 80%;display: block; margin: 0 auto;"}

### Prepare Equipment Outside the Scanner Room

#### Turn on the projector

!!! important "If someone is already scanning, ask first if you can switch the projector on already"

Turn on the Sony projector located in the back room of the scanner room.
![projector-e](../../assets/debi_protocol/selected/1-projector-e.png){: style="width: 80%;display: block; margin: 0 auto;"}

Ensure the projector beam is directed into the scanner room.

#### Set up the Psychopy laptop on the table

- Take the psychopy PC from JB's office.
![laptop-office](../../assets/debi_protocol/selected/2-e-jb-office-laptop.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Insert the hdmi into the Psychopy laptop to monitor the visual stimuli on the screen. The hdmi should be from the 3-cable bundle (which connects PC, projector and the Psychopy laptop).
![psychopy-laptop](../../assets/debi_protocol/selected/2-e-psychopy-laptop.png){: style="width: 80%;display: block; margin: 0 auto;"}

- If the monitor does not automatically switch the screen source, use the button below to manually change it.
![button-monitor](../../assets/debi_protocol/selected/3-e-button-monitor.jpg){: style="width: 80%;display: block; margin: 0 auto;"}

- Change the resolution of the screen of the laptop to 800x600 to ensure the whole screen is projected to the participant inside the scanner.

- Ensure that the PC beneath the monitor remains turned on.
![pc-under-screen](../../assets/debi_protocol/selected/3-e-pc-under-screen.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Connect the USB cable from the SyncBox to the PsychoPy laptop.
![usb-from-SyncBox-1](../../assets/debi_protocol/selected/4-e-usb-from-syncbox.png){: style="width: 80%;display: block; margin: 0 auto;"}
![usb-from-SyncBox-2](../../assets/debi_protocol/selected/4-e2-usb-from-syncbox.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Plug the Ethernet from the ET computer to the psychopy laptop.
![ethernet](../../assets/debi_protocol/selected/5-e-ethernet.png){: style="width: 80%;display: block; margin: 0 auto;"}
!!! danger "Make sure the IP address is reset if the laptop is connected to the ET PC for the first time!"

#### Set up the SyncBox

- Ensure the SyncBox cable (RJ45) is already plugged onto the interface to the scanner room.
![rj45-1](../../assets/debi_protocol/selected/6-rj45-plugged.png){: style="width: 80%;display: block; margin: 0 auto;"}
- Plug the other end of the cable into the SyncBox.
![rj45-2](../../assets/debi_protocol/selected/6-e2-rj45-plugged.png){: style="width: 80%;display: block; margin: 0 auto;"}
- Turn on the SyncBox
- Check synchronization
    - [ ] Enter the <span class="syncbox">Synchronization</span> mode by selecting it and pushing the enter button :fontawesome-solid-circle:{ .bluecolor }.
    - [ ] Hit the down arrow button :fontawesome-solid-caret-down:{ .bluecolor } until you find <span class="syncbox">Send triggerpulse to PC</span>
    - [ ] Push the enter button :fontawesome-solid-circle:{ .bluecolor } every time you want to send an <span class="keypress">s</span> character.
    - [ ] Check that the *PsychoPy* laptop types those triggers (e.g., on an open editor receiving keypresses, or the shell prompt, or looking at your open log).

    ![Trigger to PsychoPy PC](../../assets/debi_protocol/selected/19-pc-trigger-signal.png){: style="width: 80%;display: block; margin: 0 auto;"}
    **Trigger to PsychoPy PC**
    {: style="text-align: center;"}

    - [ ] Check that the *PsychoPy* laptop types those triggers onto the scanner's PC.

    ![Trigger to Scanner](../../assets/debi_protocol/selected/19-scanner-signal.png){: style="width: 80%;display: block; margin: 0 auto;"}
    **Trigger to Scanner**
    {: style="text-align: center;"}

- Go to the `Simulation`, and we can see the `Start Session` on the page.
![start-sync-1](../../assets/debi_protocol/selected/7-e-start-sync.png){: style="width: 80%;display: block; margin: 0 auto;"}
![start-sync-2](../../assets/debi_protocol/selected/7-e2-start-sync.png){: style="width: 80%;display: block; margin: 0 auto;"}
- Configure the TR time to 2500 ms according to our sequence. The TR determines the interval between two triggers.
![tr-sync](../../assets/debi_protocol/selected/7-e3-tr-sync.png){: style="width: 80%;display: block; margin: 0 auto;"}

#### Set up the ET system

- Make sure the ET PC is plugged in.
![charge-et-pc](../../assets/debi_protocol/selected/8-e-charge-ET-PC.png){: style="width: 80%;display: block; margin: 0 auto;"}
- Before turning on the ET computer, ensure it is connected to the PsychoPy laptop (this should have been done in the previous step).
- Switch on the ET’s PC using the power-on button at the front
- Select "Eyelink" when given the option of which operating system to launch.
- Initialize the ET software from the ET work station here by typing "elcl.exe" in the terminal
![et-initial](../../assets/debi_protocol/selected/8-e-ET-initial.png){: style="width: 80%;display: block; margin: 0 auto;"}

!!! warning "The command elcl.exe will only work and start the software once the eye tracker device is connected to the ET PC. If you encounter any error messages, please ensure the eye tracker is connected to the PC inside the scanner room and try running the command again."

#### Prepare the Eye Tracker device

- All the lenses, mirrors, and other equipment are in the box in JB's office.
![box](../../assets/debi_protocol/selected/9-e-box.png){: style="width: 80%;display: block; margin: 0 auto;"}
- Install the <mark>50mm</mark> lens onto the eye tracker (the compatible lens has a silver screw on it) <mark>(photos from Oscar's SOP)</mark>
  
![lens-1](../../assets/debi_protocol/selected/10-e1-cover-mri-compatible-lens.png){: style="width: 80%;display: block; margin: 0 auto;"}
![lens-2](../../assets/debi_protocol/selected/10-e2-cover-mri-compatible-lens.png){: style="width: 80%;display: block; margin: 0 auto;"}

!!! tip "The default position of the screw for convenient focus is typically set to around `1`. ![install-lens](../../assets/debi_protocol/selected/20-e-screw-of-lens.jpg)However, the exact value can vary depending on the specific participant and setup for each time. It's recommended to start with the screw at value `1` and adjust from there for optimal focus during setup. If you're following a specific SOP, it might provide additional details for your equipment."
![install-lens](../../assets/debi_protocol/selected/11-install-lens-ET.png){: style="width: 80%;display: block; margin: 0 auto;"}

#### Place the infrared-mirror onto the head coil

- Detach the standard mirror's frame from the head coil, if it is placed there.
- Take the infrared mirror out of the «fMRI usage» box. It should be always protected by a mask unless in use.
!!! warning "This infrared mirror is the most delicate part, because the mirror cannot be replaced nor cleaned. This mirror is EXTREMELY EXPENSIVE."
![ir-mirror](../../assets/debi_protocol/selected/12-e-infered-mirror.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Get two gloves (e.g., from the box hanging at the entrance of the scanner room)
- Put the gloves on, and **DON'T TOUCH ANYTHING**. You must have the standard mirror dismounted and ahead of this step.
- **WITH THE GLOVES** proceed to extract the infra-red mirror from its box, being extremely careful. **YOU CAN ONLY TOUCH THE MIRROR WITH GLOVES**, because it cannot be cleaned up. Watch out for FINGERPRINTS and once taken out of the protection mask, IMMEDIATELY AND CAREFULLY ATTACH IT to the head coil.
![head_coil_mirror](../../assets/debi_protocol/selected/22_anno_head_coil_mirror.png){: style="width: 80%;display: block; margin: 0 auto;"}

### Preparation in the scanner room

#### Connect the external cables to ET and scanner

![cables](../../assets/debi_protocol/selected/13-e-cables.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Unroll and connect the cables (two plugs for the black, one plug for the orange).
![et-cables](../../assets/debi_protocol/selected/13-e-ET-cables.png){: style="width: 80%;display: block; margin: 0 auto;"}

!!! warning "No photo here due to magnetic field."

#### Place the eye tracker and screen

- Place the glass plate (stored in JB's office) on the scanner
- Position the ET on the glass plate according to the stickers on the plate.

!!! danger "Hold the ET arm FIRMLY, because the magnetic field imposes some resistance."

- Place the half-circle one-direction screen, which is on the table behind the scanner, onto the glass plate. Position it between the projector and the eye tracker to reflect the projector's image.
![half-circle-screen](../../assets/debi_protocol/selected/14-half-circle-screen.png){: style="width: 80%;display: block; margin: 0 auto;"}

- Check the output of the following command and verify that IP/mask is **100.1.1.2/24**, and the protocol is IP version 4.

    ``` shell
    ifconfig -a
    ```

- Check whether the link is properly established. The ET should respond to echos sent from a terminal with:

    ```shell
    ping 100.1.1.1
    ```

#### Place the participant

##### Place the subject on the bed

- Provide the participant with a blanket, ear plugs and sand bags.
- Adjust the head coil and the mirror. If necessary, apply some pads to adjust the participant's head position to ensure the forehead tightly positioned against the head coil.
- Ensure the participant does not cross the legs.
- Provide the participant with the emergency button and explain that it can be pressed it in case of an emergency.

##### Adjust the scanner before send the subject inside

- Twist the knob to adjust the height of the bed and  wait for it to stop.
- Gently move the participant with the manual controls. Stop when the head is under the head-localizer. Instruct the participant to close the eyes.
- Turn on the red light to localize the head. Put one hand on the head coil, then turn the knob left or right to align the red light with the mark on the head coil. Once aligned, turn off the red light and instruct the participant to open the eyes.
- Turn off the ventilation and set the scanner light to the minimum level.
- Send the participant into the scanner, then proceed to the console at the back of scanner.

##### Adjust the lens of eye tracker

- Point the lens of eye tracker towards the participant's right eye.
- The default position of the screw on the lens can be set to around 1 for convenient adjustment.
![install-lens](../../assets/debi_protocol/selected/20-e-screw-of-lens.jpg){: style="width: 80%;display: block; margin: 0 auto;"}
- Rotate the lens until the pupil is in focus on the screen during camera mode. Adjust until the image is sharp, with both the pupil and eyelashes well defined.
![no-pupil](../../assets/debi_protocol/selected/17-e-no-pupil.jpg){: style="width: 80%;display: block; margin: 0 auto;"}
![good-pupil](../../assets/debi_protocol/selected/17-e-good-pupil.jpg){: style="width: 80%;display: block; margin: 0 auto;"}

### ET Calibration

#### Inform the participant

Inform the participant that you are leaving the room and will shortly come back for a final preparation.

#### Open psychopy in the psychopy laptop

If you are connecting the eye tracker to the experimental laptop for the first time, you will need to configure it (see Section 0).

#### Run the experiment on psychopy

Click the `Run Experiment` button, or run the experiment from the terminal by typing:
`python experiment.py`. All the experiments must have a calibration and validation phase before the experiment itself (they come with the software).

!!!info "Click [here](https://github.com/Evelyn92/MREye_psychopy/blob/main/ver25/fixation_dots_T1weighted_250127_last_run.py) to check out the psychopy code for the [2.0 MR-Eye study](https://data.snf.ch/grants/grant/220433), and [here](https://github.com/MattechLab/MR-EyeTrack/blob/dev/visual_stimuli/fixed_dot-16_grid_T1w.py) for the [MR-Eye Track study](https://hee-projets.heig-vd.ch/en/projects/183/MREye-Track)"

![et-calibration](../../assets/debi_protocol/selected/18-e-calibration.png)
<!-- {: style="width: 80%;display: block; margin: 0 auto;"} -->
**Example psychopy project (MR-Eye Track)**
{: style="text-align: center;"}

!!! important "Make sure that once the experiment start after the calibration, the data are being stored to the xx.EDF file. There should be a message about that displayed <mark>at the ET’s PC screen</mark>. <mark>(According to Helene's SOP, but we did not notice there was such message popping out before)</mark>"

!!! important "For every new visual stimulation, even on the same subject, there must be new calibration and validation phases to ensure a proper generated EDF"

#### Run the calibration

Once the stimulation begins, follow the messages on the screen to run the calibration, make sure the following options are selected correctly

- Calibration Type: `5 points calibration`
- Sampling rate: `1k`
- Tracking mode: `Pupil-CR`
- Pupil Tracking: `Ellipse`
- Camera Position: `Right`

#### Apply threshold to find the pupil

- On the ET PC, click `Apply Threshold` (top left corner, as shown in the figure below). Ensure that the pupil is detected and that you see the blue cross on the eye. If you encounter issues, check the lighting inside the scanner (ensure it's not too bright or too dim) and verify the participant's position inside the coil. Once the calibration starts, accept the calibration points when they turn green by clicking `Accept Fixation` (the first click is always manual, the following ones are automatic or manual).
- If the calibration was successful, you will see the sentence `calibration successful` at the bottom in green. Check the stability of the accepted points and overall score of the calibration.
!!!tip "If the calibration points form a cross, it is a perfect calibration."
![good-cross](../../assets/debi_protocol/selected/16-e-good-cross.jpg){: style="width: 80%;display: block; margin: 0 auto;"}

#### Follow up with the validation

!!! tip "What you should see in an ideal situation is: the reference dot on the center of the screen and another dot that corresponds to the pupil calibration. The calibration dot is more or less stable moving a little around the reference dot."
!!! warning "If the calibration dot is unstable and is moving around far from the reference dot, the experimenter should go back clicking the restart button, adjust the contrast and redo the calibration. Once the calibration dot is quite stable, proceed with the validation clicking the accept fixation."

![validation](../../assets/debi_protocol/selected/18-e-validation.jpg){: style="width: 80%;display: block; margin: 0 auto;"}

#### Go into the scanner room and inform the participant

Inform the participant that you are leaving the room and will now close the door to start. Let them also know that you are going to communicate with them very shortly to check that communications through the speaker are functioning.

#### Exit the Scanning Room

#### Close the Scanning Room door