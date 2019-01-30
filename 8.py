from tweepy import OAuthHandler
from tweepy import API
consumer_key="vVzBcI55kw02vy84SWXBQzOa2"
consumer_secret="sCh7ThurBejL8sTN3BIybRlsf2hCKfR9ZgWcG41j9js9I6rFJR"
access_token="2451885708-PamQxDd4OqoeXuyKk0OB19jtvpAMFuhCshqM0vW"
access_token_secret="RGEBcPnk59c26ScyU6K0fnwF0VgjOx3jJW8zd71L3AoUY"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
account_list = [None]*2

account1 = input("Εισάγεται Το Όνομα Του Πρώτου Χρήστη:")
account2 = input("Εισάγεται Το Όνομα Του Δεύτερου Χρήστη:")
account_list[0] = account1
account_list[1] = account2

itemOne = auth_api.get_user(account1)
itemTwo = auth_api.get_user(account2)

followersOne = int(itemOne.followers_count)
followersTwo = int(itemTwo.followers_count)

tweetsOne = auth_api.user_timeline(screen_name=account1, count=10)
tweetsTwo = auth_api.user_timeline(screen_name=account2, count=10)

tmpOne = []
tmpTwo = []

tweets_One = [tweet.text for tweet in tweetsOne]  
for j in tweets_One:
    tmpOne.append(j)

tweets_Two = [tweet.text for tweet in tweetsTwo]  
for j in tweets_Two:
    tmpTwo.append(j)

tweet_len_one = 0
tweet_len_two = 0

for i in range(len(tmpOne)):
    lenght = len(tmpOne[i].split())
    tweet_len_one = tweet_len_one + lenght

for i in range(len(tmpTwo)):
    lenght = len(tmpTwo[i].split())
    tweet_len_two = tweet_len_two + lenght

AmmountOne = followersOne * tweet_len_one
AmmountTwo = followersTwo * tweet_len_two

if AmmountOne>AmmountTwo:
    print("Ο "+account1+" έχει το μεγαλύρερο γινόμενο")
elif AmmountTwo>AmmountOne:
    print("Ο "+account2+" έχει το μεγαλύτερο γινόμενο")
elif AmmountOne==AmmountTwo:
    print("Και οι δύο χρήστες έχουν το ίδιο γινόμενο")