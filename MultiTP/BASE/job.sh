#!/bin/bash
#SBATCH --ntasks=8               # total number of tasks across all nodes
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=4G       # memory per cpu-core (4G is default)
#SBATCH --time=24:00:00          # total run time limit (HH:MM:SS)
#SBATCH --job-name="TEMPERATURE_PRESSURE" 

module purge
module load anaconda3/2023.3
conda activate /tigress/yifanl/usr/licensed/anaconda3/2021.11/envs/pytest

############################################################################
# Run
############################################################################
srun --mpi=pmix lmp -in start.lmp

date
