import logging
import math
import sys


def combine(in1, in2, out):
  with open(in1, "rt", encoding="utf8") as inf1, \
    open(in2, "rt", encoding="utf8") as inf2:
    file1 = [row.strip() for row in inf1 if not (row.startswith("#begin") or row.startswith("#end")) or row.strip()]
    file2 = [row.strip() for row in inf2 if not (row.startswith("#begin") or row.startswith("#end")) or row.strip()]

  files = [file1, file2]
  files_len = [len(file) for file in files]
  max_len = max(files_len)
  max_len_i = files_len.index(max_len)
  min_len = min(files_len)
  min_len_i = files_len.index(min_len)

  res = []
  n = math.floor(files_len[max_len] / files_len[min_len])
  for m in files[min_len_i]:
    res.extend([next(files[max_len_i]) for _ in range(n - 1)])
    res.append(m)
  res.extend(files[max_len_i])

  with open(out, "wt", encoding="utf8") as outf:
    for line in res:
      outf.write(line)


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  in1_path = sys.argv[1]
  in2_path = sys.argv[2]
  out_path = sys.argv[3]
  combine(in1_path, in2_path, out_path)
  logging.info("Completed %s", " ".join(sys.argv))
