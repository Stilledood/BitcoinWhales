import tweepy
from twython import Twython
from auth import API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_SECRET_TOKEN

class Tweeter:
    '''Class to connect to the tweeter api and post tweets'''
    api_key=API_KEY
    api_secret_key=API_SECRET_KEY
    access_token=ACCESS_TOKEN
    access_secret_token=ACCESS_SECRET_TOKEN




    def __init__(self,client=None):
        self.client=client


    def connect_to_api(self):
        self.client=tweepy.Client(
            consumer_key=self.api_key,consumer_secret=self.api_secret_key,access_token=self.access_token,access_token_secret=self.access_secret_token
        )




    def post_tweet(self,text):
        response=self.client.create_tweet(text=text)




