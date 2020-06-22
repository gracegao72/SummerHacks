import os
import cv2
import numpy as np
import cvlib as cv
import tensorflow as tf
from shapely.geometry import Polygon


class Detector:
    detector_params = {}
    detector = None

    def __init__(self):
        pass

    def set_detector_params(self, params):
        self.detector_params = params

    def detect(self):
        pass


class CVLibDetector(Detector):
    def __init__(self):
        self.detector = cv

    def detect(self, rgb_image):
        # returns an array of coordinates (top, bottom, right left)
        faces, confidences = self.detector.detect_face(rgb_image)
        # change to array of (x, y, w, h)
        return [(top, left, bottom - top, right - left) for (top, right, bottom, left) in faces]
    
# add class TS Detector

