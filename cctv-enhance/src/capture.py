import cv2

def capture_frames(input_path):
    cap = cv2.VideoCapture(input_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()
