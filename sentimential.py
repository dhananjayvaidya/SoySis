import re 
import tweepy 
import sys
from tweepy import OAuthHandler 
from textblob import TextBlob 
import csv
from datetime import datetime
class TwitterClient(object): 
	''' 
	Generic Twitter Class for sentiment analysis. 
	'''
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'K3jlCTAwQdhQ1j2gm7iYCN7dy'
		consumer_secret = 'qqZkS2oYqVmojs7OGD8VJsTrRtyv39OpgFNZNVpKsETxesQsXu'
		access_token = '1044251886390575104-J8adkCw7NnmD1lAZiAUJ9jF0bblJid'
		access_token_secret = 'RvtkyctEbg02sY3kj7Fkx5Xez2lBwlhQGtMPNpG7i7stu'

		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		''' 
		Utility function to clean tweet text by removing links, special characters 
		using simple regex statements. 
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): 
		''' 
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		'''
		# create TextBlob object of passed tweet text 
		analysis = TextBlob(self.clean_tweet(tweet)) 
		# set sentiment 
		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10, geo = "37.090240,-95.712891,100mi"): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count,geocode = geo) 

			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text 
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 

def main(): 
	# creating object of TwitterClient Class 
	api = TwitterClient() 
	# calling function to get tweets 
	print(sys.argv[1])
	if sys.argv[1]:
		q = sys.argv[1]
	
	if sys.argv[2]:
		c = sys.argv[2]

	if sys.argv[3]:
		lat = sys.argv[3]
	if sys.argv[4]:
		log = sys.argv[4]
	if sys.argv[5]:
		Jump = sys.argv[5]
	#lat = 32.776665
	#log = -96.796989
	mit = 10
	
	for x in range(1,10):
		mit = x*int(Jump)
		Geo = str(lat)+","+str(log)+","+str(mit)+"mi"
		print(Geo)
		tweets = api.get_tweets(query = q, count = c ,geo = Geo) 
		print("================ "+str(mit)+"Meters ================")
		
		# picking positive tweets from tweets 
		ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
		positiveCount = format(100*len(ptweets)/len(tweets))
		# percentage of positive tweets 
		print("Positive tweets percentage: {} %"+positiveCount) 

		# picking negative tweets from tweets 
		ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
		negativeCount = format(100*len(ntweets)/len(tweets))
		# percentage of negative tweets
		print("Negative tweets percentage: {} %"+negativeCount) 

		# picking neutral tweets from tweets
		netweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
		neutralCount = format(100*len(netweets)/len(tweets))
		# percentage of neutral tweets 
		print("Neutral tweets percentage: {} %"+neutralCount)
        
		#setup row
		print(type(positiveCount))
		row = [str(x),str(round(float(positiveCount),2)),negativeCount,neutralCount]
		with open(str(q)+"-"+str(datetime.date(datetime.now()))+".csv", 'a') as writeFile:
			writer = csv.writer(writeFile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			writer.writerow(row)
		writeFile.close()

	# printing first 5 positive tweets 
	#print("\n\nPositive tweets:") 
	#for tweet in ptweets[:10]: 
		#print(tweet['text']) 
	# printing first 5 negative tweets 
	#print("\n\nNegative tweets:") 
	#for tweet in ntweets[:10]: 
		#print(tweet['text']) 

if __name__ == "__main__": 
	# calling main function 
	main() 
