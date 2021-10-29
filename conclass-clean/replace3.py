from definitions import alveolar, syllabic, swede_syllabic, bilabial, vowels, velar, rcolored, palatal, doublecon, \
    glottal
with open("word.txt", "r+") as f:
    word = f.read()

word = word.replace('n=', ' ̩̩n')
word = word.replace('l=', ' ̩̩l')
word = word.replace('m=', ' ̩̩m')
word = word.replace('n>', 'ɳ')
word = word.replace('g?', 'ʔ')
word = word.replace('I', 'i')
word = word.replace('U', 'i')
word = word.replace('/', 'el')
print(word)

with open("word.txt", "w") as f:
    f.write(word)