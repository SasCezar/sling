import csv
import logging
import sys


def fix_conll(in_path, out_path, task_id, lang_id, simplify):
  with open(in_path, "rt") as inf, open(out_path, "wt") as outf:
    writer = csv.writer(outf, delimiter=" ", quoting=csv.QUOTE_NONE, quotechar='')
    verb_count = 0
    for line in inf:
      is_verb = False
      verb_column = -1
      if line.startswith("#"):
        outf.write(line.strip() + "\n\n")
        continue

      row = line.split()
      n = len(row)
      if not row:
        verb_count = 0
        writer.writerow([])
        continue

      if row[2] == '0':
        writer.writerow(["#task_id:", "<{}>".format(task_id)])
        writer.writerow(["#lang_id:", "<{}>".format(lang_id)])

      if row[7] != "-" and "." in row[7]:
        row[7] = row[7].split('.')[1]

      if row[7] != "-":
        is_verb = True
        verb_count += 1
        verb_column = verb_count - 1 + 11

      for i in range(11, n - 1):
        if row[i] != '*':
          size = len(row[i])
          if row[i][size - 2] != '*':
            row[i] = row[i].replace(")", "*)")

        if is_verb and i != verb_column:
          row[i] = "*"

        if is_verb and i == verb_column:
          row[i] = "(V*)" if "V" in row[i] else "(v*)"

        if row[i].startswith("(A"):
          row[i] = row[i].replace("(A", "(ARG")
        if row[i].startswith("(R-A"):
          row[i] = row[i].replace("(R-A", "(ARG")
        if row[i].startswith("(C-A"):
          row[i] = row[i].replace("(C-A", "(ARG")

        if simplify and "-" in row[i]:
          suffix = "*)" if "*)" in row[i] else "*"
          row[i] = row[i].split("-")[0] + suffix

        row[i] = row[i].upper()
      writer.writerow(row)


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  in_path = sys.argv[1]
  out_path = sys.argv[2]
  task_id = sys.argv[3]
  lang_id = sys.argv[4]
  simplify = bool(int(sys.argv[5])) if len(sys.argv) == 6 else False
  fix_conll(in_path, out_path, task_id, lang_id, simplify)
  logging.info("Completed %s", " ".join(sys.argv))
