import torch
import cv2
import numpy as np

# model
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='/Users/sofyflorez/Documents/brushes_model/brushes.pt')

# Specify the path to the image you want to detect objects in
img_path = '/Users/sofyflorez/Documents/brushes_test/images/IMG_7748.jpg'

# Read the image using OpenCV
img = cv2.imread(img_path)

# Use the YOLOv5 model for object detection on the loaded image
detect = model(img)

# Display the detection results
cv2.imshow('Brushes Detector', np.squeeze(detect.render()))

# Wait for a key press to close the window
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
