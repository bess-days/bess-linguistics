from definitions import vvreplace, vreplace, vreplace3

with open("word.txt", "a+") as f:
    word = f.readline().rstrip()
    print(word)

if len(word) >= 4:
    vreplace(word)
    vvreplace(word)

print(word)