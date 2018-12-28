#!/usr/bin/python3
from flask_restful import Resource
from flask import Flask, request, jsonify
from json import dumps
from .TwitterClientService import TwitterClient
class Sentiment(Resource):
    def post(self):
        api = TwitterClient()
        query = request.json['query']
        count = request.json['count']
        latitude = request.json['latitude']
        longitude = request.json['longitude']
        radius = request.json['radius']
        until = request.json['until']
        tweets = api.get_tweets(query = query, count = count ,geo = latitude+","+longitude+","+radius,until=until) 
	
        # picking positive tweets from tweets 
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
        # picking negative tweets from tweets 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
        # picking neutral tweets from tweets
        netweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        
        # percentage of positive tweets  
        positivePercentage = format(100*len(ptweets)/len(tweets))
        negativePercentage = format(100*len(ntweets)/len(tweets))
        neutralPercentage  = format(100*len(netweets)/len(tweets))
        
        # printing first 5 positive tweets 
        print("\n\nPositive tweets:") 
        for tweet in ptweets[:10]: 
            print(tweet['text']) 

        # printing first 5 negative tweets 
        print("\n\nNegative tweets:") 
        for tweet in ntweets[:10]: 
            print(tweet['text']) 
        return {"response":{"positive":positivePercentage,"negative":negativePercentage,"neutral":neutralPercentage}},200