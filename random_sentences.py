#!/usr/bin/python3
import random
import json
from tweepy_secrets import secret_keyword
from urllib.request import urlopen

def open_files():
    options = "two_dolla_words", "websites.txt"
    with open(random.choice(options), 'r') as f:
        s = list(line for line in f.read().split('\n'))
    f.closed
    return(s)

def get_json_parsed(word):
    url = "http://api.wordnik.com:80/v4/word.json/" + word + "/definitions?limit=1&includeRelated=true&useCanonical=false&includeTags=false&api_key=" + secret_keyword
    # url2 = "http://api.wordnik.com:80/v4/words.json/wordOfTheDay?api_key=" + secret_keyword
    with urlopen(url) as response:
        data = response.read().decode("utf-8")
        parsed = json.loads(data)
    return(parsed)
    return(word)

def random_sentence():
    buf = ""
    word_or_web = open_files()
    if "http" not in word_or_web[0]:
        buf = "Word Of The Day!\n"
        returned = get_json_parsed(random.choice(word_or_web))
        buf += returned
        buf += "{}: ".format(returned[0]['word'])
        buf += "{} -- ".format(returned[0]['partOfSpeech'])
        buf += "{}".format(returned[0]['text'])
    else:
        buf += random.choice(word_or_web)
    return(buf[:140])
