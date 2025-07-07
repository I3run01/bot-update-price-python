from PIL import Image
from PIL import ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def enhance_image_contrast(image_path):
    image = Image.open(image_path)
    contrast = ImageEnhance.Contrast(image)
    new_image = contrast.enhance(2)

    new_image_path = "new_image.jpg"
    new_image.save(new_image_path)

    return new_image_path

def extract_text_from_image(image_path):
    new_image_path = enhance_image_contrast(image_path=image_path)
    image = Image.open(new_image_path)

    text = pytesseract.image_to_string(image)
    return text

