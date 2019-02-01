EXPERIMENTS = {
  "name": {
    "train": [("", 5000), ("", 500)],
    "dev": [""],
    "test": [""]
  },
  "es_wiki_5000_conll_500": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },
}
