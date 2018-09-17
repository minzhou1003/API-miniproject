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
from google_vision_module import analyze_labels

import time
import argparse
import os


def main():

    # download images
    media_files = get_media_url_from_tweets("@BU_Tweets")
    time.sleep(2)
    download_images(media_files, len(media_files))

    # convert to video
    image_to_video('v.avi')

    # analyze the label of the video
    parser = argparse.ArgumentParser(description=__doc__, 
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('path', help='GCS file path for label detection.')
    args = parser.parse_args()

    analyze_labels(args.path)

if __name__ == '__main__':
    main()




