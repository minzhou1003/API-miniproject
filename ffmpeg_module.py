#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This is the ffmpeg module for converting a set of images to a video using ffmpeg API
"""

import subprocess
import os


def image_to_video(video_name, image_folder_path):
    """
    convert a set of images to video
    @param: video_name is a string of video file, ex: 'result.mp4'
    @param: image_folder_path is the path of the images folder
    """
    os.chdir(image_folder_path)
    subprocess.call(['ffmpeg', '-framerate', '1', '-i', 'image%03d.jpg', video_name])
    print(f'\nVideo successfully saved as {video_name}.')
