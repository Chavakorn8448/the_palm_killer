import picamera

with picamera.PiCamera() as camera:
    # Set camera resolution (you can adjust it based on your needs)
    camera.resolution = (2592, 1944)  # Max resolution for v2.1 camera

    # Optional: Provide a preview, which is useful for adjusting camera position
    camera.start_preview()
    
    # Allow the camera to warm-up
    import time
    time.sleep(2)

    # Capture the image
    camera.capture('captured_image.jpg')
    
    camera.stop_preview()
