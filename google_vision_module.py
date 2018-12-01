#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This is the google vision module for analyzing labels of video.
"""

from google.cloud import videointelligence
from google.cloud import vision
from google.cloud.vision import types
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

import os

def analyze_video_labels(path):
    """ Detects labels given a GCS path. """
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with open(path, 'rb') as movie:
        input_content = movie.read()
    operation = video_client.annotate_video(features=features, input_content=input_content)

    print('\nProcessing video for label annotations:')
    result = operation.result(timeout=90)
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print('Video label description: {}'.format(
            segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))

        for i, segment in enumerate(segment_label.segments):
            start_time = (segment.segment.start_time_offset.seconds +
                          segment.segment.start_time_offset.nanos / 1e9)
            end_time = (segment.segment.end_time_offset.seconds +
                        segment.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = segment.confidence

            # print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')


def detect_image_labels(directory_in_str):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    pathlist = Path(directory_in_str).glob('**/*.jpg')

    image_labels = []

    paths = []
    for path in pathlist:
        path_in_str = str(path)
        paths.append(path_in_str)
    # sort the paths by the filename index to match the database
    paths = sorted(paths, key = lambda x: int(x.split("/")[-1].split(".")[0][-3:]))

    for path in paths:
        with open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations

        score = labels[0].score
        description = labels[0].description

        message = f'Highest score: {score:.2}, Description: {description}'
        image_labels.append((score, description))
        print(message)
        add_label_to_image(path, message)

    print('\nFinished analysis!')
    return image_labels

def add_label_to_image(path, message):
    image = Image.open(path)
    draw = ImageDraw.Draw(image)

    # create font object with the font file and specify
    # desired size
    font = ImageFont.truetype('arial.ttf', size=25)
    # starting position of the message
    (x, y) = (50, 50)
    color = 'rgb(255, 0, 0)' # black color
    
    # draw the message on the background   
    draw.text((x, y), message, fill=color, font=font)   
    # save the edited image
    image.save(path)


