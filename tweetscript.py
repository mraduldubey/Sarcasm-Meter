'''Using python-twitter module for streaming all MoS tweets'''
'''
import twitter

api = twitter.Api(consumer_key='the_key',
                      consumer_secret='secret_key',
                      access_token_key='access_token',
                      access_token_secret='secret_access_token')

print(api.VerifyCredentials())
#{"id": 16133, "location": "Philadelphia", "name": "bear"}

#Generate search query from here: https://twitter.com/search-advanced.
results = api.GetSearch(raw_query="=from%3ASarcasmMother") 

print (results)
'''


import tweepy 
import csv

#Twitter API credentials
consumer_key = "F88gLghFSb3SWApKVvDS6ldiD"
consumer_secret = "qP3jIfb8F6qEhvDFhcuOlthOhKitGgZVa34t1Vvr6a10kj8QpS"
access_key = "926774903046471680-xtfADLd95RxqsqxBPczkVXQ8wluR4YV"
access_secret = "is7FfCBp1WFdjdumEn5PE4DTKlsIRJmQY9Bk99gN3PyF7"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('MOStweets.csv', 'w+') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("SarcasmMother")
