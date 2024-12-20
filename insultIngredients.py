import os.path
import json
import wordset

LEXICON = 'vendor/subjLexicon.json'
CACHE = 'insultIngredients.cache'

# include in the cache the lexicon and dictionary records used to build the ingredients
DEBUG = False

def posTag(words, wordSetPos, subjPos):
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
    return [dict(word=word['word']) for word in words]

def buildInsultIngredients():
    lexicon = json.load(open(LEXICON))

    posTag(lexicon, 'adjective', 'adj')
    posTag(lexicon, 'noun', 'noun')

    realWords = list(filter(lambda word: word['_wordSet'] is not None, lexicon))
    badWords = list(filter(lambda word: word['sentiment'] == 'negative', realWords))
    badAdjectives = list(filter(lambda word: word['partOfSpeech'] == 'adj' and word['partOfSpeech2'] == 'adj', badWords))
    badNouns = list(filter(lambda word: word['partOfSpeech'] == 'noun' and word['partOfSpeech2'] == 'noun', badWords))
    badSingularNouns = list(filter(lambda word: word['word'][-2:] != 'es', badNouns))

    badAdjectives = list(badAdjectives)
    badSingularNouns = list(badSingularNouns)

    if not DEBUG:
        badAdjectives = lightenUp(badAdjectives)
        badSingularNouns = lightenUp(badSingularNouns)

    return badAdjectives, badSingularNouns

if not os.path.isfile(CACHE):
    badAdjectives, badSingularNouns = buildInsultIngredients()
    json.dump(dict(badAdjectives=badAdjectives, badSingularNouns=badSingularNouns), open(CACHE, 'w'))
else:
    cache = json.load(open(CACHE))
    badAdjectives = cache['badAdjectives']
    badSingularNouns = cache['badSingularNouns']
