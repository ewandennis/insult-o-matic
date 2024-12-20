import json
import random
import insultIngredients

DEBUG = False
MAX_WORD_LEN=8

def insultme(badAdjectives, badSingularNouns, lightMode=True):
    def pickWord(library):
        return library[random.randrange(len(library))]

    def wordFromObj(w):
        return w if lightMode else w['word']

    adj = pickWord(badAdjectives)
    noun = pickWord(badSingularNouns)
    article = 'an' if wordFromObj(adj)[0] in 'aeiou' else 'a'
    insult = 'You are ' + article + ' ' + wordFromObj(adj) + ' ' + wordFromObj(noun)
    if DEBUG:
        print('adjectives: {}'.format(len(badAdjectives)))
        print('nouns: {}'.format(len(badSingularNouns)))
        print(json.dumps(adj, indent=2))
        print(json.dumps(noun, indent=2))

    return insult

if __name__ == '__main__':
    badAdjectives, badSingularNouns = insultIngredients.loadIngredients(lightMode=True, maxWordLen=MAX_WORD_LEN)
    print(insultme(badAdjectives, badSingularNouns))
