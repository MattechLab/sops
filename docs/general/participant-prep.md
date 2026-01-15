
!!!warning "Procedures for when the participant has arrived"
    It is critical to stay alert and anticipate any potential risk to the participant to avert them.
    This is particularly important for the first session.

## Participant reception
- [ ] Meet the participant at an easily locatable place (e.g., the reception desk of the Radiology Unit) and show them the way into the control room. <mark>Allow sufficient time before the experiment for the preparation (min. 30 minutes)</mark>.
- [ ] Show the participant the scanning room and explain to them how the device is controlled from outside.
- [ ] Ask the participant to fill out the consent form and MRI safety screener, and verbally confirm responses, paying attention to frequently forgotten devices and implants, like orthodontia.

    !!!danger "DO NOT subject the participant to any risk"
        - [ ] In case of any doubts emerging from the MRI safety screening, contact {{ secrets.people.medical_contact | default("███") }} immediately at :fontawesome-solid-square-phone: {{ secrets.phones.medical_contact | default("###-###-####") }}. <span style="color:red">**DO NOT PROCEED** if the medical contact cannot be reached</span>.
        - [ ] In case of discovering any previously undisclosed contraindication, the volunteer **MUST NOT** participate in the study.

---

## Preparation of the participant in the CONTROL ROOM

### Collecting participant's data

- [ ] Remind the participant to use the bathroom at this moment if they need.

!!!warning "Only female participants, only the first session"
    - [ ] Remind the participant that for their safety, pregnant women cannot participate:

        > Hey [NAME], I have to remind you that pregnant women cannot participate for their safety.
        >
        > To be absolutely sure that you are not scanned while being pregnant, the ethical review board requests us that you take a pregnancy test before the first session.
        > Here you have a test, and this is the urine sample cup.
        > I'm going to show you the bathroom now so that you can do the test with the necessary privacy.

    - [ ] Provide the participant with a pregnancy test and a urine sample cup.
    - [ ] Go over the instructions with them.
    - [ ] Accompany them to the bathroom (situated at {{ secrets.rooms.bathroom | default("███") }}), and ask whether there is anything else they anticipate they will need.
    - [ ] If the test is positive, the person **CANNOT PARTICIPATE** in the study.
        <mark>You MUST be understanding of the situation as most likely the person will not be aware of the circumstance</mark>.

- [ ] Instruct the participant on how to use the alarm button:

    ???+ quote "Alarm button should be used when needed"
        During the duration of the exam, you'll have an alarm button on your hand.
        You can use it at any moment.
        We will first talk with you to check everything is fine, and we will stop the session whenever you need to stop the experiment.
        There is no need for you to endure uncomfortable experiences or anxiety (for instance, if you feel claustrophobic)

### Describing the development of the session
- [ ] Describe the participant how the session will develop, with special attention to tasks. In the first session, show the task while explaining them for clarity. Let them interrupt you to ask for clarifications and answer all the questions that may arise.

    ???+ quote "Script for the first session"

        We are going to acquire...

        --- Give the instructions of the specific protocol ---

        Is everything clear to you? Do you have any questions?

### Finalizing the preparation
- [ ] Offer the participant a box to deposit everything they have in their pockets and all jewelry/hair accessories, and indicate the clothing to enter the scanning room:

    ??? quote "*Dress code* inside the scanner **if they need to CHANGE INTO SCRUBS**"
        Before we continue, we need to make sure we do not introduce any dangerous object in the magnet room.

        Here you will find a changing room [SHOW THEM THE CHANGING ROOM].
        I have prepared some scrubs for you.
        Please remove all your clothes and leave them in the changing room.
        Please keep your underwear on [if a woman, ask whether **their undergarment DOES NOT contain any large metallic part** such as shaping guides, and request their removal if they do].

    ???+ quote "*Dress code* inside the scanner **if they CAN WEAR THEIR CLOTHES**"
        Before we continue, we need to make sure we do not introduce any dangerous object in the magnet room.

        Please deposit here all your belongings, your belt, your glasses, your jewelry and any accessories, piercings, etc. that you have on you.
        If a woman, ask whether **their undergarment DOES NOT contain any large metallic part** such as shaping guides, and request their removal in the changing room.

