import json
import random
import insultIngredients

DEBUG = False

def insultme():
    def pickWord(library):
        return library[random.randrange(len(library))]

    adj = pickWord(insultIngredients.badAdjectives)
    noun = pickWord(insultIngredients.badSingularNouns)
    insult = 'You are a ' + adj['word'] + ' ' + noun['word']
    if DEBUG:
        print(json.dumps(adj, indent=2))
        print(json.dumps(noun, indent=2))

    return insult

if __name__ == '__main__':
    print(insultme())
