import cv2
import numpy as np
import picamera
from picamera.array import PiRGBArray

# Initialize the camera
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32

# Create a raw capture object to hold the frames
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
import time
time.sleep(0.1)

# Capture the frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    
    # Use OpenCV to process the image (if you want to)
    # For demonstration, we'll just convert the image to grayscale and show it
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Show the image
    cv2.imshow("Frame", gray)
    
    # Clear the stream for the next frame
    rawCapture.truncate(0)
    
    # If you press 'q', exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
