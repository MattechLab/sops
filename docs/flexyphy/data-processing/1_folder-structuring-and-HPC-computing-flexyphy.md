## Folder Structure and HPC Computing

This SOP describes how to organize the raw Flexyphy data and how to run the reconstruction pipeline on the HPC. Paths in this page are written relative to the released repository root unless otherwise stated. The reconstruction scripts used for the current analysis are stored at:

```text
code/HPC
```

The pipeline is designed to run inside an Apptainer/Singularity container with MATLAB, Monalisa, Pulseq, and SPM available on the MATLAB path. Processing is parallelized at the subject level by submitting one SLURM job per subject.

---

## 1. Required Folder Structure

The MATLAB scripts assume the following folder structure. The `raw` folders must exist before processing starts. The `derivatives` folders are created by the reconstruction scripts.

```text
study_root
├── sub-01
│   ├── raw
│   │   ├── gre
│   │   │   ├── original
│   │   │   │   ├── meas_name.dat
│   │   │   │   └── seq_name.seq
│   │   │   ├── uniform
│   │   │   │   ├── meas_name.dat
│   │   │   │   └── seq_name.seq
│   │   │   ├── flexiphy
│   │   │   │   ├── meas_name.dat
│   │   │   │   └── seq_name.seq
│   │   │   └── prescans
│   │   │       ├── meas_name_BC.dat
│   │   │       ├── meas_name_HC.dat
│   │   │       └── seq_name.seq
│   │   └── libre
│   │       ├── original
│   │       ├── uniform
│   │       ├── flexiphy
│   │       └── prescans
│   └── derivatives
│       ├── gre
│       │   ├── coilSense
│       │   │   ├── coilSens_lowres.mat
│       │   │   └── roiMask_lowres.mat
│       │   ├── original
│       │   │   ├── motion_correction
│       │   │   │   └── meas_name
│       │   │   │       ├── x_cs_tres3p5s_Nu120x120x120_delta5.mat
│       │   │   │       ├── rp_spm_x_cs_tres3p5s_Nu120x120x120_delta5.txt
│       │   │   │       └── normalization.mat
│       │   │   └── meas_name
│       │   │       ├── normalization.mat
│       │   │       ├── normalization_moco.mat
│       │   │       ├── x0_1bin.mat
│       │   │       ├── x0_4bins.mat
│       │   │       ├── x0_1bin_moco.mat
│       │   │       └── x0_4bins_moco.mat
│       │   ├── uniform
│       │   └── flexiphy
│       └── libre
│           ├── coilSense
│           ├── original
│           ├── uniform
│           └── flexiphy
└── sub-02
    └── ...
```

Naming assumptions:

- each main-scan trajectory folder contains exactly one `.dat` file and exactly one `.seq` file;
- each `prescans` folder contains exactly one prescan `.seq` file;
- the body-coil prescan `.dat` filename contains `BC`;
- the head-coil prescan `.dat` filename contains `HC`;
- subject folders are named `sub-*`, for example `sub-01`.

At execution time, the job file binds `study_root` to the container path `/data`, so the MATLAB scripts see the study root as:

```matlab
rootDir = '/data';
```

---

## 2. Software Requirements

The HPC environment must provide:

- SLURM for job scheduling;
- Apptainer or Singularity for container execution;
- the Monalisa container image;
- the reconstruction code folder;
- a local clone of Pulseq;
- a local clone of SPM.

Clone the external dependencies in an HPC-accessible location:

```bash
mkdir -p external
git clone https://github.com/spm/spm.git external/spm
git clone https://github.com/pulseq/pulseq.git external/pulseq
```

The current reconstruction code is part of the release repository under `code/HPC`. The SLURM job binds this folder to `/code` inside the container.

---

## 3. Container Preparation

Pull the Monalisa Docker image and convert it to a SIF file:

```bash
singularity pull --docker-login ./monalisa.sif docker://yiwei99/monalisa_251215:latest
```

On systems where the command is named `apptainer`, the equivalent command is:

```bash
apptainer pull --docker-login ./monalisa.sif docker://yiwei99/monalisa_251215:latest
```

The container is later run with the following bind mounts:

```text
./data/study      -> /data    root study folder containing sub-* folders
./code/HPC        -> /code    Flexyphy HPC MATLAB reconstruction code
./external/pulseq -> /pulseq  Pulseq repository
./external/spm    -> /spm     SPM repository
```

---

## 4. SLURM Job File

Use one job per subject. The current job file is `code/HPC/flexiphy_jobfile.sh`. Run the submission command from the released repository root.

