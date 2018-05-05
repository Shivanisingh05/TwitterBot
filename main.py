from twitter import Twitter, OAuth
import tweepy
import textblob
from textblob import TextBlob
API_KEY = 'OZdisl10940KgoyOOiVXheGv5'
API_SECRET = 'jWXndj1SMWMnP1ISvU0lj2fyt7tcEQUJV5O6ziyFB52HljqKJU'
ACCESS_TOKEN = '990982189818044417-3V8KzMJEOhTR9b4PEzkUXpl4b9izCw2'
ACCESS_TOKEN_SECRET = 'ndU8rHLVbIE75GkrJz5PvVTuXXFsYerYEdoRSf0ePtdUF'

twitter_oauth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth = twitter_oauth)

def get_tweets(query):
    tweets = twitter.search.tweets(q='#' +query, count=100)
    return tweets

def get_num_followers(query):
    num_followers = 0
    tweets = get_tweets(query)
    #print type(tweets)
    for each_tweet in tweets['statuses']:
        print each_tweet['user']['followers_count']
        num_followers += each_tweet['user']['followers_count']
    return  num_followers

def sentiments(query):
    oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    oauth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(oauth)
    public_tweets = api.search(query)
    for tweet in public_tweets:
        print(tweet.text)
        analyse = TextBlob(tweet.text)
        print(analyse.sentiment)
        print(analyse.detect_language())
        print("######################################################################################################")


def main():
 while (True):
    user_choice = input("What would you like to do? \n"
                   "1. Count the number of people Tweeting using a certain hash tag.\n"
                   "2. Determine the location, timezone and language of people Tweeting using a certain has tag.\n"
                   "3. Number of times Modi has referred USAin the past 200 tweets compared to how many time Trumph has mentioned India.\n"
                   "4. Determine the sentiments of people Tweeting using a certain has tag.\n"
                   "5. Top used word by PM MODI on twitter.\n"
                   "6. Tweet a message from your account.\n"
                   "7. Exit\n")


    if user_choice == 1:
        user_input = raw_input("Enter the has tag: ")
        print "\n\nTotal number of people who might have seen this has tag are: %s" % (get_num_followers(user_input))
    elif user_choice == 2:
        user_input = raw_input("Enter the has tag: ")

    elif user_choice == 3:
        pass
        #user_input = raw_input("Enter the has tag.")

    elif user_choice == 4:
        user_input = raw_input("Enter the has tag: ")
        (sentiments(user_input))
    elif user_choice == 5:
       pass
       #user_input = raw_input("Enter the has tag.")

    elif user_choice == 6:
        user_input = raw_input("Enter the has tag.")
    elif user_choice == 7:
       break
    else:
        print("wrong choice try again.")
        exit()
main()