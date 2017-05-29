# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:44:15 2017

@author: ashishbansal
how to obtain Twitter API credentials, interaction with the Twitter API using 
Python, and retrieve information from public Twitter accounts, like tweets.

"""
#import needed packages
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
#CREATE YOUR NEW APP
#FROM THERE EXTRACT CONSUMER KEY ,SECRET KEY (CONSUMER),ACESS_TOKEN,
#ACESS_SECRET_KEY 
twitter_consumer_key = '0UAUzgrJqnbEHX8e6D6oeqAbT'  
twitter_consumer_secret = 'h2fczsDeMWgpXovgpZwsJ7zLtOknd3QRuDGrXWucpEVAmEKHwv'  
twitter_access_token = '839931355991535621-KiPSBgOFHHXVXj9XhYrGF1StFwR9usJ'  
twitter_access_secret = 'PiEbJp9qhpUblGU2MdphEdNE7TszzgxsASIj8xIWUiiCV'
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)
handle = "@narendramodi"#ADD THE REQUIRED HANDLES FOR REQUIRED STATUS

statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, 
                                       include_rts=False)
text = ""
for status in statuses:
    if (status.lang =='en'): #English tweets
        text += status.text.encode('utf-8')
print (text)        
