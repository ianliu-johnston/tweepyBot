#!/usr/bin/python3
import random
from json import loads
from tweepy_secrets import secret_keyword
from urllib.request import urlopen

def open_files():
    options = "two_dolla_words", "websites.txt"
    random_choice = random.choice(range(len(options)))
    with open(options[random_choice], 'r') as fr:
        lst = list(line for line in fr.read().split('\n'))
        choice = random.choice(range(len(lst)))
        chosen = lst[choice]
        del lst[choice]
    fr.closed
    with open(options[random_choice], 'w') as fw:
        for i in lst:
            fw.write(i)
            fw.write("\n")
    fw.closed
    return(chosen)

def get_json_parsed(word):
    url = "http://api.wordnik.com:80/v4/word.json/" + word + "/definitions?limit=1&includeRelated=true&useCanonical=false&includeTags=false&api_key=" + secret_keyword
    # url2 = "http://api.wordnik.com:80/v4/words.json/wordOfTheDay?api_key=" + secret_keyword
    with urlopen(url) as response:
        data = response.read().decode("utf-8")
        parsed = json.loads(data)
    return(parsed)

def random_sentence():
    buf = ""
    word_or_web = open_files()
    if "http" not in word_or_web:
        buf = "Word Of The Day!\n"
        returned = get_json_parsed(word_or_web)
        buf += "{}: ".format(returned[0]['word'])
        buf += "{} -- ".format(returned[0]['partOfSpeech'])
        buf += "{}".format(returned[0]['text'])
    else:
        buf += (word_or_web)
    return(buf[:140])

