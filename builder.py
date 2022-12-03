import random
import time

audible = ["a","e","i","o","u"]
quiet = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","y","z","q","w"]

def generateWords(number):
    loop = 1
    while loop<=number:
        word = audible[random.randrange(0,len(audible))] + quiet[random.randrange(0,len(quiet))] + quiet[random.randrange(0,len(quiet))] + audible[random.randrange(0,len(audible))]
        print(loop,". word->",word)
        loop += 1
        time.sleep(1)

generateWords(10)
