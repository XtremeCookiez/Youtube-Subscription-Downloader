# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:53:24 2018

@author: Cameron
"""

maxAge = 1
subscriptionFile = 'subscription_manager.xml'

from pytube import YouTube
import feedparser as fp
import xml.etree.ElementTree as ET
import datetime
import os

tree = ET.parse(subscriptionFile)
root = tree.getroot()
videos = []
for subscription in root.iter('outline'):
    feed = fp.parse(subscription.get('xmlUrl'))
    title = subscription.get('title')
    title = title.replace('/', '')
    print(title)
    if not (os.path.exists(title)):
        os.makedirs(title)
    for entry in feed['entries']:
        age = age = datetime.datetime.now() - datetime.datetime.strptime(entry['published'].split('T')[0], "%Y-%m-%d")
        age = age.days
        if (age < maxAge):
            yt = YouTube(entry['link'])
            print('Downloading:', entry['title'], 'from', title)
            yt.streams.filter(file_extension='mp4', res='720p', progressive=True).first().download(title)
        else:
            print('No more videos from', title)
            break