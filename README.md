# API-miniproject
This is the mini project from EC601.

Author: Min Zhou

Email: minzhou@bu.edu

## Description:
This a python library that downloads images from a twitter feed, convert them to a video and describe the content of the images in the video, and it also can output the label of the video.

## Useful software components:
- Twitter API
- FFMPEG
- Google Vision API, Google Intelligence Video API

## File instruction:
- `images/ ` is the folder to store the images collected by Twitter API.
- `api_mini_project.py` is the script to for this project.
- `ffmpeg_module.py`, `twitter_module.py` and `google_vision_module.py` is neccessary first party libraries for this project.

## Installation:
- python 3
- virtualenv
- Twitter API credential
- [Google Vision API](https://cloud.google.com/vision/docs/), [Google Intelligence Video API](https://cloud.google.com/video-intelligence/docs/) credential JSON key.

    _Note: this project is only tested on MAC OS._

1. Create a test folder and activate virtualenv inside that folder, check [this](https://cloud.google.com/python/setup).

2. Inside above test folder:
```
git clone https://github.com/minzhou1003/API-miniproject.git
```

3. Go to API-miniproject folder:
```
cd API-miniproject
pip install -r requirements.txt
```

4. Put the Google API JSON key under this folder

    _Note: you should enable both Google Vision API and Google Intelligence Video API._


5. Run the test code:
```
python api_mini_project.py
```
_You will be asked to enter your Twitter API credential_.

6. After successfully run the code, you will get downloaded images with labels and a `result.mp4` video inside the `/images` folder.


## Sprint 1:
- [x] Study the general functions of all APIs
- [x] Define the function of each module
- [x] Implement a shell for the module

## Sprint 2:
- [x] Implement the twitter module

## Sprint 3:
- [x] Implement the FFMPEG module

## Sprint 4:
- [x] Implement the Vision module

## Test:
- [x] Test the FFMPEG module
- [x] Test the twitter module
- [x] Test the google-vision module
- [x] Test all parts

## Test code result: 

Images from [@NatGeoPhotos](https://twitter.com/NatGeoPhotos)

[![](https://img.youtube.com/vi/7jhDZyZXr1I/0.jpg)](https://www.youtube.com/watch?v=7jhDZyZXr1I)

```
Image label detection using Google vision API:
Highest score: 0.93, Description: bird
Highest score: 0.94, Description: water
Highest score: 0.98, Description: brown bear
Highest score: 0.96, Description: nature
Highest score: 0.99, Description: giraffe
Highest score: 0.96, Description: photograph
Highest score: 0.89, Description: fauna
Highest score: 0.9, Description: sky
Highest score: 0.94, Description: nature
Highest score: 0.95, Description: nature
Highest score: 0.98, Description: reflection
Highest score: 0.97, Description: sky
Highest score: 0.93, Description: tree
Highest score: 0.87, Description: arctic
Highest score: 0.96, Description: bird
Highest score: 0.95, Description: great ape
Highest score: 0.94, Description: bird
Highest score: 0.96, Description: cephalopod
Highest score: 0.87, Description: sky
Highest score: 0.98, Description: bird
Highest score: 0.7, Description: organism
Highest score: 0.96, Description: white
Highest score: 0.86, Description: stage
Highest score: 0.8, Description: wood
Highest score: 0.95, Description: nature
Highest score: 0.92, Description: ecosystem
Highest score: 0.88, Description: fauna
Highest score: 0.77, Description: poster
Highest score: 0.98, Description: fox
Highest score: 0.89, Description: water
Highest score: 0.97, Description: wildlife
Highest score: 0.93, Description: fauna
Highest score: 0.87, Description: tree
Highest score: 0.95, Description: sky
Highest score: 0.97, Description: flamingo
Highest score: 0.95, Description: sky
Highest score: 0.92, Description: sky
Highest score: 0.93, Description: mammal
Highest score: 0.92, Description: mammal
Highest score: 0.98, Description: reflection
Highest score: 0.9, Description: tree
Highest score: 0.92, Description: fauna
Highest score: 0.88, Description: dog
Highest score: 0.97, Description: squirrel
Highest score: 0.95, Description: sky
Highest score: 0.94, Description: sky
Highest score: 0.94, Description: ecosystem
Highest score: 0.95, Description: wildlife
Highest score: 0.97, Description: blue
Highest score: 0.95, Description: black
Highest score: 0.83, Description: black and white
Highest score: 0.84, Description: sky
Highest score: 0.94, Description: water
Highest score: 0.97, Description: lavender
Highest score: 0.97, Description: blue
Highest score: 0.97, Description: honey bee
Highest score: 0.98, Description: tree
Highest score: 0.98, Description: wildlife
Highest score: 0.55, Description: girl
Highest score: 0.96, Description: sky
Highest score: 0.98, Description: fireworks

...

Video label analysis using Google vision API:

Processing video for label annotations:
Video label description: wildlife
	Label category description: animal
	Confidence: 0.6899771690368652


Video label description: photography
	Confidence: 0.47163185477256775


Video label description: animal
	Confidence: 0.7916033267974854


Video label description: nature
	Confidence: 0.9364510774612427
```
