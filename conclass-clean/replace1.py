import binascii
import encodings
import codecs
with open("word.txt", "r") as f:
    word = f.read()

print(word)
word = word.replace('sh', 'ʃ', 1)
word = word.replace('th', 'θ', 1)
word = word.replace('j', 'ʤ', 1)
word = word.replace('ch', 'ʧ', 1)
print(word)

with open("word.txt", "w") as f:
    f.write(word)
import change1



