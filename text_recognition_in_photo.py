import pytesseract
from PIL import Image

image = Image.open('')  # путь к изображению
pytesseract.pytesseract.tesseract_cmd = r''  # путь к pytesseract для пользователей Windows

file_name = image.filename
file_name = file_name.split('.')[0]

custom_config = r'--oem 3 --psm 1'

image_text = pytesseract.image_to_string(image, lang='rus', config=custom_config)

with open(f'{file_name}.txt', 'w') as file:
    file.write(image_text)
