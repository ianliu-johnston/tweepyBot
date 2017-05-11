#!/usr/bin/python3
"""
Module to get a list of followers and compare it to my list of following
"""
import tweepy
from tweepy_bot import authenticate


def get_lists(which="followers"):
    returns a list of followers or following
    import json
    api = authenticate()
    names = []
    black_list = []
    white_list = []

    if which == "followers":
        cursor = tweepy.Cursor(api.followers).items()
        with open('black_list', 'r') as bl:
            for line in bl:
                black_list.append(line.strip())
    elif which == "following":
        cursor = tweepy.Cursor(api.friends).items()
        with open('white_list', 'r') as bl:
            for line in bl:
                white_list.append(line.strip())

    for user in cursor:
        if user.following == False and user.screen_name not in black_list:
            api.create_friendship(user.screen_name)
    for user in cursor:
    return(names)

"""
###################
    #Write cursor object to file
    for user in cursor:
        with open("friend_cursor_dump", 'a') as f:
            f.write(json.dumps(user._json))

    #Read cursor object from file
    with open("cursor_dump") as f:
        for user in json.loads(f):
            names.append(user.screen_name)
    print(names)
###################
    """


if __name__ == "__main__":
    followers = get_lists("followers")
    print(followers)
#    following = get_lists("following")
#    print("#############################")
#    print(followers)