```bash
#!/bin/bash
#SBATCH --job-name=flexy_final
#SBATCH --partition=Dance
#SBATCH --cpus-per-task=8
#SBATCH --mem=90G
#SBATCH --time=48:00:00
#SBATCH --output=logs/flexy_final%j.out
#SBATCH --error=logs/flexy_final%j.err

subj=$1

STUDY_ROOT="${STUDY_ROOT:-./data/study}"
PULSEQ_ROOT="${PULSEQ_ROOT:-./external/pulseq}"
SPM_ROOT="${SPM_ROOT:-./external/spm}"
MONALISA_SIF="${MONALISA_SIF:-./monalisa.sif}"

echo "========================================"
echo "Job started on $(date)"
echo "Processing subject: $subj"
echo "Node: $(hostname)"
echo "CPUs: $SLURM_CPUS_PER_TASK"
echo "========================================"

apptainer exec --cleanenv \
  --writable-tmpfs --fakeroot \
  --bind "${STUDY_ROOT}:/data" \
  --bind "./code/HPC:/code" \
  --bind "${PULSEQ_ROOT}:/pulseq" \
  --bind "${SPM_ROOT}:/spm" \
  "${MONALISA_SIF}" \
  matlab -nodisplay -nosplash -r "addpath(genpath('/code')); try, main_recon_container('$subj'), catch ME, disp(ME.message), exit(1), end, exit(0);"

echo "========================================"
echo "Job finished on $(date)"
echo "========================================"
```

Before running, update:

- `--partition` to match the cluster partition;
- `--mem` and `--time` if the reconstruction fails because of memory or wall-time limits;
- `STUDY_ROOT`, if the study data are not stored under `./data/study`;
- `PULSEQ_ROOT` and `SPM_ROOT`, if the external repositories are not stored under `./external`;
- `MONALISA_SIF`, if the Monalisa image is not stored as `./monalisa.sif`.

Submit one subject with:

```bash
sbatch code/HPC/flexiphy_jobfile.sh sub-01
```

Submit all available subjects with a shell loop, adapting the subject list to the dataset:

```bash
for subj in sub-01 sub-02 sub-03; do
  sbatch code/HPC/flexiphy_jobfile.sh "$subj"
done
```

---

## 5. MATLAB Entry Point

The SLURM job starts MATLAB inside the container and calls:

```matlab
main_recon_container(subject)
```

Inside the container, the entry point sets:

```matlab
rootDir = '/data';
```

It then adds the required paths:

```matlab
addpath(genpath('/code'));
addpath(genpath('/usr/src/app/src'));
addpath(genpath('/usr/src/app/third_part'));
addpath(genpath('/pulseq'));
addpath(genpath('/spm'));
```

The script also recompiles the Monalisa MEX files by calling:

```matlab
compile_mex_for_monalisa();
```

Before running a full reconstruction campaign, open `code/HPC/main_recon_container.m` and verify which steps are uncommented. The script is often edited during development to rerun only selected stages.

For a full reconstruction, the intended subject-level sequence is:

```matlab
step0_check_orientation(rootDir, subject);
step1_coil_sens(rootDir, subject);
step2_recon_mathilda(rootDir, subject);
step3_recon_sequential(rootDir, subject, 3.5);
step4_estimate_motion(rootDir, subject);
step5_recon_mathilda_moco(rootDir, subject);
```

Run group-level metrics once after all subjects have completed:

```matlab
step6_group_metrics(rootDir);
```

---

## 6. Processing Steps and Outputs

### Step 0: Orientation Check

Script:

```matlab
step0_check_orientation(rootDir, subject)
```

Purpose:

- check that the body-coil prescan, head-coil prescan, and main scan have compatible orientations;
- stop reconstruction early if the prescan orientation is inconsistent with the main scan.

This step reads the prescan and main-scan TWIX files, creates Monalisa raw-data readers, and calls `checkPrescanOrientation()`.

### Step 1: Coil Sensitivity Estimation

Script:

```matlab
step1_coil_sens(rootDir, subject)
```

Purpose:

- compute one low-resolution coil sensitivity map per subject and sequence type;
- compute the corresponding low-resolution ROI mask;
- save both outputs under `derivatives/<sequence>/coilSense`.

Expected outputs:

```text
coilSens_lowres.mat
roiMask_lowres.mat
```

### Step 2: Non-Motion-Corrected Reconstruction

Script:

```matlab
step2_recon_mathilda(rootDir, subject)
```

Purpose:

- reconstruct all-lines images from the original raw data and trajectory;
- reconstruct four temporally sequential bins without sharing information between bins;
- save outputs for each sequence and trajectory.

