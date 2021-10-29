from definitions import read, replace1, write, theline


word = str(theline("word.txt", 2))
print(word)
for w in word:
    word = word.replace('sh', 'ʃ', 1)
    word = word.replace('th', 'θ', 1)
    word = word.replace('j', 'ʤ', 1)
    word = word.replace('ch', 'ʧ', 1)
write(word)
import vowel1



