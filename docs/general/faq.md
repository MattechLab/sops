# Frequently Asked Questions (FAQ)

<!-- TEMPORARY CI TEST CONTENT - to be reverted: this sentence has teh purpose of testing
the speling checkers, with a wibbleflorpzap word cspell should also catch. -->

## Troubleshooting

### Problem 1: Visual stimuli experiment fails to run on the on-site laptop

The visual stimuli experiment fails to run on the on-site laptop due to a version conflict. This likely occurs because different developers use different PsychoPy versions during development.

**Potential solution:**

- Ensure a consistent PsychoPy version across all platforms (development and execution) to prevent compatibility issues with the `.psyexp` file.
- Instead of running the `.psyexp` file directly, execute the generated Python script (`.py`) from PsychoPy in the terminal within the PsychoPy environment for greater stability.
- Use Git to track both the experiment files and PsychoPy configurations to maintain version control.

---

### Problem 2: Calibration or validation of the eye-tracker is rejected

The calibration or validation procedure of the eye-tracker is rejected.

**Potential solution:**

- Ensure the participant's forehead is firmly pressed against the head coil before entering the MRI scanner. If needed, use sponge pads to adjust head height.
- Turn off the scanner's interior light to prevent interference with the eye-tracker's infrared reflection system.
- Verify that the eye-tracker camera properly focuses on the pupil, with eyelashes visible in detail. If not, adjust the lens to the recommended setting (around 1) and fine-tune the smaller knob for precise focus.
- Avoid any possible source of artifacts, such as make-up or facial creams.

!!! tip "Additional guidance on ET setup and focus"
    See the [ET extended guidelines](et-related/notes-et.md#setting-viewframe-and-focusing) for step-by-step instructions on adjusting the viewframe, focus, and pupil detection thresholds.

---

### Problem 3: Participant fatigue causes prolonged eye closure during acquisition

The participant can become fatigued during acquisition, keeping their eyes closed for extended periods. This results in a high proportion of non-applicable data in the eye-tracking (ET) recordings, degrading data quality and impacting motion-resolved reconstruction.

**Potential solution:**

- Monitor the participant's eye status in real time on the eye-tracking (ET) PC.
- If the participant is falling asleep, use the microphone to check on their wellbeing:
    - If the participant feels unwell or too fatigued, stop the scan and guide them out of the scanner, rescheduling if necessary.
    - If the participant is simply tired but willing to continue, provide gentle encouragement to follow the stimuli while ensuring their comfort.

!!! warning "Interrupting the session"
    If the session is interrupted, right-click the current sequence in the scanner console and select *Repeat* to restart it without modifying its name. See [Notes on the scanner's console](notes-scanning.md#repeat-scan) for details.

---

### Problem 4: Participant cannot see the full visual stimuli (MR-Eye Track protocol)

The participant cannot see the full visual stimuli in the MR-Eye Track protocol, especially dots near the top, bottom, left, or right edges.

**Potential solution:**

Ensure the monitor resolution is set to **800×600**. If left at the default (e.g., 1920×1080), the projection onto the half-circle screen behind the scanner may be misaligned, causing stimuli near the edges to fall outside of the visible area for the participant.

!!! tip "Where to change the resolution"
    This setting is configured on the PsychoPy laptop during [session preparation](../debi/data-collection/1_session_prep.md#set-up-the-psychopy-laptop-on-the-table).

---

### Problem 5: Visual stimulation and scanning are not synchronized

Visual stimulation has started, but not the scanning — or vice versa.

**Potential solution:**

- Ensure that the EXT trigger cable is connected to the scanner and to the SyncBox, and that it is also connected inside and outside the scanner room to the same channel port.
- Check that in the IDEA UI, the EXT trigger is enabled in the **Physio** section.

!!! important "EXT trigger setup"
    See [Run scanning session](../debi/data-collection/2_run_scanning_session.md#send-the-trigger-to-both-the-scanner-and-the-stimuli-laptop) for details on enabling the EXT trigger in the IDEA UI.

---

### Problem 6: No EDF files are generated or they are empty

There are no EDF files generated, or they are empty.

**Potential solution:**

- Ensure that there is a line in your PsychoPy code to start the ET recording (usually `etRecord.start()`).
- Check that on the ET's PC there is a textbox with an increasing number — this indicates the samples being recorded by the ET and confirms it is recording correctly.
- It is mandatory to wait until the end of the experiment to allow the transfer of the EDF file. Do **not** interrupt this process by disconnecting the cable; it may take several seconds.

!!! warning "EDF transfer at session end"
    The EDF data transfer from the ET PC to the laptop is initiated by pressing `t` on the experimental laptop at the end of the session. Disconnecting the Ethernet cable before this step completes will result in an empty or missing EDF file. See [Session completed](../debi/data-collection/2_run_scanning_session.md#session-completed) for the full procedure.

---

### Problem 7: ET software (`elcl.exe`) fails to start

Running `elcl.exe` on the ET PC produces an error and the software does not launch.

**Potential solution:**

The command `elcl.exe` will only work once the eye-tracker device is physically connected to the ET PC. Ensure the ET device cable is plugged in inside the scanner room before running the command. If the error persists, try running the command again after confirming the connection.

!!! tip "Reference"
    See [Session preparation — Set up the ET system](../debi/data-collection/1_session_prep.md#set-up-the-et-system).

---

### Problem 8: IDEA UI freezes when loading a Pulseq sequence

The IDEA UI becomes unresponsive after attempting to load a Pulseq `.seq` file.

**Potential solution:**

This is caused by failing to disable the **"libBalance / Grad health"** option before loading the sequence. Always set this option to *disabled* first, then select your sequence from the Pulseq file list.

!!! warning "Order of operations"
    See [Run scanning session — Load the Pulseq files](../debi/data-collection/2_run_scanning_session.md#load-the-pulseq-seq-files) for the correct sequence of steps.

---

### Problem 9: Wrong coils are selected after copying parameters between sequences

After copying parameters from a head-coil (HC) sequence to a body-coil (BC) sequence, the BC scan uses the coils from the HC sequence.

**Potential solution:**

When using *Copy Parameters* (including *Adjustment Volume*) from an HC sequence to a BC sequence, the coil selection is also copied. After copying, manually go to **System > Coils** and re-select the correct coils for the BC sequence (i.e., select *Body*).

!!! warning "Reference"
    This is noted in [Run scanning session](../debi/data-collection/2_run_scanning_session.md#modify-some-system-parameters).
