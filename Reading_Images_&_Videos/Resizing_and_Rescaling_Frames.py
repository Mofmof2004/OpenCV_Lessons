import cv2 as cv

# Rescaling video implies changing height and width
# Frame and scale value
# Scale value default is 0.75
def rescaleFrame(frame, scale=0.75):
    # frame.shape[1] = width
    # frame.shape[0] = height
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Return frame resized a articular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Change resolution
# Only work on LIVE VIDEO
def changeResolution(width, height):
    # 3 references the width
    # 4 references the height
    capture.set(3, width)
    capture.set(4, height)

