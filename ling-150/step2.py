alveolar = ['d', 'l', 'n', 't', 's']
doublecon = ['ll', 'zz', 'ff', 'dd']
velar = ['k', 'c', 'g', 'x']
vowels = ['a', 'e', 'i', 'o', 'u']
syllabic = ['n=', 'm=', 'l=']
swede_syllabic = ['n>', 'l>']

word = str(input('Word: '))

for w in word:
    if word.endswith(tuple(doublecon)):
        word = word + 'an'
        if word[1] in list(vowels):
            word = word[:2] + ':' + word[2:]
            break
        else:
            break
    elif word.endswith(tuple(vowels)) and len(word) > 3 and word.endswith('o' or 'a' or 'e'):
        word = word + syllabic[0]
    elif len(word) >= 3 and word.endswith(tuple(vowels)) and word[1] in list(vowels):
        word = word[:2] + ':' + syllabic[1]
    elif len(word) >= 3 and word[1] in list(vowels) and not word.endswith(tuple(vowels)):
        word[:2] + ':' + swede_syllabic[0]
    elif word[1] in list(vowels) and len(word) > 3 and not word.endswith(tuple(vowels)):
        word = word[:2] + ':' + syllabic[2]
    elif word.endswith(tuple(alveolar)) and len(word) > 3:
        word = word + syllabic[2]
    elif len(word) == 3 and word.endswith(tuple(alveolar)) and not word.endswith(tuple(doublecon)):
        word.replace(word[1], 'ai', 1)
    elif word.endswith(tuple(velar)) and len(word) > 3 and not word.endswith('k'):
        word = word + syllabic[0]
    elif word.endswith(tuple(velar)) and len(word) > 3 and word.endswith('k'):
        word = word + syllabic[1]

word = word.replace('tS', 'ʧ')
word = word.replace('ʤ', 'dZ')
word = word.replace('th', 'θ')
word = word.replace('sh','ʃ',)
word = word.replace('n=', ' ̩̩n')
word = word.replace('l=', ' ̩̩l')
word = word.replace('m=', ' ̩̩m')
word = word.replace('ll', 'l')
word = word.replace('ck', 'k')
word = word.replace('n>', 'ɳ')
word = word.replace('l>', 'ɭ')

print('[' + word + ']')
