#IMPORT LIBRARIES:
import tweepy
import csv
import pandas as pd
import sqlite3


#%%
#INPUT FOR THE PROGRAM:
#Section where user must input the relevant information to run this program.
twitterProfile = "PipingGourmets" #Input the Twitter Profile you want to analyze
consumer_key = "RIoocQTyKhFazOz8zMDJDfT3Z" #Input Twitter API credentials
consumer_secret = "8ZwWHnyic1fkzq1c0X1l1GHqHUWx7PSiNCnvDVPMt2SFNuKGfw" #Input Twitter API credentials



#%%
#################################################################################################################################################################################################################
#RETRIEVE TWEETS:
#This block of code was NOT WRITTEN BY US
#We were graciously able to borrow it from https://gist.github.com/yanofsky/5436496
def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	api = tweepy.API(auth)
	alltweets = []	
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		alltweets.extend(new_tweets)
		oldest = alltweets[-1].id - 1
		print "...%s tweets downloaded so far" % (len(alltweets))
	outtweets = [[tweet.id_str, tweet.created_at, tweet.author.name.encode('utf8'), tweet.user.followers_count, tweet.favorite_count, tweet.retweet_count, tweet.text.encode("utf-8")] for tweet in alltweets]	
	with open('%s.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["TweetID","CreatedAt", "Author", "FollowerCount", "FavoriteCount", "RetweetCount", "TweetText"])
		writer.writerows(outtweets)
	pass

#Runs the function with Twitter handle inputted above
get_all_tweets(twitterProfile)


#################################################################################################################################################################################################################



#%%
#DATA PREPARATION:
#In this section, we convert the CSV file to a Pandas dataframe and then from a pandas dataframe to an SQLite database
csvName = twitterProfile + ".csv"
tweetsDF = pd.read_csv(csvName, sep=",") #Convert the CSV file to a Pandas dataframe
dbName = twitterProfile + ".sqlite"
db = sqlite3.connect(dbName)
db.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
tweetsDF.to_sql("Tweets", db, if_exists='replace', index=False) #Convert Pandas dataframe to SQLite database




#%%
#SQL EMBEDDED IN PYTHON ... YAY!! :)
#Getting the tweets with the top FavoriteCount
df = pd.read_sql_query('SELECT * FROM Tweets WHERE FavoriteCount > 75', db)
for column in df.columns:
	for idx in df[column].index:
		x = df.get_value(idx,column)
		try:
			x = unicode(x.encode('utf-8','ignore'),errors ='ignore') if type(x) == unicode else unicode(str(x),errors='ignore')
			df.set_value(idx,column,x)
		except Exception:
			print 'encoding error: {0} {1}'.format(idx,column)
			df.set_value(idx,column,'')
			continue
fileCSV = open('topFavorites.csv', 'wb')
df.to_csv(fileCSV, index=False, header = True, mode='a')
fileCSV.close()



#%%
#EFFECTS ON TIME OF TWEET ON AMOUNT OF AVERAGE VIRALITY:
temp = pd.DatetimeIndex(tweetsDF['CreatedAt'])
tempHour = pd.DataFrame(temp.hour)
tempDate = pd.DataFrame(temp.date)
tempTime = pd.DataFrame(temp.time)
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
tweetsDF.insert(1, 'Date', tempDate)
tweetsDF.insert(2, 'Year', tempYear)
tweetsDF.insert(3, 'Month', tempMonth)
tweetsDF.insert(4, 'Time', tempTime)
tweetsDF.insert(5, 'Hour', tempHour)
print 'Average Favorite Count For Each Hour Tweet Was Created At:'
print tweetsDF.groupby(['Hour'])['FavoriteCount'].mean()
print '\n'
print 'Average Retweet Count For Each Hour Tweet Was Created At:'
print tweetsDF.groupby(['Hour'])['RetweetCount'].mean()
print '\n'


#%%
#DATA PREP TO MAKE COMMON KEYS - 'Year' & 'Business Quarter' - THAT CAN BE USED TO COMBINE THIS DATA WITH EXTERNAL DATA SOURCE(S)
tweetsDF['BusinessQuarter'] = 'NA'
# tweetsDF['BusinessQuarter'][(tweetsDF['Month'] > 0) & (tweetsDF['Month'] <= 3)] = 'Q2'
# tweetsDF['BusinessQuarter'][(tweetsDF['Month'] >= 4) & (tweetsDF['Month'] <= 6)] = 'Q3'
# tweetsDF['BusinessQuarter'][(tweetsDF['Month'] >= 7) & (tweetsDF['Month'] <= 9)] = 'Q4'
# tweetsDF['BusinessQuarter'][(tweetsDF['Month'] >= 10) & (tweetsDF['Month'] <= 12)] = 'Q1'
tweetsDF.loc[((tweetsDF['Month'] > 0) & (tweetsDF['Month'] <= 3)), 'BusinessQuarter'] = 'Q2'
tweetsDF.loc[((tweetsDF['Month'] >= 4) & (tweetsDF['Month'] <= 6)), 'BusinessQuarter'] = 'Q3'
tweetsDF.loc[((tweetsDF['Month'] >= 7) & (tweetsDF['Month'] <= 9)), 'BusinessQuarter'] = 'Q4'
tweetsDF.loc[((tweetsDF['Month'] >= 10) & (tweetsDF['Month'] <= 12)), 'BusinessQuarter'] = 'Q1'


#%%
#AVERAGE VIRALITY OF ALL TWEETS:
print 'Average Retweets For All Tweets:'
print float(float(tweetsDF['RetweetCount'].sum()) / float(len(tweetsDF['RetweetCount'])))
print 'Average FavoriteCount For All Tweets:'
print float(float(tweetsDF['FavoriteCount'].sum()) / float(len(tweetsDF['FavoriteCount'])))
print '\n'

#%%
#EFFECTS OF HASHTAG AND INTERACTION ON AMOUNT OF AVERAGE VIRALITY:
tweetsWithHashtag = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE TweetText LIKE "%#%"', db)
print 'Average Retweets For Tweets With Hashtag:'
print round((tweetsWithHashtag['Retweets'].iloc[0]), 2)
print 'Average FavoriteCount For Tweets With Hashtag:'
print round((tweetsWithHashtag['Favorites'].iloc[0]), 2)
print '\n'

tweetsDirectedAtSomeone = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE TweetText LIKE "%@%"', db)
print 'Average Retweets For Tweets With @:'
print round((tweetsDirectedAtSomeone['Retweets'].iloc[0]), 2)
print 'Average FavoriteCount For Tweets With @:'
print round((tweetsDirectedAtSomeone['Favorites'].iloc[0]), 2)
print '\n'

#%%
#EFFECTS OF GIVEAWAYS ON AMOUNT OF AVERAGE VIRALITY:
tweetsAboutGiveaway = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%giveaway%"', db)
print 'Average Retweets For Tweets With Giveaway:'
print round((tweetsAboutGiveaway['Retweets'].iloc[0]), 2)
print 'Average FavoriteCount For Tweets With Giveaway:'
print round((tweetsAboutGiveaway['Favorites'].iloc[0]), 2)
print '\n'

#%%
#POPULARITY OF 'GLUTEN' IN TWEETS
tweetsAboutGluten = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%gluten%" OR LOWER(TweetText) LIKE "%gf%"', db)
print 'Average Retweets For Tweets About Gluten-Free:'
print round((tweetsAboutGluten['Retweets'].iloc[0]), 2)
print 'Average Favorites For Tweets About Gluten-Free:'
print round((tweetsAboutGluten['Favorites'].iloc[0]), 2)
print '\n'

#%%
#POPULARITY OF 'DAIRY' IN TWEETS:
tweetsAboutDairy = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%dairy%"', db)
print 'Average Retweets For Tweets About Dairy-Free:'
print round((tweetsAboutDairy['Retweets'].iloc[0]), 2)
print 'Average Favorites For Tweets About Dairy-Free:'
print round((tweetsAboutDairy['Favorites'].iloc[0]), 2)
print '\n'


#%%
#POPULARITY OF 'KOSHER' IN TWEETS:
tweetsAboutKosher = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%kosher%"', db)
print 'Average Retweets For Tweets About Kosher:'
print round((tweetsAboutKosher['Retweets'].iloc[0]), 2)
print 'Average Favorites For Tweets About Kosher:'
print round((tweetsAboutKosher['Favorites'].iloc[0]), 2)
print '\n'

#%%
#POPULARITY OF 'GMO' IN TWEETS:
tweetsAboutGMO = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%gmo%"', db)
print 'Average Retweets For Tweets About GMO:'
print round((tweetsAboutGMO['Retweets'].iloc[0]), 2)
print 'Average Favorites For Tweets About GMO:'
print round((tweetsAboutGMO['Favorites'].iloc[0]), 2)
print '\n'


#%%
#POPULARITY OF 'VEGAN' IN TWEETS:
tweetsAboutVegan = pd.read_sql_query('SELECT AVG(RetweetCount) AS Retweets, AVG(FavoriteCount) AS Favorites, COUNT(*) AS Num FROM Tweets WHERE LOWER(TweetText) LIKE "%vegan%"', db)
print 'Average Retweets For Tweets About VEGAN:'
print round((tweetsAboutVegan['Retweets'].iloc[0]), 2)
print 'Average Favorites For Tweets About VEGAN:'
print round((tweetsAboutVegan['Favorites'].iloc[0]), 2)


# fileUpdated = open('FINAL_Tweets.csv', 'wb')
# tweetsDF.to_csv(fileUpdated, index=False, header = True, mode='a')
# fileUpdated.close()

