from datetime import date
import tweepy


last_day = date(year=date.today().year, month=12, day=31)
calculation = last_day - date.today()
year_gone = 365 - calculation.days
percentage = round((year_gone*100) / 365)

consumer_key = 'insert-your-consumer-key'
consumer_secret = 'insert-your-consumer-secret'
access_token = 'insert-your-access-token'
access_token_secret = 'insert-your-access-token-secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# You can customize this anyway you want! variable 'percentage' holds the calculation, so go nuts!
message = f'#PythonBot - Hey! This year is already at {percentage}%! This is a gentle reminder to enjoy your day!'
api.update_status(message)
#api.update_status("Hello Tweepy")

