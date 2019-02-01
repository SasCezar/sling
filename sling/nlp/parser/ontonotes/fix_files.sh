#!/usr/bin/env bash

FOLDER_IN=$1
task=$2
lang=$3
simplify=$4

for filename in $FOLDER_IN/*
do
    fileout="${filename/.txt/}"
    python fix_conll_2009to2012.py $filename $fileout $task $lang $simplify
done
