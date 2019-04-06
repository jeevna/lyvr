from PIL import Image

import pytesseract

def ocr(image):
    # image example = 'labsample1.jpg'
    img = Image.open(image)

    text = pytesseract.image_to_string(img, lang='eng')

    return (text)
