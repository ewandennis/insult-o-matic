import json
import random
import insultIngredients

DEBUG = False
LIGHTMODE = True

def wordFromObj(w):
    return w if LIGHTMODE else w['word']

def insultme():
    def pickWord(library):
        return library[random.randrange(len(library))]

    badAdjectives, badSingularNouns = insultIngredients.loadIngredients(LIGHTMODE)
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
    print(insultme())
