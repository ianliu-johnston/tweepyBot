#!/usr/bin/python3
import random
from datetime import date
from json import loads
from misc_tokens import the_word
from urllib.request import urlopen

def random_picker(random_or_not):
    options = "two_dolla_words", "websites.txt"
    if random_or_not is True:
        random_choice = random.choice(range(len(options)))
    elif random_or_not is -1:
        random_choice = 1
    else:
        random_choice = 0
    try:
        with open(options[random_choice], 'r') as fr:
            lst = list(line for line in fr.read().split('\n'))
            if len(lst) > 1:
                choice = random.choice(range(len(lst)))
                chosen = lst[choice]
                print ("Random Choice: ", chosen)
                del lst[choice]
                with open(options[random_choice], 'w') as fw:
                    for i in lst:
                        if len(i) > 1:
                            fw.write(i)
                            fw.write("\n")
                fw.closed
            else:
                print("File: {} is completely empty.".format(options[random_choice]))
                return(None)
        fr.closed
        return(chosen)
    except FileNotFoundError as no_files:
        print(no_files)
        return(None)


def get_json_parsed(word):
    url = "http://api.wordnik.com:80/v4/word.json/" + word + "/definitions?limit=1&includeRelated=true&useCanonical=false&includeTags=false&api_key=" + the_word
    # url2 = "http://api.wordnik.com:80/v4/words.json/wordOfTheDay?api_key=" + the_word
    try:
        with urlopen(url) as response:
            data = response.read().decode("utf-8")
            parsed = loads(data)
        return(parsed)
    except Exception as err:
        print(err)
        return(-1)

def random_sentence():
    print("-----------", date.today(), "------------")
    buf = ""
    word_or_web = random_picker(True)
    if word_or_web is None or len(word_or_web) < 1:
        buf = "Oops, no more tweets... #cisfun"
    elif ' ' not in word_or_web:
        buf = "Word Of The Day!\n"
        returned = get_json_parsed(word_or_web)
        if returned != -1:
            buf += "{}: ".format(returned[0]['word'])
            buf += "{} -- ".format(returned[0]['partOfSpeech'])
            buf += "{}".format(returned[0]['text'])
        else:
            buf = random_picker(-1)
    else:
        buf += (word_or_web)
    print(buf)
    return(buf[:140])

random_sentence()
