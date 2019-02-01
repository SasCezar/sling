import json
import logging
import os
import sys
from itertools import chain
from os.path import join
from shutil import copyfile

import experiments
from merge_datasets import random_combine


def load_experiment_config(path):
  with open(path, "rt", encoding="utf8") as inf:
    configs = json.load(inf)

  return configs


def write_ids(out_path, filename, files):
  with open(join(out_path, filename), "wt", encoding="utf8") as outf:
    for f in files:
      outf.write("/".join(["data", "english", "annotations", f]) + "\n")


def create_ids_files(out_path, training, dev, test):
  write_ids(out_path, "train.ids", training)
  write_ids(out_path, "dev.ids", dev)
  write_ids(out_path, "test.ids", test)


def create_dataset(in_path, out_path, config):
  training = [(join(in_path, f), k) for f, k in config['train']]
  dev = config['dev']
  test = config['test']

  data_path = join(*[out_path, "data", "english", "annotations"])
  if not os.path.exists(data_path):
    os.makedirs(data_path)

  training_file = "train.gold_conll"
  random_combine(training, join(data_path, training_file))

  create_ids_files(out_path, [training_file], dev, test)

  for f in chain(dev,test):
    src = join(in_path, f)
    dst = join(data_path, f)

    copyfile(src, dst)


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  in_path = sys.argv[1]
  print(in_path)
  out_path = sys.argv[2]
  experiment_name = sys.argv[3]
  out_path = join(out_path, experiment_name)

  if not os.path.exists(out_path):
    os.makedirs(out_path)

  create_dataset(in_path, out_path, experiments.EXPERIMENTS[experiment_name])

  logging.info("Completed %s", " ".join(sys.argv))
