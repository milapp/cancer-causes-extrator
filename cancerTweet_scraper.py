import GetOldTweets3 as got
import pandas as pd

topicDict = {}

def TweetsOnTopic(topics, count):
	text_tweets = []
	for topic in topics:
		# making query object
		tweetCriteriaVer = got.manager.TweetCriteria().setQuerySearch(topic+" filter:verified").setMaxTweets(count)
		tweetCriteriaNotVer = got.manager.TweetCriteria().setQuerySearch(topic+" -filter:verified").setMaxTweets(count)
		# Fetching and saving tweets
		print("fetching %d*2 recent tweets for %s\n\tGetting Verified account tweets"%(count,topicDict[topics.index(topic)]))
		tweetsVer = got.manager.TweetManager.getTweets(tweetCriteriaVer)
		
		for tweet in tweetsVer:
			text_tweets.append([topicDict[topics.index(topic)],1,tweet.text])
			print("saved:\t",[topicDict[topics.index(topic)],1,tweet.text])

		print("\tGetting Not verified account tweets")
		tweetsNotVer = got.manager.TweetManager.getTweets(tweetCriteriaNotVer)
		
		for tweet in tweetsNotVer:
			text_tweets.append([topicDict[topics.index(topic)],0,tweet.text])		
			print("saved:\t",[topicDict[topics.index(topic)],0,tweet.text])
		
	print("Exporting to a CSV file")
	# Creation of file from tweets
	tweets_df = pd.DataFrame(text_tweets, columns = ['Topic','verified', 'Text'])
	tweets_df.to_csv('Data/cancer-%2.1fk-tweets.csv'%(len(text_tweets)/1000), sep=',')

topics = ['("causes cancer" OR "is a cause of cancer" OR "results in cancer" OR "is a reason of cancer" OR "caused cancer" OR "will lead to cancer" OR "leads to cancer") -RT -filter:links',\
			'("cures cancer" OR "is a cure of cancer" OR "is cure of cancer" OR "cured cancer") -RT -filter:links',\
			'("prevention of cancer" OR "prevents cancer" OR "avoid cancer" OR "avoids cancer" OR "prevention against cancer") -RT -filter:links']

topicDict[0] = "Causes of cancer"
topicDict[1] = "Cure of cancer"
topicDict[2] = "prevention against cancer"

count = 2200
TweetsOnTopic(topics,count/2)