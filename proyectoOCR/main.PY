""" import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_path = 'img1.jpg'
reader = easyocr.Reader(['en','es'])

results = reader.readtext(image_path, paragraph="false")

text = ''
for result in results:
    text += result[1] + ' '

print (text) """

import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_path = 'img2.jpg'
reader = easyocr.Reader(['en','es'])

results = reader.readtext(image_path, paragraph="false")

text = ''
for result in results:
    text += result[1] + ' '

print (text)