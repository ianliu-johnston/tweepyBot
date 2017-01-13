#!/bin/bash
apt-get update
apt-get install python3-pip
pip3 install --upgrade pip
pip3 install tweepy
echo "Create the bot script in python, using the tweepy module."
chmod u+x tweepy_bot.py
crontab -e
echo "Enter this at the end of the comments section: 23 20 * * * /home/<user>/tweepy_bot.py
