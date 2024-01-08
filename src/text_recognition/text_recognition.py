import pytesseract
import os
from PIL import Image

# Get relative path
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Recognise text from python_import_this.png
str_img = Image.open(os.path.join(__location__,'images/python_import_this.png'))
str = pytesseract.image_to_string(str_img, lang="eng")
print(str)

# Recognise text from amenimo_makezu.jpg
str_jp_img = Image.open(os.path.join(__location__,'images/amenimo_makezu.jpg'))
str_jp = pytesseract.image_to_string(str_jp_img, lang="jpn")
print(str_jp)

# Recognise text from discours_de_la_methode.png
str_jp_vert_img = Image.open(os.path.join(__location__,'images/discours_de_la_methode.png'))
str_jp_vert = pytesseract.image_to_string(str_jp_vert_img, lang="jpn_vert")
print(str_jp_vert)