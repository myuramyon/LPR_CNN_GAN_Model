import cv2, json, csv
from capture import capture_frames
from detect import detect_objects
from align import align_plate
from superres import enhance_sr
from enhance import preprocess
from ocr import recognize
from overlay import draw_info

def main(input_path, output_path):
    writer = None
    logs = []
    for frame in capture_frames(input_path):
        boxes, classes = detect_objects(frame)
        texts = []
        for box in boxes:
            x1,y1,x2,y2 = map(int,box)
            roi = frame[y1:y2, x1:x2]
            roi = align_plate(roi)
            roi = enhance_sr(roi)
            gray = preprocess(roi)
            text = recognize(gray)
            texts.append(text)
        out = draw_info(frame, boxes, texts)
        if writer is None:
            h,w = out.shape[:2]
            writer = cv2.VideoWriter(output_path,
                                     cv2.VideoWriter_fourcc(*'mp4v'),
                                     20, (w,h))
        writer.write(out)
        logs.append({'boxes': boxes.tolist(), 'texts': texts})
    writer.release()
    with open('logs.json','w') as f:
        json.dump(logs, f)
    with open('logs.csv','w', newline='') as f:
        csv.writer(f).writerows([list(item.values()) for item in logs])

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
