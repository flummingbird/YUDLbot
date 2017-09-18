#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config, wget, os

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

statuses = api.user_timeline(user_id='LDLbot')

last_tweets = []

for status in statuses:
  last_tweets.append(status.id)

tweets = api.statuses_lookup(last_tweets)
for tweet in tweets:
  dict = tweet.entities
  if dict['urls']:
    urls = dict['urls'][0]
    print(urls['expanded_url'])
    pid = urls['expanded_url']
    pid = pid[57:len(pid)]
    print(pid)
  print(tweet.text)
  print( "\n")



response = urllib.request.urlopen(config.SOLR_DATA);
data = response.read()
decoded = data.decode('utf-8')
d_json = json.loads(decoded)
docs = d_json["response"]["docs"]
items = random.sample(docs,1)

description = ''

#print(items)

for item in items:
  pid = item["PID"]


