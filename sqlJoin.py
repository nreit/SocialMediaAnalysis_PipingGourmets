import pandas as pd
import sqlite3

db = sqlite3.connect("allTweetsData.sqlite")
db.text_factory = str

#print 'Gluten'
glutenFree_tweets = pd.read_sql_query('SELECT * FROM Tweets WHERE LOWER(TweetText) LIKE "%gluten%" OR LOWER(TweetText) LIKE "%gf%"', db)
temp = pd.DatetimeIndex(glutenFree_tweets['CreatedAt'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
glutenFree_tweets.insert(1, 'Year', tempYear)
glutenFree_tweets.insert(2, 'Month', tempMonth)
glutenFree_tweets.loc[((glutenFree_tweets['Month'] > 0) & (glutenFree_tweets['Month'] <= 3)), 'BusinessQuarter'] = 'Q1'
glutenFree_tweets.loc[((glutenFree_tweets['Month'] >= 4) & (glutenFree_tweets['Month'] <= 6)), 'BusinessQuarter'] = 'Q2'
glutenFree_tweets.loc[((glutenFree_tweets['Month'] >= 7) & (glutenFree_tweets['Month'] <= 9)), 'BusinessQuarter'] = 'Q3'
glutenFree_tweets.loc[((glutenFree_tweets['Month'] >= 10) & (glutenFree_tweets['Month'] <= 12)), 'BusinessQuarter'] = 'Q4'
glutenFree_DF_Retweets = glutenFree_tweets.groupby(['Year', 'BusinessQuarter'])['RetweetCount'].sum().reset_index()
glutenFree_DF_Favorites = glutenFree_tweets.groupby(['Year', 'BusinessQuarter'])['FavoriteCount'].sum().reset_index()


#print 'Dairy'
dairy_tweets = pd.read_sql_query('SELECT * FROM Tweets WHERE LOWER(TweetText) LIKE "%dairy%"', db)
temp = pd.DatetimeIndex(dairy_tweets['CreatedAt'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
dairy_tweets.insert(1, 'Year', tempYear)
dairy_tweets.insert(2, 'Month', tempMonth)
dairy_tweets.loc[((dairy_tweets['Month'] > 0) & (dairy_tweets['Month'] <= 3)), 'BusinessQuarter'] = 'Q1'
dairy_tweets.loc[((dairy_tweets['Month'] >= 4) & (dairy_tweets['Month'] <= 6)), 'BusinessQuarter'] = 'Q2'
dairy_tweets.loc[((dairy_tweets['Month'] >= 7) & (dairy_tweets['Month'] <= 9)), 'BusinessQuarter'] = 'Q3'
dairy_tweets.loc[((dairy_tweets['Month'] >= 10) & (dairy_tweets['Month'] <= 12)), 'BusinessQuarter'] = 'Q4'
dairy_DF_Retweets = dairy_tweets.groupby(['Year', 'BusinessQuarter'])['RetweetCount'].sum().reset_index()
dairy_DF_Favorites = dairy_tweets.groupby(['Year', 'BusinessQuarter'])['FavoriteCount'].sum().reset_index()


#print 'Kosher'
kosher_tweets = pd.read_sql_query('SELECT * FROM Tweets WHERE LOWER(TweetText) LIKE "%kosher%"', db)
temp = pd.DatetimeIndex(kosher_tweets['CreatedAt'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
kosher_tweets.insert(1, 'Year', tempYear)
kosher_tweets.insert(2, 'Month', tempMonth)
kosher_tweets.loc[((kosher_tweets['Month'] > 0) & (kosher_tweets['Month'] <= 3)), 'BusinessQuarter'] = 'Q1'
kosher_tweets.loc[((kosher_tweets['Month'] >= 4) & (kosher_tweets['Month'] <= 6)), 'BusinessQuarter'] = 'Q2'
kosher_tweets.loc[((kosher_tweets['Month'] >= 7) & (kosher_tweets['Month'] <= 9)), 'BusinessQuarter'] = 'Q3'
kosher_tweets.loc[((kosher_tweets['Month'] >= 10) & (kosher_tweets['Month'] <= 12)), 'BusinessQuarter'] = 'Q4'
kosher_DF_Retweets = kosher_tweets.groupby(['Year', 'BusinessQuarter'])['RetweetCount'].sum().reset_index()
kosher_DF_Favorites = kosher_tweets.groupby(['Year', 'BusinessQuarter'])['FavoriteCount'].sum().reset_index()


#print 'GMO'
gmo_tweets = pd.read_sql_query('SELECT * FROM Tweets WHERE LOWER(TweetText) LIKE "%gmo%"', db)
temp = pd.DatetimeIndex(gmo_tweets['CreatedAt'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
gmo_tweets.insert(1, 'Year', tempYear)
gmo_tweets.insert(2, 'Month', tempMonth)
gmo_tweets.loc[((gmo_tweets['Month'] > 0) & (gmo_tweets['Month'] <= 3)), 'BusinessQuarter'] = 'Q1'
gmo_tweets.loc[((gmo_tweets['Month'] >= 4) & (gmo_tweets['Month'] <= 6)), 'BusinessQuarter'] = 'Q2'
gmo_tweets.loc[((gmo_tweets['Month'] >= 7) & (gmo_tweets['Month'] <= 9)), 'BusinessQuarter'] = 'Q3'
gmo_tweets.loc[((gmo_tweets['Month'] >= 10) & (gmo_tweets['Month'] <= 12)), 'BusinessQuarter'] = 'Q4'
gmo_DF_Retweets = gmo_tweets.groupby(['Year', 'BusinessQuarter'])['RetweetCount'].sum().reset_index()
gmo_DF_Favorites = gmo_tweets.groupby(['Year', 'BusinessQuarter'])['FavoriteCount'].sum().reset_index()


#print 'Vegan'
vegan_tweets = pd.read_sql_query('SELECT * FROM Tweets WHERE LOWER(TweetText) LIKE "%vegan%"', db)
temp = pd.DatetimeIndex(vegan_tweets['CreatedAt'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)
vegan_tweets.insert(1, 'Year', tempYear)
vegan_tweets.insert(2, 'Month', tempMonth)
vegan_tweets.loc[((vegan_tweets['Month'] > 0) & (vegan_tweets['Month'] <= 3)), 'BusinessQuarter'] = 'Q1'
vegan_tweets.loc[((vegan_tweets['Month'] >= 4) & (vegan_tweets['Month'] <= 6)), 'BusinessQuarter'] = 'Q2'
vegan_tweets.loc[((vegan_tweets['Month'] >= 7) & (vegan_tweets['Month'] <= 9)), 'BusinessQuarter'] = 'Q3'
vegan_tweets.loc[((vegan_tweets['Month'] >= 10) & (vegan_tweets['Month'] <= 12)), 'BusinessQuarter'] = 'Q4'
vegan_DF_Retweets = vegan_tweets.groupby(['Year', 'BusinessQuarter'])['RetweetCount'].sum().reset_index()
vegan_DF_Favorites = vegan_tweets.groupby(['Year', 'BusinessQuarter'])['FavoriteCount'].sum().reset_index()


tweetsFINAL_DF = pd.merge(glutenFree_DF_Retweets, dairy_DF_Retweets, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, kosher_DF_Retweets, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, gmo_DF_Retweets, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, vegan_DF_Retweets, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, glutenFree_DF_Favorites, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, dairy_DF_Favorites, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, kosher_DF_Favorites, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, gmo_DF_Favorites, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF = pd.merge(tweetsFINAL_DF, vegan_DF_Favorites, how='left', on=['Year', 'BusinessQuarter'])
tweetsFINAL_DF.columns = ['Year', 'BusinessQuarter', 'GlutenAVGRetweets', 'DairyAVGRetweets', 'KosherAVGRetweets', 'GmoAVGRetweets', 'VeganAVGRetweets', 'GlutenAVGFavorites', 'DairyAVGFavorites', 'KosherAVGFavorites', 'GmoAVGFavorites', 'VeganAVGFavorites']

print tweetsFINAL_DF






googleTrends = pd.read_csv('GoogleTrends_Attributes.csv', sep=",")

temp = pd.DatetimeIndex(googleTrends['Week'])
tempYear = pd.DataFrame(temp.year)
tempMonth = pd.DataFrame(temp.month)

googleTrends.insert(1, 'Month', tempMonth)
googleTrends.insert(2, 'Year', tempYear)

googleTrends['BusinessQuarter'] = 'NA'
googleTrends['BusinessQuarter'][(googleTrends['Month'] > 0) & (googleTrends['Month'] <= 3)] = 'Q2'
googleTrends['BusinessQuarter'][(googleTrends['Month'] >= 4) & (googleTrends['Month'] <= 6)] = 'Q3'
googleTrends['BusinessQuarter'][(googleTrends['Month'] >= 7) & (googleTrends['Month'] <= 9)] = 'Q4'
googleTrends['BusinessQuarter'][(googleTrends['Month'] >= 10) & (googleTrends['Month'] <= 12)] = 'Q1'

db = sqlite3.connect("GoogleOutput.sqlite3")
googleTrends.to_sql("GoogleTrends", db, if_exists='replace', index=False)

groupedGoogleTrends = pd.read_sql_query('SELECT Year, BusinessQuarter, AVG(GlutenFree) AS GlutenFree, AVG(Vegan) AS Vegan, AVG(DairyFree) AS DairyFree, AVG(Kosher) AS Kosher, AVG(GMO) AS GMO FROM GoogleTrends GROUP BY Year, BusinessQuarter', db)

print groupedGoogleTrends


MASTER_FINAL_DATA = pd.merge(groupedGoogleTrends, tweetsFINAL_DF, how='left', on=['Year', 'BusinessQuarter'])
print MASTER_FINAL_DATA

fileFinal = open('OutputAfterMerge.csv', 'w')
MASTER_FINAL_DATA.to_csv(fileFinal, sep=",", index=False, header=True)
fileFinal.close()

