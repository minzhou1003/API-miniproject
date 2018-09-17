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


def image_to_video(video_name):
    """
    convert a set of images to video
    """
    current_path = os.getcwd()
    os.chdir(current_path + '/images')
    print('images:')
    print(subprocess.check_output(['ls']))
    subprocess.call(['ffmpeg', '-framerate', '1', '-i', 'image%03d.jpg', video_name])
    print('Video successfully saved.')
