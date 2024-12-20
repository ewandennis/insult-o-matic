## Deps

 - python - tested with py 3.10.2
 - subjectivity lexicon: http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/
 - wordset dictionary: https://github.com/wordset/wordset-dictionary.git

## Setup

1. download subjectivity lexicon and unzip to vendor/subjectivity_clues_hltemnlp05/
1. clone wordset dictionary: `cd vendor && git clone https://github.com/wordset/wordset-dictionary.git`
1. translate the subjectivity lexicon to json: `python xlateSubjLexicon.py vendor/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff > vendor/subjLexicon.json`

## Usage

`python insultMe.py`

On first run, it build build insult ingredients and cache to insultIngredients.cache. On future runs, it will reuse the cache.

