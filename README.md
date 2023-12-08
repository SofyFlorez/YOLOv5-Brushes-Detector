# YOLOv5 Brushes Detector

This repository contains a Python script that utilizes the YOLOv5 object detection model to detect brushes in both live video feed and static images. The YOLOv5 model is loaded using PyTorch and the Ultralytics YOLOv5 hub. The code combines video capture functionality with real-time detection and static image detection.

<img width="477" alt="Screenshot 2023-12-07 at 15 23 48" src="https://github.com/SofyFlorez/YOLOv5-Brushes-Detector/assets/117933153/24f2fa4e-8a04-496e-a480-2b6f6fefc742">

## Data Generation

The synthetic data used for training was generated using the Jupyter Notebook file synthetic_data.ipynb. This notebook contains the code to generate synthetic data, including images with brushes in various scenarios to diversify the training dataset.

## Model Training

The YOLOv5 model used in this project was trained using Google Colab with the following parameters:

1000 synthetic data images for training
200 synthetic images for validation
Batch size: 16
Epochs: 100
Model: YOLOv5 X-Large
After training, the model weights were exported. You can download the trained weights file (best.pt) and use it for inference.

## Environment setup

To set up the environment optimally, please execute the following command:

https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt

## Usage

To read the weights with the PyTorch framework, run the following:

#### Live Video Detection

```bash
python live_video_detection.py
```

This command will open a video feed from the specified device index (in this case, index 1) and perform real-time brush detection. Press 'q' to exit the video feed.

#### Image Detection

```bash
python image_detection.py
```
This command will load a sample image for testing and display the brush detection results.

## Acknowledgements

YOLOv5: https://github.com/ultralytics/yolov5
