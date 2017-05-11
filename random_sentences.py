#!/usr/bin/python3
import random
from datetime import date
from json import loads
from misc_tokens import the_word
from urllib.request import urlopen
from word_soup import wordsoup

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
            else:
                print("File: {} is completely empty.".format(options[random_choice]))
                return(None)
        fr.close()
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
        buf = "ianbot: Oops, no more tweets. I better make something up: "
        buf += wordsoup()
        buf += "#ai"
    elif ' ' not in word_or_web:
        buf = "Word Of The Day!\n"
        returned = get_json_parsed(word_or_web)
        word_of_the_day = returned[0].get('word')
        part_of_speech = returned[0].get('partOfSpeech')
        if returned != -1:
            buf += "{}: ".format(word_of_the_day)
            buf += "{} -- ".format(part_of_speech)
            buf += "{}".format(returned[0]['text'])
            if part_of_speech == 'adjective':
                with open('data/Adjectives.txt', 'a') as word:
                    word.write('\n' + word_of_the_day.strip())
            elif part_of_speech[0:4] == 'verb':
                with open('data/Past_Verbs.txt', 'a') as word:
                    write_this = word_of_the_day.strip()
                    if write_this[len(write_this)-1] == "e":
                        write_this += 'd'
                    else:
                        write_this += 'ed'
                    word.write('\n' + write_this)
            elif part_of_speech[0:4] == 'noun':
                with open('data/Nouns.txt', 'a') as word:
                    word.write('\n' + word_of_the_day.strip())
        else:
            buf = random_picker(-1)
    else:
        buf += (word_or_web)
    print(buf)
    return(buf[:140])

if __name__ == "__main__":
    print(random_sentence())
