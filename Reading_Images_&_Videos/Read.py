import cv2 as cv


def Reading_images():
    # Method takes in a path to an image
    # Return image as pixels
    img = cv.imread('Image/Cat_1.jpg')

    # Display_ image as a new window
    # Paramters: Name of Window, matrix of pixels
    cv.imshow('Cat', img)

    # method wich wait for a certain amount of time for a keyboard key to be pressed
    # Wait for an infinite amount of time
    cv.waitKey(0)

def Reading_videos():

    # Take a path to a video
    # Or integer using camera
    capture = cv.VideoCapture(0)
    # Use a while loop and read the video frame by frame
    while True:
        # Read Video Frame by Frame
        # Return the Frame and a Boolean saying if the frame was successfully read or not
        isTrue, frame = capture.read()
        # Display invidual frame
        cv.imshow('Video', frame)

        # To Break out of the While loop
        # If letter d is presses break from while loop
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    # Release Capture pointer
    capture.release()
    # Destroy all windows
    cv.destroyAllWindows()







Reading_videos()
