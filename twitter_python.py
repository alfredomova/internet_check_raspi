import sys, urllib, cStringIO, os, time
from PIL import Image
from twython import Twython

# Twitter application authentication
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

MESSAGE_ = "#isp  " # hashtag or mention your ISP

for idx, arg in enumerate(sys.argv):
        if idx == 1:
                MESSAGE_ = MESSAGE_ + arg
        elif idx == 2:
                # create an image file
                f = open('speedtest.png','wb')
                f.write(urllib.urlopen(arg).read())
                f.close()
				# upload it to twitter
                imagen =  open('speedtest.png', 'rb')
                image_ids = twitter.upload_media(media=imagen)
                # tweet the message + image
                MESSAGE_ = MESSAGE_ + " " + arg
                twitter.update_status(status=MESSAGE_, media_ids=[image_ids['media_id']])
				# remove the image
                os.remove('speedtest.png')
                sys.exit()
