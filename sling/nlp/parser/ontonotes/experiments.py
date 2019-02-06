EXPERIMENTS = {
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

  "es_wiki_5000_conll_0": {
    "train": [("wiki_srl_es.gold_conll", 5000), ("CoNLL2009-ST-Spanish-train.gold_conll", 0)],
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
              ("CoNLL2009-ST-English-train.gold_conll", 5000),  ("CoNLL2009-ST-Spanish-train.gold_conll", 100)],
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

}
