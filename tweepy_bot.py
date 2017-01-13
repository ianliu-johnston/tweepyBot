#!/usr/bin/python3
import tweepy
from random_sentences import random_sentence
from tweepy_secrets import consumer_key, consumer_secret, access_token, access_token_secret

SECRET_KEY=consumer_key
SECRET_SECRET=consumer_secret
SECRET_ACCESS=access_token
SECRET_ACCESS_SECRET=access_token_secret

auth = tweepy.OAuthHandler(SECRET_KEY, SECRET_SECRET)
auth.set_access_token(SECRET_ACCESS, SECRET_ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status(random_sentence())
