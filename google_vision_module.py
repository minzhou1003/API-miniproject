#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Min Zhou'
__copyright__ = 'Copyright 2018, API mini-project'
__email__ = 'minzhou@bu.edu'

"""
This is the google vision module for analyzing labels of video.
"""

import argparse
import os
from google.cloud import videointelligence


def analyze_labels(path):
    """ Detects labels given a GCS path. """
    # [START video_label_tutorial_construct_request]
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with open(path, 'rb') as movie:
        input_content = movie.read()
    operation = video_client.annotate_video(features=features, input_content=input_content)

    # [END video_label_tutorial_construct_request]
    print('\nProcessing video for label annotations:')

    # [START video_label_tutorial_check_operation]
    result = operation.result(timeout=90)
    print('\nFinished processing.')
    # [END video_label_tutorial_check_operation]

    # [START video_label_tutorial_parse_response]
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
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')
