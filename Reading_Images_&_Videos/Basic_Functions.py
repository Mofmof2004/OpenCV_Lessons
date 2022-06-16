import cv2 as cv
img = cv.imread('Image/Cat_1.jpg')


def converting_an_image_greyscale(img):
    # Colour convert Method
    # Colour BGR to GrayScale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)
    cv.waitKey(0)


def BLur(img):
    # Blur Remove noise from an image
    # Use Gaussain blur technique
    # ksize need to be 2 values + odd number - Use amount of Blur
    blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
    cv.imshow("blur", blur)
    cv.waitKey(0)

def Edge_cascade():
    # Edge Cascade
    # Find Edges in an Image
    # Use canny edge cascade method
    # Two threshold values
    canny = cv.Canny(blur,175, 225)
    cv.imshow("canny", canny)
    cv.waitKey(0)


def dilated():
    dilated = cv.dilate(canny, (7,7), iterations=3)
    cv.imshow("canny", dilated)
    cv.waitKey(0)

# Opposite of dilated
# eroded = cv.erode(img, (3, 3), iterations=1)
# cv.imshow("eroded", eroded)
# cv.imshow("img", img)
# cv.waitKey(0)

# Resize Image
Resized = cv.resize(img, (500,500))
# can interpolate
# Shrinking
Shrinking = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
Enlarging = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
# Slowest
Enlarging_High_QUALITY = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)


# Cropping
# Select Region
cropped = img[50:200, 50:150]
cv.imshow("Crooped", cropped)
cv.waitKey(0)





