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

import sqlite3
import time
import datetime
import argparse
import os
import sys


# connect/create a database
conn = sqlite3.connect('twitter.db')
c = conn.cursor()

# create the table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS twitter_table(unix REAL, datestamp TEXT, account TEXT, \
    total_images REAL, image_url TEXT, image_label TEXT, score REAL)')


def dynamic_data_entry():
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
        exit(1)

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
    for i in range(total_images):
        c.execute('INSERT INTO twitter_table (unix, datestamp, account, total_images, image_url, image_label, score) \
            VALUES (?, ?, ?, ?, ?, ?, ?)', (unix, date, twitter_account, total_images, media_files[i], image_labels[i][1], image_labels[i][0]))
        time.sleep(1)
    
    conn.commit()

create_table()
dynamic_data_entry()
c.close()
conn.close()
print('Database successfully saved as twitter.db')
