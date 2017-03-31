#!/usr/bin/python3
import random


def wordsoup():
    adjs = verbs = pres_verbs = nouns = pronouns = {}
    with open("data/Nouns.txt") as f:
        for num,line in enumerate(f):
            nouns[num] = line
    n1 = nouns[random.choice(range(len(nouns)))];
    n2 = nouns[random.choice(range(len(nouns)))];
    n3 = nouns[random.choice(range(len(nouns)))];
    print(nouns)

    with open("data/Adjectives.txt") as f:
        for num,line in enumerate(f):
            adjs[num] = line
    adj = adjs[random.choice(range(len(adjs)))];
    print(adjs)

    with open("data/Past_Verbs.txt") as f:
        for num,line in enumerate(f):
            verbs[num] = line
    verb = verbs[random.choice(range(len(verbs)))];
    print(verbs)

    pronouns = { 0:"you", 1:"he", 2:"she", 3:"we", 4:"they", 5:"it", 6:"I", }
    pro = pronouns[random.choice(range(len(pronouns)))];

    possessives = { 0:"the", 1:"his", 2:"her", 3:"their", 4:"our", 5:"my", 6:"your", 7:"its"}
    pos = possessives[random.choice(range(len(possessives)))];

    return(pos + " " + adj[0:-1] + " " + n1[0:-1] + " " + verb + " the " + n2)

if __name__ == "__main__":
    print(wordsoup())
