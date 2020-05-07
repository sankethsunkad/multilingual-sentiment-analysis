from tweepy import streaming
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import time
import re

#Variables that contains the user credentials to access Twitter API 
access_token = "1227931108597088256-C72eGskn7ICdaoUMC2IlKyxsaQXvlC"
access_token_secret = "KNqDlxbvkUWDAjeGAVJRqGxGGCWgw2HL2jbXJbKMAYapW"
consumer_key = "2RexuOx5ul8cdzuy2PJKkf9LY"
consumer_secret = "DcjceoOvb3KCPPoweO0zbxtNbPUT4BWICIvhcix4VR3o8HMNpl"


#This is a basic listener that just prints received tweets to stdout.
class listener(StreamListener):

    def on_data(self, data):

        try:
            #print(data)
            tweet = data.split(',"text":"')[1].split('","')[0]
            print(tweet)
            saveThis = str(time.time())+'::'+tweet
            saveFile=open('twitdb.csv','a')
            unicode_literal = re.compile(r'\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}')
            saveThis=(unicode_literal.sub(r'', saveThis))
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print('Failed ondata',str(e))
            time.sleep(5)
    def on_error(self, status):
        print(status)

auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
twitterStream=Stream(auth,listener())
twitterStream.filter(track=["india"])