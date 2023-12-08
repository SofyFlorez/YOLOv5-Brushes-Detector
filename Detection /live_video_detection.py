import torch
import cv2
import numpy as np

# model
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='/Users/sofyflorez/Documents/brushes_model/brushes.pt')

# Initialise video capture from camera
cap = cv2.VideoCapture(1)

while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Detection on video frame
    detect = model(frame)

    # Show FPS on video feed
    cv2.imshow('Brushes Detector', np.squeeze(detect.render()))

    # Wait for key press and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object
cap.release()
cv2.destroyAllWindows()



