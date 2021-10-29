from termcolor import colored

import colored
from coloring import *

bilabial = ['p', 'b', 'm']
labiodental = ['f', 'v']
alveolar = ['t', 'n', 'r', 'd', 's', 'ʤ', 'ʃ', 'θ', 'ʧ', 'l']
retroflex = ['n>', 'l>']
velar = ['k', 'g']
palatal = ['c', 'j']
glottal = ['g?']
swede_syllabic = ['n>', 'l>']
syllabic = ['n=', 'm=', 'l=']
rcolored = ['i-', 'a-']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
doublecon = ['ll', 'tt', 'ss']
inventory = bilabial + labiodental + alveolar + retroflex + velar + palatal + glottal + vowels

input('Word: ')

if word.endswith('s'):
    print('The', chartreuse('system'), 'detects your inputed word might be a', violet('plural'))
    print('Is your word plural?')
    print('Type', sienna('Y for yes'), 'or', aquamarine('N for no'))
    plural = str(input('Y/N: '))
    plural.upper()
    if plural == 'Y':
        print('Please re-enter your word to be singular')
        exit()

    else:
        print('Great! In the future, adding plurals will be adding a \"z\" sound no matter enviroment.')

if word.endswith('ly' or 'able' or 'er' or 'ed' or 'ing'):
    print(
        'The system detected suffixes that serve as bound morphemes providing tense or changing a word to an adverb.')
    print('Are you using the simplist syntax to relay your meaning and intention?')
    print('Type', sienna('Y for yes'), 'or', aquamarine('N for no'))
    simple = str(input('Y/N: '))
    simple.upper()
    if simple == 'Y':
        print(
            'Good to know! In this language, since the words being edited are often nouns or adjectives to '
            'describe '
            'a person,')
        print('or thing does not need to be edited with \"ly\" or \"able\" because the words in this language'
              'are exclusively positive, they can\'t be negated')
    else:
        print('Please re-input your word.')
        exit()

if word[-1:] in inventory:
    print('Okay')
else:
    print('Not Okay')

def my_func():
    print('Try it out!')


if __name__ == '__main__':
    my_func()
bilabial = ['p', 'b', 'm']
labiodental = ['f', 'v']
alveolar = ['t', 'n', 'r', 'd', 's', 'ʤ', 'ʃ', 'θ', 'ʧ', 'l']
retroflex = ['n>', 'l>']
velar = ['k', 'g']
palatal = ['c', 'j']
glottal = ['g?']
swede_syllabic = ['n>', 'l>']
syllabic = ['n=', 'm=', 'l=']
rcolored = ['i-', 'a-']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
doublecon = ['ll', 'tt', 'ss']
inventory = bilabial + labiodental + alveolar + retroflex + velar + palatal + glottal + vowels

word = input('Word: ')
for w in word:
    word = word.replace('sh', 'ʃ', 1)
    word = word.replace('th', 'θ', 1)
    word = word.replace('j', 'ʤ', 1)
    word = word.replace('ch', 'ʧ', 1)
    if len(word) == 3:
        if word[1] in vowels and not word[2] in vowels:
            word = word.replace('a', 'æ', 1)
            word = word.replace('o', 'ɔ', 1)
            word = word.replace('u', 'ʌ', 1)
            word = word.replace('i', 'ɪ', 1)
            word = word.replace('e', 'ɜ', 1)
            print(word, 'CVC replacement')
        elif word[1] in vowels and word[2] in vowels:
            word = word.replace('oo', 'U', 1)
            word = word.replace('ee', 'I', 1)
            word = word.replace('ea', 'I', 1)
            word = word.replace('ou', 'W', 1)
            word = word.replace('oi', 'I', 1)
            word = word.replace('ai', 'A', 1)
            word = word.replace('ay', 'A', 1)
            word = word.replace('oy', '0', 1)
    if len(word) >= 4:
        if word[1] in vowels and not word[2] in vowels:
            word = word.replace('a', 'A', 1)
            word = word.replace('o', 'O', 1)
            word = word.replace('u', 'U', 1)
            word = word.replace('i', 'I', 1)
            word = word.replace('e', 'I', 1)
            print(word, 'CVC replacement')
            pass
        elif word[1] in vowels and word[2] in vowels:
            word = word.replace('oo', 'U', 1)
            word = word.replace('ee', 'I', 1)
            word = word.replace('ea', 'I', 1)
            word = word.replace('ou', 'W', 1)
            word = word.replace('oi', 'I', 1)
            word = word.replace('ai', 'A', 1)
            word = word.replace('ay', 'A', 1)
            word = word.replace('oy', 'U', 1)
            pass
        elif word[2] in vowels and not word[3] in vowels:
            word = word.replace('a', 'A', 1)
            word = word.replace('o', 'O', 1)
            word = word.replace('u', 'U', 1)
            word = word.replace('i', 'I', 1)
            word = word.replace('e', 'I', 1)
            print(word, 'CVC replacement')
            pass
        elif word[2] in vowels and word[3] in vowels:
            word = word.replace('oo', 'U', 1)
            word = word.replace('ee', 'I', 1)
            word = word.replace('ea', 'I', 1)
            word = word.replace('ou', 'W', 1)
            word = word.replace('oi', 'I', 1)
            word = word.replace('ai', 'A', 1)
            print(word, 'CVVC replacement')
            pass
        elif word.endswith(tuple(alveolar)):
            word = word[: -1] + syllabic[2]
        elif word.endswith(tuple(bilabial)):
            word = word[: -1] + syllabic[1]
        elif word.endswith(tuple(labiodental)):
            word = word[: -1] + rcolored[0]
        elif word.endswith(tuple(velar)):
            word = word[: -1] + swede_syllabic[0]
        elif word.endswith(tuple(palatal)):
            word = word[: -1] + rcolored[0]
    elif len(word) <= 3:
        # Ends in what provided
        if word.endswith(tuple(alveolar)) and not word.endswith('l'):
            word = word + syllabic[2]
            break
        if word.endswith(tuple(alveolar)) and word.endswith('l'):
            word = word.replace('l', '/', 1)
            break
        if word.endswith(tuple(bilabial)) and not word.endswith('m'):
            word = word + syllabic[1]
            break
        if word.endswith(tuple(bilabial)) and word.endswith('m'):
            word = word + syllabic[2]
            break
        if word.endswith(tuple(labiodental)):
            word = word + rcolored[0]
            break
        if word.endswith(tuple(velar)):
            word = word[:2] + glottal[0] + word[2:]
            break
        if word.endswith(tuple(palatal)):
            word = word[:2] + glottal[0] + word[2:]
            break
        else:
            word = word[:2] + glottal[0] + swede_syllabic[0]
