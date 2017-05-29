# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:44:15 2017

@author: ashishbansal
 a fully functional, Watson-powered application that does the following:

Queries the Twitter API
Queries the Watson Personality Insights API
Compares two bodies of text (tweets) from two Twitter users
Displays the top 5 personality traits shared between the two Twitter users

"""
#import needed packages
import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights
def analyze(handle):

	twitter_consumer_key = '0UAUzgrJqnbEHX8e6D6oeqAbT'  
	twitter_consumer_secret = 'h2fczsDeMWgpXovgpZwsJ7zLtOknd3QRuDGrXWucpEVAmEKHwv'  
	twitter_access_token = '839931355991535621-KiPSBgOFHHXVXj9XhYrGF1StFwR9usJ'  
	twitter_access_secret = 'PiEbJp9qhpUblGU2MdphEdNE7TszzgxsASIj8xIWUiiCV'
	twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, 
                                       include_rts=False)
	text = ""
  	for status in statuses:
    		if (status.lang =='en'): #English tweets
      			text += status.text.encode('utf-8')
#The IBM Bluemix credentials for Personality Insights!
	pi_username = 'f40696b2-8ea9-418f-984a-e09b353aa8dd'
	pi_password = 'OQQFUyhK0rJH'
	personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
	pi_result = personality_insights.profile(text)
	return pi_result
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                          data[c3['id']] = c3['percentage']
	return data
def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
                compared_data[keys]=abs(dict1[keys] - dict2[keys])
	return compared_data
user_handle = "@narendramodi"
celebrity_handle = "@AnupamPkher"
user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)
#First, flatten the results from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)
#Then, compare the results of the Watson PI API by calculating the distance between traits
compared_results = compare(user,celebrity)
sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

for keys, value in sorted_result[:5]:
    print keys,
    print(user[keys]),
    print ('->'),
    print (celebrity[keys]),
    print ('->'),
    print (compared_results[keys])

                                                
                                                