## Installing the participant in the SCANNING ROOM

- [ ] Have the participant remove their shoes at the entrance of the scanning room.
- [ ] Show the alarm button to the participant and explain how they may use it.
- [ ] Give to the participant the emergency button. Make the participant try it, so they can see it works. To switch off the alarm, there's a button on the scanner (circular, both on the left and on the right of the hole)
- [ ] Give them the ear-plugs to protect their hearing during acquisition, allow time for them to place them.
- [ ] Instruct the participant to lay on the MRI bed.

### Accommodating the participant's head in the coil

- [ ] Adjust the participant inside. With the paddings, their head position MUST be adjusted and elevated so that the nose and the forehead of the participant are both close to the upper coil. This procedure ensures the ET has the clearest possible view of eye.
- [ ] This part must be repeated taking out and putting back the upper part of the head-coil, adjusting the pillow at every step, until the head is fixed and the nose and forehead of the participant almost touch the coil. In case of need, ask the participant to rotate their head like when *saying yes* until reaching an adequate position, place any remaining paddings.
- [ ] Take the side paddings and fit them between each ear and the coil. If using the inflatable padding, pump air into them without making the participant uncomfortable (check with them).
- [ ] Cut a long strip of medical auto-adhesive band and stick it at each side of the lower block of the head coil, across the participant's forehead and stick it to the participant's forehead. Indicate the participant that this band will tell them when they moved and help them recover the original position.
- [ ] Place the top block of the coil and check that the participants' front touches or is really close to the coil. Now the nose can also be a bit far from the coil. Tell the participant to relax the neck, so the nose should go a bit up and touch the coil.
- [ ] Connect the coil's cable to the corresponding socket on the table.
- [ ] Check that both the posterior and anterior parts of the head-and-neck coil are now detected:
    - [ ] Verify "Head Neck 64 Posterior" is listed on the scanner's monitor, and
    - [ ] Verify "Head Neck 64 Anterior" is listed in the scanner's monitor.
- [ ] Place rectangular paddings at each side of the chest and help the participant accommodate their elbows on them.
- [ ] Cover them with a blanket if necessary, and remind them of not closing loops with their body:

    !!! quote "Ask the participant if they are feeling cold"

        Hey [NAME], are you feeling cold? Do you want a blanket?

        I have placed some paddings for your elbows, is there anything else you would need to feel comfortable?

        Throughout the examination, remember not to create closed loops by crossing your legs or holding hands together.

- [ ] Insert the participant in the scanner [following the protocol](notes-scanning.md#participant-insertion).
- [ ] Once the participant is lying on the scanner bed, check that no arms/legs rest on the GA or the RB tubes and may block them.
- [ ] Before continuing with the setup, make sure all cables and tubes leave the scanner's bed *perpendicularly* and lie on the floor.
    Tape them to the floor so that they don't move accidentally.

---

## Final preparations

- [ ] Inform the participant that you are leaving the room and will shortly come back for a final preparation.
- [ ] Proceed with the [ET aiming and focusing protocol](et-related/notes-et.md#setting-viewframe-and-focusing).
- [ ] Inform the participant that you are leaving the room and will now close the door to start.
    Let them also know that you are going to communicate with them very shortly to check that communications through the speaker are functioning.
- [ ] Exit the Scanning Room.
- [ ] Close the Scanning Room door.
- [ ] Check the [communication with the participant](notes-scanning.md#communication-with-the-participant).

    ??? warning "Do not allow a delay before talking to the participant"

        Delays in establishing contact with the participant will likely increase their anxiety.

You can now move on to initiating the session for your specific protocol.
