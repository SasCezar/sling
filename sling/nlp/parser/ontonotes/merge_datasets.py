import logging
import math
import os
import random
import sys


def merge_doc_sentences(file):
  docs = []
  doc = ""
  for row in file:
    if not row.strip():
      continue
    if row.startswith("#task_id") and doc:
      docs.append(doc)
      doc = ""
    doc += row.strip() + "\n"

  return docs


def combine(in1, in2, out):
  with open(in1, "rt", encoding="utf8") as inf1, \
    open(in2, "rt", encoding="utf8") as inf2:
    file1 = [row.strip() for row in inf1 if not (row.startswith("#begin") or row.startswith("#end")) or row.strip()]
    file1 = merge_doc_sentences(file1)
    file2 = [row.strip() for row in inf2 if not (row.startswith("#begin") or row.startswith("#end")) or row.strip()]
    file2 = merge_doc_sentences(file2)

  files = [file1, file2]
  files_len = [len(file) for file in files]
  max_len = max(files_len)
  max_len_i = files_len.index(max_len)
  min_len = min(files_len)
  min_len_i = files_len.index(min_len)

  res = []
  n = math.floor(files_len[max_len_i] / files_len[min_len_i])
  print(n)
  f_max = iter(files[max_len_i])
  for m in files[min_len_i]:
    res.extend([next(f_max) for _ in range(0, n)])
    res.append(m)
  # res.extend(f_max)

  with open(out, "wt", encoding="utf8") as outf:
    file = os.path.basename(out)
    outf.write("#begin document ({});\n".format(file))
    for line in res:
      if line.strip():
        outf.write(line + "\n")
    outf.write("#end document")


def read_examples(file, limit):
  with open(file, "rt", encoding="utf8") as inf1:
    rows = [row.strip() for row in inf1 if not (row.startswith("#begin") or row.startswith("#end")) or row.strip()]
    examples = merge_doc_sentences(rows)

  return examples[:limit]


def write(examples, out):
  with open(out, "wt", encoding="utf8") as outf:
    file = os.path.basename(out)
    outf.write("#begin document ({});\n".format(file))
    for line in examples:
      if line.strip():
        outf.write(line + "\n")
    outf.write("#end document")


def random_combine(files, out):
  examples = []
  files = [(file, int(limit)) for file, limit in zip(files[:-1:2], files[1::2])]
  print(files)
  for file, limit in files:
    ex = read_examples(file, limit)
    assert len(ex) == limit, "{} - {}".format(len(ex), limit)
    examples.extend(ex)

  random.shuffle(examples)

  write(examples, out)


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  out_path = sys.argv[1]
  files = sys.argv[2:]
  random_combine(files, out_path)
  logging.info("Completed %s", " ".join(sys.argv))
