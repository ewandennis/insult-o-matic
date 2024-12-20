import os
import json

LEXICON = 'vendor/subjLexicon.json'
CACHE = 'insultIngredients.cache'
VERY_BAD_NOUNS = ['bastard']

# include in the cache the lexicon and dictionary records used to build the ingredients
DEBUG = False

def posTag(words, wordSetPos, subjPos):
    import wordset
    for word in words:
        dictResult = wordset.lookup(word['word'])
        if dictResult:
            isPos = any([meaning['speech_part'] == wordSetPos for meaning in dictResult['meanings']])
            if isPos:
                word['partOfSpeech2'] = subjPos
            elif not 'partOfSpeech2' in word:
                word['partOfSpeech2'] = None
        word['_wordSet'] = dictResult

def lightenUp(words):
    return [word['word'] for word in words]

def exclude(comparator, lst):
    return list(filter(comparator, lst))

def _buildInsultIngredients(lightMode, maxWordLen):
    lexicon = json.load(open(LEXICON))

    posTag(lexicon, 'adjective', 'adj')
    posTag(lexicon, 'noun', 'noun')

    if maxWordLen is not None:
        shortWords = exclude(lambda word: len(word['word']) <= maxWordLen, lexicon)

    realWords = exclude(lambda word: word['_wordSet'] is not None, shortWords)
    badWords = exclude(lambda word: word['sentiment'] == 'negative', realWords)
    badAdjectives = exclude(lambda word: word['partOfSpeech'] == 'adj' and word['partOfSpeech2'] == 'adj', badWords)
    badNouns = exclude(lambda word: word['partOfSpeech'] == 'noun' and word['partOfSpeech2'] == 'noun', badWords)
    badSingularNouns = exclude(lambda word: word['word'][-2:] != 'es', badNouns)

    badSingularNouns = exclude(lambda word: word['word'].lower() not in VERY_BAD_NOUNS, badSingularNouns)

    if lightMode:
        badAdjectives = lightenUp(badAdjectives)
        badSingularNouns = lightenUp(badSingularNouns)

    return badAdjectives, badSingularNouns

def loadIngredients(lightMode=True, forceRebuild=False, maxWordLen=None):
    if forceRebuild:
        os.remove(CACHE)

    try:
        cache = json.load(open(CACHE))
        badAdjectives = cache['badAdjectives']
        badSingularNouns = cache['badSingularNouns']
    except Exception as e:
        badAdjectives, badSingularNouns = _buildInsultIngredients(lightMode, maxWordLen)
        kwargs = {} if lightMode else {"indent": 2}
        json.dump(dict(badAdjectives=badAdjectives, badSingularNouns=badSingularNouns), open(CACHE, 'w'), **kwargs)

    return badAdjectives, badSingularNouns

