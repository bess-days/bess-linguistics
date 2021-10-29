from definitions import alveolar, syllabic, swede_syllabic, bilabial, vowels, velar, rcolored, palatal, doublecon, glottal, labiodental

with open("word.txt", "r+") as f:
    word = f.read()

for w in word:
    if word.endswith(tuple(alveolar)):
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
with open("word.txt", "w") as f:
    f.write(word)
import replace3
