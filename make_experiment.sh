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
python create_dataset.py $SRL_FILES $OUT_FOLDER $EXP_NAME
cd -

source activate venv/
./sling/nlp/parser/ontonotes/make_corpus.sh $OUT_FOLDER/$EXP_NAME $EXP_NAME

pwd
./sling/nlp/parser/tools/train.sh \
    --train=./local/data/corpora/caspar/$3/train.rec \
    --dev=./local/data/corpora/caspar/$3/dev.rec \
    --output=$4/$3/ \
    --word_embeddings=./local/data/corpora/sempar/wiki.multi.en-es.vec \
    --batch 8 \
    --report_every 1000