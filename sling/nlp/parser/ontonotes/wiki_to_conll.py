import csv
import json
import logging
import os
import sys

import spacy


example = """{
	"entity": "Frobisher Bay",
	"entity_id": "Q1004067",
	"entity_locations": [0, 1],
	"entity_sequence": ["Frobisher", "Bay"],
	"id": "aac68aa23a09987ed067d4cd3280c2186cfef188",
	"lang": "en",
	"pos": ["NNP", "NNP", "VBZ", "VBN", "IN", "DT", "NNP", "NN", "NNP", "NNP", "NNP", ",", "WP", ",", "IN", "PRP$", "NN", "IN", "DT", "NNP", "NN", "IN", "CD", ",", "VBD", "DT", "JJ", "JJ", "TO", "VB", "PRP", "."],
	"relations": [{
			"answer": "Martin Frobisher",
			"answer_id": "Q80288",
			"answer_locations": [9, 10],
			"answer_sequence": ["Martin", "Frobisher"],
			"property_id": "P138",
			"property_label": "named after",
			"relation_id": "1d3550b18ac350d60cb672e6e9e41fb89dd8c624",
			"relation_locations": [3, 4],
			"relation_sequence": ["named", "for"],
			"sentence_relation": "named for"
		}
	],
	"sentence": "Frobisher Bay is named for the English navigator Sir Martin Frobisher, who, during his search for the Northwest Passage in 1576, became the first European to visit it.",
	"sentence_sequence": ["Frobisher", "Bay", "is", "named", "for", "the", "English", "navigator", "Sir", "Martin", "Frobisher", ",", "who", ",", "during", "his", "search", "for", "the", "Northwest", "Passage", "in", "1576", ",", "became", "the", "first", "European", "to", "visit", "it", "."]
}
"""


def find_verb_index(pos, locations):
  if len(locations) == 1:
    return locations
  res = []
  for i in range(locations[0], locations[-1]):
    if pos[i] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
      res.append(i)

  return res


def create_list(label, positions, n):
  res = ["*"] * n
  if len(positions) == 1:
    res[positions[0]] = "(" + label + "*)"
  else:
    k = len(positions) - 1
    for i, loc in enumerate(positions):
      if i == 0:
        tag = "(" + label + "*"
      elif i == k:
        tag = "*)"
      else:
        tag = "*"

      res[loc] = tag

  return res


LIMIT = 5000


def wiki_to_conll(in_path, out_path, task_id, lang_id):
  words = set()

  nlp = spacy.load(lang_id.lower())

  with open(in_path, "rt", encoding="utf8") as inf, open(out_path, "wt", encoding="utf8", newline="") as outf:
    # with open(out_path, "wt", encoding="utf8", newline="") as outf:
    file = os.path.basename(in_path)
    outf.write("#begin document ({});\r\n".format(file))
    writer = csv.writer(outf, delimiter=" ", quoting=csv.QUOTE_NONE, quotechar='')
    skipped = 0
    line_number = 0
    for line in inf:
      line_number += 1
      if (line_number % 100) == 0:
        logging.info("Processed {} lines".format(line_number))
      if LIMIT and line_number - skipped == LIMIT + 1:
        outf.write("\r\n#end document\r\n")
        break

      outf.write("\r\n")

      obj = json.loads(line)

      tokens = obj['sentence_sequence']
      pos = obj['pos']
      relation_position = obj["relations"][0]["relation_locations"]
      answer_locations = obj["relations"][0]["answer_locations"]
      verb_position = find_verb_index(pos, relation_position)
      if len(verb_position) != 1:
        skipped += 1
        continue
      entity_locations = obj['entity_locations']

      n = len(tokens)
      predicate = create_list("V", verb_position, n)
      arg_0 = create_list("ARG0", entity_locations, n)
      arg_1 = create_list("ARG1", answer_locations, n)
      verb = ["-"] * n
      predicate_word = tokens[verb_position[0]]
      doc = nlp(predicate_word)
      predicate_lemma = doc[0].lemma_
      verb[verb_position[0]] = predicate_lemma

      features = []
      filename = [file] * n
      zeros = ["0"] * n
      i = list(range(0, n))
      try:
        for p, a0, a1 in zip(predicate, arg_0, arg_1):
          if p == a0 == a1 == "*":
            features.append("*")
          elif p != "*" and a0 == a1 == "*":
            features.append(p)
          elif a0 != "*" and p == a1 == "*":
            features.append(a0)
          elif a1 != "*" and p == a0 == "*":
            features.append(a1)
          else:
            raise ValueError
      except ValueError:
        skipped += 1
        continue

      writer.writerow(["#task_id:", "<{}>".format(task_id)])
      writer.writerow(["#lang_id:", "<{}>".format(lang_id)])
      dummy = ["-"] * n
      for k in zip(filename, zeros, i, tokens, pos, dummy, verb, dummy, dummy, dummy, ["*"] * n, features, dummy):
        writer.writerow(k)

    outf.write("\r\n#end document\r\n") if line_number - skipped != LIMIT + 1 else None
  logging.info("Skipped: {} lines".format(skipped))
  logging.info("Words: {}".format(len(words)))


if __name__ == '__main__':
  logging.basicConfig(format='%(asctime)s - %(module)s - %(levelname)s - %(message)s', level=logging.INFO)
  logging.info("Running %s", " ".join(sys.argv))
  # in_path = sys.argv[1]
  # out_path = sys.argv[2]
  # task_id = sys.argv[3]
  # lang_id = sys.argv[4]
  # wiki_to_conll(in_path, out_path, task_id, lang_id)
  logging.info("Completed %s", " ".join(sys.argv))

LANG = "ES"
wiki_to_conll("{}_srl.json".format(LANG.lower()), "wiki_srl_{}.gold_conll".format(LANG.lower()), "WikiSRL", LANG)
