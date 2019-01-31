import json
import logging
import sys
from itertools import chain
from os import listdir
from os.path import isfile, join
from shutil import copyfile

from nlp.parser.ontonotes import experiments
from nlp.parser.ontonotes.merge_datasets import random_combine


def load_experiment_config(path):
  with open(path, "r") as inf:
    configs = json.load(inf)

  return configs


train_strings = ["train"]
dev_strings = ["development"]
test_strings = ["test", "evaluation"]


def filter_file(files, strings, langs):
  return [f for f in files if any([True for s in strings if s in f]) and any([True for s in langs if s in f])]


def load_files(in_path, source_langs, target_lang):
  files = [f for f in listdir(in_path) if isfile(join(in_path, f))]
  training = filter_file(files, train_strings, source_langs)
  dev = filter_file(files, dev_strings, target_lang)
  test = filter_file(files, test_strings, target_lang)

  return training, dev, test


def write_ids(out_path, set_name, files):
  with open(join(out_path, set_name + ".ids"), "w") as outf:
    for f in files:
      outf.write("/".join(["data", "english", "annotations", f]) + "\n")


def create_ids_files(out_path, training, dev, test):
  write_ids(out_path, "train", training)
  write_ids(out_path, "dev", dev)
  write_ids(out_path, "test", test)


def create_dataset(in_path, out_path, experiment_name, config):
  # training, dev, test = load_files(in_path, config['source_langs'], config['target_lang'])
  training = config[experiment_name]['training']
  dev = config[experiment_name]['dev']
  test = config[experiment_name]['test']

  data_path = join(*[out_path, "data", "english", "annotations"])

  training_file = "train.gold_conll"
  random_combine(training, join(data_path, training_file))

  create_ids_files(out_path, training_file, dev, test)

  for f in chain(dev, test):
    src = join(in_path, f)
    dst = join(data_path, f)

    copyfile(src, dst)


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  in_path = sys.argv[1]
  out_path = sys.argv[2]
  experiment_name = sys.argv[3]

  create_dataset(in_path, out_path, experiment_name, experiments.EXPERIMENTS[experiment_name])

  logging.info("Completed %s", " ".join(sys.argv))
