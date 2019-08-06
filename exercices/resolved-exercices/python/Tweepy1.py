import tweepy

auth = tweepy.OAuthHandler(KDyHPrlzyi8zPhdbOHf2f49sL, uM9fTIplWbzOS1VtL0uyvHfqf5Ypgv4jbRNT5XppvrYBl4nvw9)
auth.set_access_token(1144658096574386176-R0G2FcCQaxrXLKDmsiQgINcki0tcur, jEambrj6g81eus1hsRWJg2YvWK5fQiwv5WyVyXCb6sDVO)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