Expected outputs in each scan derivatives folder:

```text
normalization.mat
x0_1bin.mat
x0_4bins.mat
```

The current reconstruction grid is `N_u = [240 240 240]`.

### Step 3: Sequential Reconstruction for Motion Estimation

Script:

```matlab
step3_recon_sequential(rootDir, subject, temporalRes, N_u, delta)
```

Typical call:

```matlab
step3_recon_sequential(rootDir, subject, 3.5, [120 120 120], 5)
```

Purpose:

- reconstruct temporally resolved images for motion estimation;
- normalize raw data within the ROI;
- compress coils with SVD while retaining 99.5% of signal energy;
- reconstruct a compressed-sensing temporal image series with temporal regularization.

Expected outputs under `derivatives/<sequence>/<trajectory>/motion_correction/<scan_name>`:

```text
normalization.mat
coilCompression.mat
x_cs_tres3p5s_Nu120x120x120_delta5.mat
```

The exact `x_cs` filename depends on `temporalRes`, `N_u`, and `delta`.

### Step 4: Motion Estimation

Script:

```matlab
step4_estimate_motion(rootDir, subject)
```

Purpose:

- read the sequential reconstruction from Step 3;
- write a NIfTI time series for SPM internally;
- register each temporal frame to the first frame with SPM realignment;
- save rigid-body motion parameters.

Expected output in the corresponding motion-correction folder:

```text
rp_spm_x_cs_tres3p5s_Nu120x120x120_delta5.txt
```

The motion vector format is:

```text
[Tx Ty Tz Rx Ry Rz]
```

where translations are in millimeters and rotations are in radians.

### Step 5: Motion-Corrected Reconstruction

Script:

```matlab
step5_recon_mathilda_moco(rootDir, subject)
```

Purpose:

- load raw data and original trajectory;
- load SPM motion parameters from Step 4;
- interpolate motion parameters to one estimate per k-space line;
- apply translation correction to the raw measurements;
- apply inverse rotation correction to the trajectory;
- reconstruct all-lines and four-bin motion-corrected images.

Expected outputs in each scan derivatives folder:

```text
normalization_moco.mat
x0_1bin_moco.mat
x0_4bins_moco.mat
```

### Step 6: Group Metrics

Script:

```matlab
step6_group_metrics(rootDir)
```

Purpose:

- loop over all `sub-*` folders;
- compare each four-bin image to the corresponding all-lines image;
- compute relative L2 distance and mean slice-wise SSIM;
- evaluate both non-motion-corrected and motion-corrected reconstructions.

Expected output:

```text
derivatives/group_analysis/recon_metrics/metrics_all_long.csv
```

Columns:

```text
subject, sequence, trajectory, scan, recon_type, bin, ssim, l2_rel
```

---

## 7. Quality-Control Checklist

After each subject-level job finishes, check the SLURM `.out` and `.err` files first. Then verify the following files exist:

```text
sub-XX/derivatives/gre/coilSense/coilSens_lowres.mat
sub-XX/derivatives/gre/coilSense/roiMask_lowres.mat
sub-XX/derivatives/<sequence>/<trajectory>/<scan>/x0_1bin.mat
sub-XX/derivatives/<sequence>/<trajectory>/<scan>/x0_4bins.mat
sub-XX/derivatives/<sequence>/<trajectory>/motion_correction/<scan>/x_cs_tres3p5s_Nu120x120x120_delta5.mat
sub-XX/derivatives/<sequence>/<trajectory>/motion_correction/<scan>/rp_spm_x_cs_tres3p5s_Nu120x120x120_delta5.txt
sub-XX/derivatives/<sequence>/<trajectory>/<scan>/x0_1bin_moco.mat
sub-XX/derivatives/<sequence>/<trajectory>/<scan>/x0_4bins_moco.mat
```

Common failure modes:

- missing or duplicated `.dat` or `.seq` files in a raw trajectory folder;
- prescan filenames that do not contain `BC` and `HC`;
- mismatched prescan and main-scan orientation;
- missing `coilSens_lowres.mat` or `roiMask_lowres.mat` before reconstruction;
- Step 3 filename mismatch, especially if `temporalRes`, `N_u`, or `delta` were changed;
- insufficient memory during 240 x 240 x 240 reconstruction.

---

## 8. Statistical Analysis and Plotting

After Step 6 produces `metrics_all_long.csv`, run the Python statistics notebook used for the study to:

- read the group-level metrics table;
- compute paired statistical tests across subjects;
- apply Bonferroni correction for multiple comparisons;
- generate the final metric plots.

Additional manuscript plots are generated from the notebooks in the project plotting folder.
