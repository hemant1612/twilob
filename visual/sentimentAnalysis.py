import tweepy,re
from textblob import TextBlob
from . import models
class Analysis:
    def __init__(self):
        self.tweets = []

    def fetchTweets(self,searchTerm,NoOfTerms):
        # keys received from twitter for developer account
        apiKey = 'K3QBlgCPNL6gzMtEE4tPdSBKg'
        apiSecret = 'fgCOmIcBGe1KP4zw5JJVepUiJrs3CcAOjNnQVTWpu0iFNoWHVK'
        accessToken = '834397594944053249-41fRRVSDB1RnDIya4H9gexlTf0OfwW6'
        accessTokenSecret = 'tzGao8QrxFIpVv1etjkcrYM6JP4CYFEPCIqJ1Rl81vG0T'
        auth = tweepy.OAuthHandler(apiKey, apiSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)


        b = TextBlob("u"+ str(searchTerm))
        lan = 'en'
        self.tweets = tweepy.Cursor(api.search, q=searchTerm+' -filter:retweets', lang = lan,tweet_mode='extended').items(NoOfTerms)
        print(lan)

        positive = 0
        weaklyPositive = 0
        stronglyPositive = 0
        negative = 0
        weaklyNegative = 0
        stronglyNegative = 0
        neutral = 0



        models.positiveTweets.objects.all().delete()
        models.negativeTweets.objects.all().delete()
        for tweet in self.tweets:
            
#            if lan != 'hi':  
            analysis = TextBlob(self.removeURL(tweet.full_text))
#            else:
#                analysis = TextBlob(self.removeURL(tweet.full_text)).translate(to="en")
                
            if (analysis.sentiment.polarity>0):
                tweetObject=models.positiveTweets()
                tweetObject.tweetText=self.removeURL(tweet.full_text)
                tweetObject.userName=str(tweet.user.name)
                tweetObject.time=tweet.created_at
                tweetObject.save()
            if (analysis.sentiment.polarity<0):
                tweetObject=models.negativeTweets()
                tweetObject.tweetText=self.removeURL(tweet.full_text)
                tweetObject.userName=str(tweet.user.name)
                tweetObject.time=tweet.created_at
                tweetObject.save()
            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                weaklyPositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                stronglyPositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                weaklyNegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                stronglyNegative += 1

        return {'positive':positive,'wpositive':weaklyPositive,'spositive':stronglyPositive,'negative':negative,
                'wnegative':weaklyNegative,'snegative':stronglyNegative,'neutral':neutral}

    def cleanTweet(self, tweet):
        #removing mentions numbers
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])", " ", tweet).split())



    def removeURL(self,string):
        mylist=string.split()
        mystr=""
        for i in mylist:
            if len(i)>4 and i[0:4]=="http":
                continue
            else:
                mystr=mystr+i+" "
        return mystr