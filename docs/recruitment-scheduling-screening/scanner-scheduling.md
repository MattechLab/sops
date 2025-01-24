
- [ ] Iteratively draw participants from the recruitment shortlist and call them back to set their first session.

    !!!danger "Stop calling potential participants when the sample size has been achieved"
        Once the sample size is filled (e.g., 3M/3F for Cohort II), call the remainder of the participants
        in the shortlist to let them know that they have been moved into the wait list.

- [ ] The first session will always happen at MRI 1 (Prisma<sup>Fit</sup>, {{ secrets.rooms.mri1 | default("███") }})

## Scheduling of the Prisma<sup>Fit</sup> system ({{ secrets.rooms.mri1 | default("███") }})

!!! info "Contact {{ secrets.people.mri_coordinator_cibm | default("███") }}, MRI Operational Manager, for any doubts/problems regarding this system"

- [ ] Open the {{ secrets.scheduling.name | default("███") }} scheduling system ([URL]({{ secrets.scheduling.url | default("/redacted.html") }})) on a browser.
- [ ] With the participant on the phone, find a suitable, empty slot by scrolling the calendar.
- [ ] Click on the preferred slot, make sure that selected resource is *{{ secrets.scheduling.resource_prisma | default("███") }}*
- [ ] Select *{{ secrets.people.mri_operator | default("███") }}* in the Operator dropdown menu.
- [ ] Select the adequate length for the session (120 minutes)
- [ ] Select *Research on healthy subjects* in the Type of Scan box.
- [ ] Select *true* in Technician Required if you are not a certified operator of the system.

## Scheduling of the Vida<sup>Fit</sup> system ({{ secrets.rooms.mri3 | default("███") }})

!!! info "Contact {{ secrets.people.mri_coordinator_chuv | default("███") }}, Technical MRI Coordinator, for any doubts/problems regarding this system"

- [ ] Open the {{ secrets.scheduling.name | default("███") }} scheduling system ([URL]({{ secrets.scheduling.url | default("/redacted.html") }})) on a browser.
- [ ] With the participant on the phone, find a suitable, empty slot by scrolling the calendar.

    !!! warning "Clinical scanner hours are very restricted"
        The study can only be executed on Fridays after 18h00

- [ ] Click on the preferred slot, make sure that selected resource is *{{ secrets.scheduling.resource_vidafit | default("███") }}*
- [ ] Select *{{ secrets.people.mri_operator_clinical | default("███") }}* in the Operator dropdown menu.
- [ ] Select the adequate length for the session (60 minutes)
- [ ] Select *Research on healthy subjects* in the Type of Scan box.
- [ ] Select *true* in Technician Required.

## Scheduling of the Vida system ({{ secrets.rooms.mri2 | default("███") }})

!!! danger "Only {{ secrets.people.mri_coordinator_chuv | default("███") }}, Technical MRI Coordinator, can book this system."
