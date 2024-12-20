import json
import random

LIGHTMODE = True
DEBUG = False

def loadIngredients():
    if LIGHTMODE:
        ingredients = json.load(open('insultIngredients.cache'))
        return ingredients['badAdjectives'], ingredients['badSingularNouns']
    import insultIngredients
    return insultIngredients.badAdjectives, insultIngredients.badSingularNouns

def insultme():
    def pickWord(library):
        return library[random.randrange(len(library))]

    badAdjectives, badSingularNouns = loadIngredients()
    adj = pickWord(badAdjectives)
    noun = pickWord(badSingularNouns)
    article = 'an' if adj['word'][0] in 'aeiou' else 'a'
    insult = 'You are ' + article + ' ' + adj['word'] + ' ' + noun['word']
    if DEBUG:
        print('adjectives: {}'.format(len(badAdjectives)))
        print('nouns: {}'.format(len(badSingularNouns)))
        print(json.dumps(adj, indent=2))
        print(json.dumps(noun, indent=2))

    return insult

if __name__ == '__main__':
    print(insultme())
