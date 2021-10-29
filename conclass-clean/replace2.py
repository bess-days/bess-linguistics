from definitions import alveolar, syllabic, swede_syllabic, bilabial, vowels, velar, rcolored, palatal, doublecon, \
    glottal
with open("word.txt", "r+") as f:
    word = f.read()

word = word.replace('A', 'ei', 1)
word = word.replace('I', 'i:', 1)
word = word.replace('E', 'i:', 1)
word = word.replace('U', 'u:', 1)
word = word.replace('O', 'a:', 1)
word = word.replace('W', 'eu', 1)
word = word.replace('0', 'eu', 1)

with open("word.txt", "w") as f:
    f.write(word)
import change2