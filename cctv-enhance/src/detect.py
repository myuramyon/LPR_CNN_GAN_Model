from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def detect_objects(frame):
    results = model(frame)
    return results[0].boxes.xyxy.cpu().numpy(), results[0].boxes.cls.cpu().numpy()
