#!/usr/bin/python3
import random


def wordsoup():
    adjs = verbs = pres_verbs = nouns = pronouns = {}
    with open("data/Nouns.txt") as f:
        for num,line in enumerate(f):
            nouns[num] = line.strip()
    n1 = nouns[random.choice(range(len(nouns)))];
    n2 = nouns[random.choice(range(len(nouns)))];
    n3 = nouns[random.choice(range(len(nouns)))];

    with open("data/Adjectives.txt") as f:
        for num,line in enumerate(f):
            adjs[num] = line.strip()
    adj = adjs[random.choice(range(len(adjs)))];

    with open("data/Past_Verbs.txt") as f:
        for num,line in enumerate(f):
            verbs[num] = line.strip()
    verb = verbs[random.choice(range(len(verbs)))];

    pronouns = { 0:"you", 1:"he", 2:"she", 3:"we", 4:"they", 5:"it", 6:"I", }
    pro = pronouns[random.choice(range(len(pronouns)))];

    possessives = { 0:"the", 1:"his", 2:"her", 3:"their", 4:"our", 5:"my", 6:"your", 7:"its"}
    pos = possessives[random.choice(range(len(possessives)))];

    return(pos[0].upper() + pos[1:] + " " + adj + " " + n1 + " " + verb + " the " + n2 + '.')

if __name__ == "__main__":
    print(wordsoup())
