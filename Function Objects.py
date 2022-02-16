import random
from math import factorial
from itertools import permutations, islice
def MakeCharsAlphabetical(text):
    return "".join(sorted(text))
def MakeWordsAlphabetical(text):
    return " ".join(sorted(text.split(" ")))
def MakeRunOn(text):
    for char in ",.:;":
        if char in text:
            text = text.replace(char," and")
    for char in "/":
        if char in text:
            text = text.replace(char, " and ")
    return text.lower()
def MoreAgressive(text):
    length = len(text.split())
    newtext = ""
    for i, word in enumerate(text.split()):
        if random.randint(0,length) <= i:
            word = word.upper()
        else:
            pass
        newtext += " " + word
    return newtext
def TurningRobot(text):
    length = len(text.split())
    newtext = ""
    for i, word in enumerate(text.split()):
        if random.randint(0,length) <= i:
            word = "".join(random.choice(("0","1")) for char in word)
        else:
            pass
        newtext += " " + word
    return newtext
def abbr(text):
    return "".join(word[0].upper() for word in text.split())
#Above functions apply only to the entire text, below functions apply to pieces of it
def mmm(text):
    newtext = ""
    for char in text:
        if char.lower() in {"m", "h"}:
            newtext += char
        else:
            newtext += " "
    return newtext
def AAAAA(text):
    return "".join("A" for char in text)
def MakeSarcastic(text):
    return "".join(random.choice((char.upper(), char.lower())) for char in text)
while True:
    data = input("")
    print (MakeSarcastic(data))

