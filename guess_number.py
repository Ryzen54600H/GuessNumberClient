import math
import numpy as np
import cv2
import onnxruntime as ort
import random

class NumberGuesser():
    """
    Refer: https://github.com/onnx/models/tree/main/vision/classification/mnist
    Download checkpoints: https://github.com/onnx/models/blob/main/vision/classification/mnist/model/mnist-12.onnx
    """
    def __init__(self):
        self.image_size = (28, 28)
        self.model = self.load_model("checkpoints/mnist-12.onnx")
        
        # threshold for determine guess or not
        self.threshold = 0.9
        
    def load_model(self, path):
        ort_sess = ort.InferenceSession(path)
        
        return ort_sess
    
    def preprocess_image(self, image):
        image[image == 2] = 0
        if(len(image.shape) == 1):
            img_size = int(math.sqrt(image.shape[0]))
            image = image.reshape((img_size, img_size))
            
        image = cv2.resize(image.astype(np.float32), self.image_size)
        return image[np.newaxis, np.newaxis, ...]
    
    def softmax(self, x):   
        """Compute softmax values for each sets of scores in x."""
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def run(self, image):
        prep_img = self.preprocess_image(image)
        outputs = self.model.run(None, {'Input3': prep_img})[0]
        
        probs = self.softmax(outputs[0])
        idx = np.argmax(probs)
        
        if (random.choice([0, 1]) == 0 and probs[idx] >= self.threshold):
            return idx
        return 100

        