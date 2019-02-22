#!/bin/bash
#SBATCH --job-name=W-SRL-FL
#number of independent tasks we are going to start in this script
#SBATCH --ntasks=1
#number of cpus we want to allocate for each program
#SBATCH --cpus-per-task=8
#SBATCH --time=6-00:00:00
#SBATCH --mem=16GB

./make_experiment_long.sh ~/datasets_full/ ~/experiments_full/ $1 ~/experiments_full/results/
