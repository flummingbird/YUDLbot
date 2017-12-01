#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, json, urllib, random, config, solr_config, re

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

nola_trends = api.trends_place(2458833)

searches = []

for trends_data in nola_trends:
    trends = trends_data['trends']
    for trend in trends:
        if '#' in trend['name']:
            trend['name'] = re.sub('#','',trend['name'])
        searches.append(trend['name'])

print(searches)

#for item in items:
#  pid = item["PID"]
#  print(pid + '\n')
#  url = "http://louisianadigitallibrary.org/islandora/object/"
#  url += pid
#  if(urllib.request.urlopen(url).getcode() == 200):
#    print('tweeted')
#    api.update_status(status=url)
#  else:
#    print('failed')
