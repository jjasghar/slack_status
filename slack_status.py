#!/usr/bin/env python

import urllib2
import sys
from bs4 import BeautifulSoup

slack_status_page = 'https://status.slack.com/'

page = urllib2.urlopen(slack_status_page)

soup = BeautifulSoup(page, 'html.parser')

status_box = soup.find('h1', attrs={'class': 'black_licorice text_center width_100'})

status = status_box.text.strip()

if status == 'Smooth sailing!':
    print "Smooth Sailing!"
    stateid = 0
elif status == 'Connectivity issues for all customers':
    print "Connectivity issues for all customers"
    stateid = 2
else:
    print "Status is unknown, check the site: https://status.slack.com for more details"
    stateid = 1

sys.exit(stateid)