word = word.replace('n=', ' ̩̩n')
word = word.replace('A', 'ei', 1)
word = word.replace('I', 'i:', 1)
word = word.replace('E', 'i:', 1)
word = word.replace('U', 'u:', 1)
word = word.replace('O', 'a:', 1)
word = word.replace('W', 'eu', 1)
word = word.replace('0', 'eu', 1)
word = word.replace('l=', ' ̩̩l')
word = word.replace('m=', ' ̩̩m')
word = word.replace('n>', 'ɳ')
word = word.replace('g?', 'ʔ')
word = word.replace('I', 'i')
word = word.replace('U', 'i')
word = word.replace('/', 'el')
print(word)



for w in vword:
    if vword.endswith(tuple(alveolar)):
        vword = vword[: -1] + syllabic[2]
    elif vword.endswith(tuple(bilabial)):
        vword = vword[: -1] + syllabic[1]
    elif vword.endswith(tuple(labiodental)):
        vword = vword[: -1] + rcolored[0]
    elif vword.endswith(tuple(velar)):
        vword = vword[: -1] + swede_syllabic[0]
    elif vword.endswith(tuple(palatal)):
        vword = vword[: -1] + rcolored[0]
    elif len(vword) <= 3:
        if vword.endswith(tuple(alveolar)) and not vword.endswith('l'):
            vword = vword + syllabic[2]
            break
        if vword.endswith(tuple(alveolar)) and vword.endswith('l'):
            vword = vword.replace('l', '/', 1)
            break
    if vword.endswith(tuple(bilabial)) and not vword.endswith('m'):
        vword = vword + syllabic[1]
        break
    if vword.endswith(tuple(bilabial)) and vword.endswith('m'):
        vword = vword + syllabic[2]
        break
    if vword.endswith(tuple(labiodental)):
        vword = vword + rcolored[0]
        break
    if vword.endswith(tuple(velar)):
        vword = vword[:2] + glottal[0] + vword[2:]
        break
    if vword.endswith(tuple(palatal)):
        vword = vword[:2] + glottal[0] + vword[2:]
        break
    else:
        vword = vword[:2] + glottal[0] + swede_syllabic[0]
vword = vword.replace('n=', ' ̩̩n')
vword = vword.replace('A', 'ei', 1)
vword = vword.replace('I', 'i:', 1)
vword = vword.replace('E', 'i:', 1)
vword = vword.replace('U', 'u:', 1)
vword = vword.replace('O', 'a:', 1)
vword = vword.replace('W', 'eu', 1)
vword = vword.replace('0', 'eu', 1)
vword = vword.replace('l=', ' ̩̩l')
vword = vword.replace('m=', ' ̩̩m')
vword = vword.replace('n>', 'ɳ')
vword = vword.replace('g?', 'ʔ')
vword = vword.replace('I', 'i')
vword = vword.replace('U', 'i')
vword = vword.replace('/', 'el')


print(vword)
