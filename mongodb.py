#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This script creates a database and records all transactions.
"""


from ffmpeg_module import image_to_video
from twitter_module import get_media_url_from_tweets, download_images
from google_vision_module import analyze_video_labels, detect_image_labels

from pymongo import MongoClient
import time
import datetime
import argparse
import os
import sys



client = MongoClient()

db = client['twitter_mongodb']
posts = db.posts

def create_post():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M %S'))
    
    try:
        twitter_account = input('Please enter the Twitter Account:(ex:@NatGeoPhotos) ')
        try:
            num_images = int(input('Enter the number of images to download: '))
            media_files = list(get_media_url_from_tweets(twitter_account))[:num_images]
            total_images = num_images
        except:
            media_files = list(get_media_url_from_tweets(twitter_account))
            total_images = len(media_files)
    except:
        print('\nTwitter API auth failed, please check your credentials.')
        sys.exit(1)
    time.sleep(1)

    try:
        download_images(media_files)
    except:
        print('\nFailed to download images, please delete the /images folder and try again.')
        sys.exit(1)
    # analyze the label of the images and video
    current_path = os.getcwd()

    # Google vision API
    print('\nImage label detection using Google vision API:')
    try:
        image_labels = detect_image_labels(current_path + '/images') # list of tuples
    except:
        print('Google vision API failed, please export the JSON file and try again.')
        sys.exit(1)

    # convert to video using ffmpeg
    print('\nConverting to video...')
    image_folder_path = current_path + '/images'
    video_name = 'result.mp4'
    try:
        image_to_video(video_name, image_folder_path)
    except:
        print('Failed to convert to video, please try again.')
    # Google video intelligence API
    print('\nVideo label analysis using Google vision API:')
    try:
        analyze_video_labels(current_path + '/images/result.mp4')
    except:
        print('Google video intelligence API failed, please export the JSON file and try again.')

    post_data = {
        'unix': unix,
        'datestamp': date,
        'account': twitter_account,
        'total_images': total_images,
        'image_url': media_files,
        'image_label': image_labels
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))
    return twitter_account

def retrieve_post(twitter_account):
    twitter_posts = posts.find_one({'account': twitter_account})
    print(twitter_posts)


twitter_account = create_post()
print('\nMongoDB posts created!')
print(f'\nRetrieving the post with account is {twitter_account}:\n')
retrieve_post(twitter_account)


