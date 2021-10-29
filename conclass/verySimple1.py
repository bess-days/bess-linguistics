word = input('word: ')
def nextLine(word):
    nl = "\n"
    f = open("word.txt", "a+")
    f.write(word + nl)

f = open("word.txt", "w")
print('Boo')
f.write(word)
f.close()


word = word.replace(word[0], 'bbbb', 1)
nextLine(word)


f2 = open("word.txt", "a")
print('heyyy')
f2.write(word)

fo = open("word.txt", "r")
word = fo.readline(2)
print(word)