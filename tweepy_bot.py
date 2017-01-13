#!/usr/bin/python3
import tweepy
from random_sentences import random_sentence
from misc_tokens import ck, cs, atok, atoks

SECRET_KEY=ck
SECRET_SECRET=cs
SECRET_ACCESS=atok
SECRET_ACCESS_SECRET=atoks

auth = tweepy.OAuthHandler(SECRET_KEY, SECRET_SECRET)
auth.set_access_token(SECRET_ACCESS, SECRET_ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(random_sentence())
