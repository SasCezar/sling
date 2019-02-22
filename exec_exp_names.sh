# while read FILE; do sleep 30; sbatch exec.sh $FILE; done < exp_names.txt
while read FILE; do sleep 30; sbatch exec_full.sh $FILE; done < exp_names.txt
