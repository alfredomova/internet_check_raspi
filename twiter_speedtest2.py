import sys, urllib, cStringIO, os, time

# sudo apt-get install python-pip

# pip install Pillow
from PIL import Image

# pip install twython
from twython import Twython

#  pip install speedtest-cli
import speedtest

print "run test >>>"

# Twitter application authentication
APP_KEY = ''

APP_SECRET = ''

OAUTH_TOKEN = ''

OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

s = speedtest.Speedtest()
s.get_config()
s.get_best_server()

speed_bps = s.download()
speed_mbps_down = round(speed_bps / 1000 / 1000, 1)

print speed_mbps_down

speed_bps = s.upload()
speed_mbps_up = round(speed_bps / 1000 / 1000, 1)

share = s.results.share()

MESSAGE_ = "@ISP \nDownload: " + str(speed_mbps_down) + "Mb/s \nUpload: " + str(speed_mbps_up) + "Mb/s "

print MESSAGE_

## -----------------------------

# download image
f = open('speedtest.png','wb')
f.write(urllib.urlopen(share).read())
f.close()

# upload it to twitter
imagen =  open('speedtest.png', 'rb')
image_ids = twitter.upload_media(media=imagen)

## -----------------------------
twitter.update_status(status=MESSAGE_, media_ids=[image_ids['media_id']])

print "<<< end test"

sys.exit()
