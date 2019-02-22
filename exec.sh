#!/bin/bash
#SBATCH --job-name=W-SRL
#number of independent tasks we are going to start in this script
#SBATCH --ntasks=1
#number of cpus we want to allocate for each program
#SBATCH --cpus-per-task=8
#SBATCH --time=6-00:00:00
#SBATCH --mem=16GB

./make_experiment.sh ~/datasets/ ~/experiments/ $1 ~/experiments/results/

