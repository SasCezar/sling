#!/usr/bin/env bash
#
# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script for converting a Ontonotes like file to a SLING corpus
# that can be used for training and testing a SLING parser.
#
# The OntoNotes SLING corpus will end up in local/data/corpora/caspar.

set -e
ONTONOTES=$1

echo "Convert CoNLL files to SLING"

CONVERTER=sling/nlp/parser/ontonotes/ontonotesv5_to_sling.py
IN=$ONTONOTES/data
OUT=local/data/corpora/caspar/$2

mkdir -p $OUT

python $CONVERTER \
  --input=$IN/ \
  --allowed_ids=$ONTONOTES/train.ids \
  --output=$OUT/train.rec

python $CONVERTER \
  --input=$IN/ \
  --allowed_ids=$ONTONOTES/dev.ids \
  --output=$OUT/dev.rec

python $CONVERTER \
  --input=$IN/ \
  --allowed_ids=$ONTONOTES/test.ids \
  --output=$OUT/test.rec

echo "Done."