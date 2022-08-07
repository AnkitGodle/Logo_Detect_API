from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import torch

max_size = 640
def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded)).convert("RGB")
    width, height = pil_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = pil_image.resize((int(pil_image.width * resize_factor),int(pil_image.height * resize_factor)))
    return pil_image

def get_yolov5():
    model = torch.hub.load('./app/yolov5', 'custom', path='./app/yolov5/runs/train/exp9/weights/best.pt', source='local')
    model.conf = 0.5
    return model



