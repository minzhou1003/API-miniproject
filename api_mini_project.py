#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This is script downloads images from a twitter feed, 
convert them to a video and describe the content of the images in the video.
"""

from ffmpeg_module import image_to_video
from twitter_module import get_media_url_from_tweets, download_images
from google_vision_module import analyze_video_labels, detect_image_labels

import time
import argparse
import os
import sys


def main():

    # download images from Twitter
    print('Please enter your Twitter API credentials.')
    try:
        twitter_account = input('Please enter the Twitter Account:(ex:@NatGeoPhotos)')
        media_files = get_media_url_from_tweets(twitter_account)
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
        detect_image_labels(current_path + '/images')
    except:
        print('Google vision API failed, please export the JSON file and try again.')

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


if __name__ == '__main__':
    main()




