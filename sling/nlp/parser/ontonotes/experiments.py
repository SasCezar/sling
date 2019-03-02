EXPERIMENTS = {
  "es_conll_full": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", -1)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_conll_full": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", -1), ("wiki_srl_es.gold_conll", 14300)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_conll_100": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_conll_500": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_conll_1000": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_conll_2000": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_conll_5000": {
    "train": [("CoNLL2009-ST-Spanish-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_5000_conll_0": {
    "train": [("wiki_srl_es.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_5000_conll_100": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_5000_conll_500": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_5000_conll_1000": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "es_wiki_5000_conll_2000": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-es_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-es_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-es_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-es_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-es_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de-es_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de-es_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de-es_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de-es_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de-es_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-de-es_wiki_5000_conll_5000-5000-0": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-de-es_wiki_5000_conll_5000-5000-100": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-de-es_wiki_5000_conll_5000-5000-500": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-de-es_wiki_5000_conll_5000-5000-1000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "en-de-es_wiki_5000_conll_5000-5000-2000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-Spanish-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-Spanish.gold_conll"]
  },

  "de_conll_full": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", -1)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_conll_full": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", -1), ("wiki_srl_de.gold_conll", -1)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_conll_100": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_conll_500": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_conll_1000": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_conll_2000": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_conll_5000": {
    "train": [("CoNLL2009-ST-German-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_5000_conll_0": {
    "train": [("wiki_srl_de.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_5000_conll_100": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_5000_conll_500": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_5000_conll_1000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "de_wiki_5000_conll_2000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-de_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-de_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-de_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-de_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-de_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-German-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-es-de_wiki_5000_conll_5000-5000-0": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-es-de_wiki_5000_conll_5000-5000-100": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-es-de_wiki_5000_conll_5000-5000-500": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-es-de_wiki_5000_conll_5000-5000-1000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en-es-de_wiki_5000_conll_5000-5000-2000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "en_conll_full": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", -1)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_full_v2": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", -1)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_conll_full": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", -1), ("wiki_srl_en.gold_conll", 39000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_conll_full_v2": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", -1), ("wiki_srl_en.gold_conll", 39000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_100": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_100_v2": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_500": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_500_v2": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_1000": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_2000": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_conll_5000": {
    "train": [("CoNLL2009-ST-English-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_5000_conll_0": {
    "train": [("wiki_srl_de.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_5000_conll_100": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_5000_conll_500": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_5000_conll_1000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "en_wiki_5000_conll_2000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-en_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-en_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-en_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-en_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-en_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-Spanish-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-0": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-100": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-500": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-1000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-2000": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "de-en_wiki_5000_conll_5000-2000_v2": {
    "train": [("wiki_srl_en.gold_conll", 5000), ("wiki_srl_de.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-de-en_wiki_5000_conll_5000-5000-0": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-de-en_wiki_5000_conll_5000-5000-100": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 100)],
    "dev": ["CoNLL2009-ST-English-development.gold_conll"],
    "test": ["CoNLL2009-ST-English-evaluation.gold_conll"]
  },

  "es-de-en_wiki_5000_conll_5000-5000-500": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 500)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de-en_wiki_5000_conll_5000-5000-1000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 1000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  },

  "es-de-en_wiki_5000_conll_5000-5000-2000": {
    "train": [("wiki_srl_de.gold_conll", 5000), ("wiki_srl_en.gold_conll", 5000), ("wiki_srl_es.gold_conll", 5000),
              ("CoNLL2009-ST-German-train.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 5000),
              ("CoNLL2009-ST-English-train.gold_conll", 2000)],
    "dev": ["CoNLL2009-ST-German-development.gold_conll"],
    "test": ["CoNLL2009-ST-evaluation-German.gold_conll"]
  }
}
