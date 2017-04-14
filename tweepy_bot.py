#!/usr/bin/python3
import tweepy
from misc_tokens import ck, cs, atok, atoks
"""
Main Module for twitter bot, includes authentication
function and default behavior
"""

"""
class twitter_bot():
    Main class with the following functions:
    authenticate
    get_followers
    get_following
    unfollow
    follow
"""
def authenticate():
    """
    Basic authentication that returns the api object
    """

    SECRET_KEY=ck
    SECRET_SECRET=cs
    SECRET_ACCESS=atok
    SECRET_ACCESS_SECRET=atoks

    auth = tweepy.OAuthHandler(SECRET_KEY, SECRET_SECRET)
    auth.set_access_token(SECRET_ACCESS, SECRET_ACCESS_SECRET)
    api = tweepy.API(auth)
    return (api)



if __name__ == "__main__":
    """
    Default behavior
    """
    from random_sentences import random_sentence
    api = authenticate()
    api.update_status(random_sentence())
