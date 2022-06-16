import cv2 as cv
import numpy as np

# Blank Image
# dtype = data type of an image
# Give size of height, width, and the number of colour channels
blank = np.zeros((500,500, 3), dtype = 'uint8')

img = cv.imread('Image/Cat_1.jpg')


# Paint image a certain colour
# [:] = reference all the pixels and set them a certain colour
blank[:] = 0,255,0
cv.imshow('Cat', blank)
# Set certain colour to certain pixel
blank[200:300, 300:400] = 0,0,255

# Draw a Rectangle Method
# Takes 2 points
cv.rectangle(blank, (0,0), (255, 255), (255, 0, 0), thickness=2)
cv.imshow('Bob', blank)

# Fill Rectangle
cv.rectangle(blank, (0,0), (255, 255), (255, 0, 0), thickness=cv.FILLED)
cv.imshow('Fill', blank)

# Draw A Circle
# 2nd parameter is pos centre of circle
cv.circle(blank, (370, 370), 30, (255,0,0), 4)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (100,100), (200,200), (0,255,255), 4)
cv.imshow('line', blank)

# Write Text
# org = position of text
# fontFAce = Type of Font
# scale = Size of text
cv.putText(blank, "LoL", (300,200), fontScale=1, color=(200,200,200), thickness=2, fontFace=cv.FONT_HERSHEY_TRIPLEX)
cv.imshow('Text', blank)

cv.waitKey(0)

