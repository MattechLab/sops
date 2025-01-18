- DICOM from standard clinical protocols: spm12 ->reslicing and registration
revise the codes.
- raw data from MR-Eye or MR_Track protocols: binning with ET masks -> Compressed sensing recon

## 1 Reconstruction from raw data
For the motion-resolved task, a binning mask must be manually generated, and image reconstruction is performed using the Monalisa toolkit, which supports non-Cartesian trajectories of the T1w/T2w-LIBRE protocol. The reconstruction results are typically saved in .mat format.

Given that the matrix size of T1w/T2w-LIBRE is 480, the reconstruction process requires computational resources and should be executed on Debi or the HES-SO server.

The practical steps for reconstructing the data are as follows:
### Prepare raw data path on Debi
To accelerate data processing, we can first prepare a list of all raw data paths required for the upcoming reconstruction.
```matlab
reconDir = '/path/to/recon/folder';

% Subject 001
/path/to/raw/data/Subject001/RawData/
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_T2_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_BC_BC.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_HC_BC.dat

% Subject 002
/path/to/raw/data/Subject002/RawData/
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_T2_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_BC_BC.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_HC_BC.dat

% Subject 003
/path/to/raw/data/Subject003/RawData/
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_T2_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_BC_BC.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_HC_BC.dat

% Subject 004
/path/to/raw/data/Subject004/RawData/
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_T2_eye.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_BC_BC.dat
meas_MIDxxxx_FIDxxxxx_BEAT_LIBREon_eye_HC_BC.dat
```
### Load all the raw data files 
It is important to consider the number of channels (nCh), as it may vary across different subjects and acquisitions. 
Additionally, make sure to record the duration of the raw data by examining the PMU, as this information will be crucial for the subsequent binning process.
```matlab
%Sub001
N     = 480 
nSeg  = 22 
nShot = 1000 
nLine = 22000 
nPar  = 1 
nCh   = 42 
nEcho = 1 
The duration of the rawdata is: 650185 ms with data points:22000

%Sub002
N     = 480 
nSeg  = 22 
nShot = 1000 
nLine = 22000 
nPar  = 1 
nCh   = 44 
nEcho = 1 
The duration of the rawdata is: 650185 ms with data points:22000

```
### Generate ET masks

- Synchronize the eye-tracking (ET) data with the MRI readouts using the trigger information. 
- Once the criteria for selecting the ET data have been established, we will generate an ET mask that matches the duration of the MRI readout.
  For instance, if the raw data duration is 650,185 ms, as determined in a previous step, and the ET sampling rate is 1 kHz, an ET mask with a length of 650,185 samples can be generated after identifying the start timestamp of the ET data.

- Save the generated ET mask in .mat format.

Further details on generating the ET mask and saving it will be provided in Section <mark>ref()<mark>.

### Binning the raw data according to ET masks.
- For the raw data, we first eliminate the SI projection of raw data by setting the corresponding mask elements to a value of 0. 
- Then we will bin the data according to the ET mask. 
    - Given that the repetition time (TR) is 8.01 ms for T1w-LIBRE and 29.14 ms for T2w-LIBRE, each MRI readout corresponds to approximately 8 ET points for T1w and 29–30 ET points for T2w. 
    - Based on this, we apply a sliding window with a length of roughly three times the TR: 30 points for T1w and 90 points for T2w.
    - Within each window, we calculate the number of valid ET mask points (where the value = 1, indicating that the gaze point falls within the selected central range of the screen). If the number of valid points exceeds the user-defined threshold—set as 3/4 of the window length in our case—the corresponding MRI readout is preserved; otherwise, it is excluded.
- Finally, we generate a binned mask that selects only the readouts unaffected by significant eye movements.
- Record the number of readouts remaining after binning for each subject and each derivative method. For example:

```matlab
Subject 001 with Binning, preserved #line: 17314 out of 22000

Subject 002 with Binning, preserved #line: 9573 out of 22000

Subject 003 with Binning, preserved #line: 15322 out of 22000

Subject 004 with Binning, preserved #line: 8835 out of 22000
```
If the preserved number of readouts are less than 10k, we will expect a low quality of reconstructed images.

### Create Mitosius

If you are working on the HES-SO server, the dataset can be directly mounted from the data storage server, making it most efficient to run Mitosius directly on the server.

If you are using an HPC and need to transfer data, it is recommended to create the Mitosius folder locally first and then upload the folder to the HPC instead of transferring the raw data.

The scripts about how to use mitosius please refer to the [Monalisa document](https://mattechlab.github.io/monalisa/2-3_mitosius_prepare.html).

### Recon function
In our reconstruction, we utilize `Steva` function for Single-frame Least-square Regularized Reconstruction, where reularizaiton is the l1-norm of spatial gradient of the image.
The reconstructed results are in the format of `**.mat`.
You can find more details in the [Monalisa document](https://mattechlab.github.io/monalisa/2-2_reconstruction_calls.html#steva).


## 2 Pipeline for processing Dicom
Whereas, the recon results from standard clinical protocols are in DICOM format, directly exported from scanner PC.
 
-  Convert Dicom to .nii files: download the [MRIcroGL](https://people.cas.sc.edu/rorden/mricron/dcm2nii.html) software.
   - Download and install the software.
   - prepare the nifti folder under the Dicom folder.
   `MRICron.exe >> import >> Dcm2nii >> uncompressed NifTi (.nii)`
-  Inspect the .nii files: 
   - Prepare [spm](https://www.fil.ion.ucl.ac.uk/spm/docs/installation/) software on the laptop.
   - Open spm -> display buttons
- Coregister: Estimate & Reslice.
  Coregister the DICOM results from the standard clinical protocol with those from LIBRE. Although the DICOM result from LIBRE will not be used for further analysis, it serves as a reference image, allowing us to transform the clinical protocol image to the same spatial domain as LIBRE for subsequent comparison.

```matlab
addpath('/Users/cag/Documents/forclone/spm')
%%

% Define image paths

nii_folder = '/path/to/NIFTI_NII_origin/';
% Libre image
a_image_name = 'DICOM_BEAT_LIBREon_eye.nii';
% Vibe image
b_image_name = 'DICOM_t1_vibe.nii'; 

a_image = fullfile(nii_folder, a_image_name);
b_image = fullfile(nii_folder, b_image_name);

%% Inspect the header before co-registration
V_a_1 = spm_vol(a_image);
disp('V_a_1'); disp(V_a_1);
V_b_1 = spm_vol(b_image);
disp('V_b_1'); disp(V_b_1);

% Co_register
co_register(b_image, a_image)

% Inspect the header after co-registration
V_a_2 = spm_vol(a_image);
disp('V_a_2'); disp(V_a_2);
V_b_2 = spm_vol(b_image);
disp('V_b_2'); disp(V_b_2)

disp(['V_b remains the same? ', num2str(isequal(V_b_1.mat, V_b_2.mat))])
%%
%---------------------------------------------
% Reslicing part
%---------------------------------------------
reslicing(b_image, a_image)


```





