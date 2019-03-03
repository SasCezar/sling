import logging
import os
import sys
import pandas as pd


def read_evaluations(path):
    scores = {}
    with open(path, "rt", encoding="utf8") as inf:
        for line in inf:
            metric, score = line.split("=")
            if "LABEL_" in metric:
                continue
            scores[metric] = float(score)

    return score


def creat_table(experiments):
    results = []
    for path, exp in experiments:
        scores = read_evaluations(path)
        experiment_name, remaining = exp.split("-")
        scores["experiment"] = experiment_name
        langs = experiment_name.split("_")[0].split("-")
        target = langs[-1]
        del langs[-1]
        scores["source"] = "_".join(langs) if langs else ""
        scores["target"] = target
        scores["wiki"] = 1 if "wiki" in experiment_name else 0

        target_size = experiment_name.split("_")[-1]
        scores["target_size"] = int(target_size)

        results.append(scores)

    return pd.DataFrame(results)


def extract_results(in_path, out_path):
    experiments_simplified_test = [(d, os.path.join(in_path, d)) for d in os.listdir(in_path) if
                                   os.path.isdir(os.path.join(in_path, d)) if "simplified" in d and "test" in d]
    experiments_simplified_dev = [(d, os.path.join(in_path, d)) for d in os.listdir(in_path) if
                                  os.path.isdir(os.path.join(in_path, d)) if "simplified" in d and "dev" in d]
    experiments_full_test = [(d, os.path.join(in_path, d)) for d in os.listdir(in_path) if
                             os.path.isdir(os.path.join(in_path, d)) if "full" in d and "test" in d]
    experiments_full_dev = [(d, os.path.join(in_path, d)) for d in os.listdir(in_path) if
                            os.path.isdir(os.path.join(in_path, d)) if "full" in d and "dev" in d]

    table = creat_table(experiments_full_dev)
    table.to_csv(os.path.join(out_path, "scores_full_dev.csv"))
    table.to_latex(os.path.join(out_path, "latex_scores_full_dev.txt"))

    creat_table(experiments_full_test)
    table.to_csv(os.path.join(out_path, "scores_full_test.csv"))
    table.to_latex(os.path.join(out_path, "latex_scores_full_test.csv"))

    creat_table(experiments_simplified_dev)
    table.to_csv(os.path.join(out_path, "scores_simplified_dev.csv"))
    table.to_latex(os.path.join(out_path, "latex_scores_simplified_dev.csv"))

    creat_table(experiments_simplified_test)
    table.to_latex(os.path.join(out_path, "scores_full_test.csv"))


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("Running %s", " ".join(sys.argv))
    in_path = sys.argv[1]
    out_path = sys.argv[2]

    extract_results(in_path, out_path)

    logging.info("Completed %s", " ".join(sys.argv))
