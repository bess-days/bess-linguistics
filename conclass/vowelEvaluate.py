from definitions import vvreplace, vreplace3, writeWord1, writeWord2

with open("word.txt", "a+") as f:
    word = f.readline().rstrip()
    print(word)

if len(word) <= 3:
        import vowe
else:
    pass

writeWord2(word)
import vowelEvaluate1