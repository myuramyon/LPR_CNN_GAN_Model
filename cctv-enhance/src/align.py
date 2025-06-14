import cv2
import numpy as np

def align_plate(roi):
    # placeholder: here you'd detect the four corners and apply homography
    h, w = roi.shape[:2]
    return cv2.resize(roi, (w, h))
