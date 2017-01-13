#!/usr/bin/python3
import random
import json
from tweepy_secrets import secret_keyword
from urllib.request import urlopen

def get_json_parsed(word):
    url = "http://api.wordnik.com:80/v4/word.json/" + word + "/definitions?limit=1&includeRelated=true&useCanonical=false&includeTags=false&api_key=" + secret_keyword
    response = urlopen(url)
    data = response.read().decode("utf-8")
    parsed = json.loads(data)
    parsed = data
    return(parsed)

def random_sentence():
    buf = "Word Of The Day!\n"
    two_dollar_words=["ephemera", "exhume", "anathema", "obsequious", "exodoi", "ornery", "extirpate", "soporiphic", "cadence", "fusty", "fungible"]
    returned = get_json_parsed(random.choice(two_dollar_words))
    buf += "{}: ".format(returned[0]['word'])
    buf += "{} -- ".format(returned[0]['partOfSpeech'])
    buf += "{}".format(returned[0]['text'])
    return(buf[:140])
