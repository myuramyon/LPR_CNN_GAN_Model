import easyocr

reader = easyocr.Reader(['en'])

def recognize(roi):
    text = reader.readtext(roi, detail=0)
    return text[0] if text else ""
