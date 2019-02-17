#!/usr/bin/env bash

SRL_FILES=$1
OUT_FOLDER=$2
EXP_NAME=$3
RES_FOLDER=$4

if [[ ! -e $OUT_FOLDER ]]; then
    mkdir $OUT_FOLDER
    mkdir $OUT_FOLDER/data/english/annotations
fi

source deactivate
cd ./sling/nlp/parser/ontonotes/
python create_dataset.py $SRL_FILES $OUT_FOLDER $EXP_NAME 1
cd -
