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

def addObjs(img1 , objects, color=(255,0,0)):
    img = np.copy(img1)
    for (x,y,w,h) in objects
        img = cv2.rectangle(img, (x,y), (x+w , y+h), color, 2)
    return img

def obj_poly(obj)
    x,y,w,h = obj
    return Polygon([(x,y), (x+w ,y) , (x+w, y+h), (x, y+h)])

def objects_intersect(face, hands)
    if face and hands:
        facePoly = obj_poly(face[0])
        for hand in hands:
            handPoly = obj_poly(hand)
            if facePoly.intersects(handPoly):
                return True
    return False

