import cv2
import numpy as np

class Vision(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    def get_frame(self):
        ret, self.frame = self.video.read()

    def show_frame(self):
        cv2.imshow('frame', self.frame)

    def detect_ball(self):
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        lower_orange = np.array([0, 109, 77])
        upper_orange = np.array([158, 255, 255])
        mask = cv2.inRange(hsv, lower_orange, upper_orange)
        res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
