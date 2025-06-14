import cv2

def draw_info(frame, boxes, texts):
    for (x1,y1,x2,y2), text in zip(boxes, texts):
        cv2.rectangle(frame, (int(x1),int(y1)), (int(x2),int(y2)), (0,255,0), 2)
        cv2.putText(frame, text, (int(x1), int(y1)-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
    return frame
