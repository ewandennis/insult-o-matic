import json

WORDSET_DICT_DATA = 'vendor/wordset-dictionary/data/'
cache = {}

def _cacheLetter(letter):
    cache[letter] = json.load(open(WORDSET_DICT_DATA + letter + '.json'))

def lookup(word):
    firstLetter = word[0]
    if firstLetter not in cache:
        _cacheLetter(firstLetter)
    if word in cache[firstLetter]:
        return cache[firstLetter][word]
    return None

