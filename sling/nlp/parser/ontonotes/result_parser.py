import csv
import logging
import os
import re
import sys
from pandas import DataFrame

score_matcher = re.compile(r"\('(?P<measure>[#a-zA-Z_0-9+-]*)', (?P<value>\d*\.\d*)\)")

nex = re.compile(r"Eval metric after (?P<n_ex>\d*)")

loss_re = re.compile(
  r"BatchLoss after \((?P<n_batches>\d*) batches = (?P<examples>\d*) examples\): (?P<loss>\d*.\d*(e(\+|-)\d*)?)  incl\. L2= \[(?P<l2>\d*.\d*)\]")


def parse_file(log_file, experiment):
  with open(log_file, "rt", encoding="utf8") as inf:
    metrics = {}
    results = []
    loss_ts = []
    for line in inf:
      if line.startswith("BatchLoss after"):
        loss_matched = list(loss_re.finditer(line))[0]
        n_batches = loss_matched.group("n_batches")
        n_examples = loss_matched.group("examples")
        loss = loss_matched.group("loss")
        l2 = loss_matched.group("l2")
        loss_ts.append((experiment, int(n_batches), int(n_examples), float(loss), float(l2)))
      elif line.startswith("Evaluation Metric:"):
        matched = list(score_matcher.finditer(line))[0]
        measure = matched.group("measure")
        score = matched.group("value")
        metrics[measure] = score
      elif line.startswith("Eval metric after"):
        examples = list(nex.finditer(line))[0].group("n_ex")
        metrics["N_Examples"] = examples
        metrics["Experiment_Name"] = experiment
        results.append(metrics)
        metrics = {}
      else:
        continue

  df_results = DataFrame(results)
  return results, df_results, loss_ts


def extract_results(in_path, out_path):
  experiments = [d for d in os.listdir(in_path) if os.path.isdir(os.path.join(in_path, d))]
  all_results = []
  all_loss = []
  for experiment in experiments:
    log_file = os.path.join(*[in_path, experiment, "log"])
    res, results, loss = parse_file(log_file, experiment)
    all_results.extend(res)
    all_loss.extend(loss)

    results.to_csv(os.path.join(out_path, experiment + "_scores.csv"), index=False)

    with open(os.path.join(out_path, experiment + "_loss.csv"), "wt", encoding="utf8", newline="") as outf:
      writer = csv.writer(outf)
      writer.writerow(["Experiment Name", "N Batches", "N Examples", "Loss", "L2"])
      for l in loss:
        writer.writerow(l)

  all_results = DataFrame(all_results)
  all_results.to_csv(os.path.join(out_path,  "scores_all.csv"), index=False)

  with open(os.path.join(out_path, "loss_all.csv"), "wt", encoding="utf8", newline="") as outf:
    writer = csv.writer(outf)
    writer.writerow(["Experiment Name", "N Batches", "N Examples", "Loss", "L2"])
    for l in all_loss:
      writer.writerow(l)

if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  in_path = sys.argv[1]
  out_path = sys.argv[2]

  extract_results(in_path, out_path)

  logging.info("Completed %s", " ".join(sys.argv))
