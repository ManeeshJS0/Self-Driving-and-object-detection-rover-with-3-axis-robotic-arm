import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn
import cv2
import numpy as np

class ObjectDetection:
    def __init__(self):
        # Load pre-trained Faster R-CNN model
        self.model = fasterrcnn_resnet50_fpn(pretrained=True)
        self.model.eval()

        # Define transformations for image preprocessing
        self.transform = T.Compose([
            T.ToTensor(),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def detect_objects(self, frame):
        # Convert the frame to a PyTorch tensor
        input_tensor = self.transform(frame)
        input_batch = input_tensor.unsqueeze(0)

        # Run inference
        with torch.no_grad():
            prediction = self.model(input_batch)

        # Extract bounding boxes and labels from the prediction
        boxes = prediction[0]['boxes'].cpu().numpy()
        labels = prediction[0]['labels'].cpu().numpy()

        # Extract object positions from the bounding boxes
        object_positions = [(int((box[0] + box[2]) / 2), int((box[1] + box[3]) / 2)) for box in boxes]

        return object_positions
