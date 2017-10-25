#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config, solr_config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)




response = urllib.request.urlopen(solr_config.SOLR_DATA);
data = response.read()
decoded = data.decode('utf-8')
d_json = json.loads(decoded)
docs = d_json["response"]["docs"]
items = random.sample(docs,1)


for item in items:
  pid = item["PID"]
  print(pid + '\n')
  url = "http://louisianadigitallibrary.org/islandora/object/"
  url += pid
  if(urllib.request.urlopen(url).getcode() == 200):
    print('tweeted')
    api.update_status(status=url)
  else:
    print('failed')
