import cv2

def preprocess(roi):
    return cv2.equalizeHist(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY))
