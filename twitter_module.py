#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This is the twitter module for downloading images from tweets
"""

import tweepy
import json
import wget
import os


def get_media_url_from_tweets(screen_name) -> set:
    """
    get media urls tweets
    @param: Twitter account name, ex: '@NatGeoPhotos'
    @return: Set of image urls
    """
    # Twitter API credentials
    consumer_key = input('Enter consumer key: ')
    consumer_secret = input('Enter consumer secret: ')
    access_key = input('Enter access key: ')
    access_secret = input('Enter access secret: ')

    # Twitter only allows access to a users most recent 3240 tweets with this method
    # authorize twitter, initialize tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    # save most recent tweets
    alltweets.extend(new_tweets)
    
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)
        
        # save most recent tweets
        alltweets.extend(new_tweets)
        
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))
    # save all media urls into set
    media_files = set()
    for status in alltweets:
        media = status.entities.get('media', [])
        if(len(media) > 0):
            media_files.add(media[0]['media_url'])
    print(f'\nThe number of media urls: {len(media_files)}')
    return media_files


def download_images(media_files):
    """
    download images from media urls and save to images folder
    @param: Set of image urls
    """

    # create the images folder
    if not os.path.exists('/images'):
        os.makedirs('images')
    
    downloaded = 1
    output_folder = 'images'
    for media_url in media_files:
        # only download if there is not a picture with the same name in the folder already
        file_name = f'image{downloaded:03}.jpg'
        if not os.path.exists(os.path.join(output_folder, file_name)):
            wget.download(media_url, out=output_folder+'/'+file_name)
            print(f'\nSuccessfully downloaded {file_name}')
            downloaded += 1