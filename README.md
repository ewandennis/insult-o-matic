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

## Licensing

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/ewandennis/insult-o-matic">Insult-o-matic</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/ewandennis/">Ewan Dennis</a> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

Credit to:
 - Pittsburgh University for the Subjectivity Lexicon
 - Wordset Inc. for the Wordset dictionary
