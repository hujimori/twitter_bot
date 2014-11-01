#coding: utf-8
from requests_oauthlib import OAuth1Session
import codecs
import json
import sys
import random

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)


CK = "Dyx2XcIXoexa31kcWcKTzxNiM" 						  # consumer key
CS = "Cjy6ZOD7d25AeXrCBRr5G7XXBtr0aRb9ALCzrdn8WSnUyQpIvs" # consumer sercet
AT = "2678756287-IpL4tN87ahCeBPA6EeDvtIzsMxddCWQhTFlD7qe" # access token
AS = "XUK9BYkrgIWGDtSEngTZiIka33iSFapqPhwyPHmAoy0ig"	  # access token sercet



# ホームタイムライン取得用のエンドポイント
home_timeline_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
# ユーザータイムライン取得用のエンドポイント
user_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json"
# ツイート投稿用エンドポイント
update_url = "https://api.twitter.com/1.1/statuses/update.json"

req_params = {"screen_name":"WonChuKissMe","count":"200"}
# OAuth で GET/usr/local/lib/python2.7/site-packages
twitter = OAuth1Session(CK, CS, AT, AS)

# 指定したユーザーのタイムライン取得
req = twitter.get(user_timeline, params = req_params)
if req.status_code == 200:
	timeline = json.loads(req.text)
else:
	print ("error: %d" % req.status_code)
# ランダムにツイート取得
post_params = {}
numbers = range(1, 1000)
status = [(x, y) for x in timeline for y in numbers]
status = random.choice(status)
tweet = status[0]["text"]
#print u(tweet)

# ランダムに取得したツイートをツイートする
post_params["status"] = tweet
post = twitter.post(update_url, params = post_params)
if post.status_code == 200:
	print "success"
else:
	print ("error: %d" % post.status_code)

	