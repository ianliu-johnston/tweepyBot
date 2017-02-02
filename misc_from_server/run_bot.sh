#!/bin/bash
cd /home/concati/tweepyBot
/usr/bin/python3 /home/concati/tweepyBot/tweepy_bot.py >> /home/concati/tweepyBot/log 2>&1 && date >> /home/concati/tweepyBot/log
