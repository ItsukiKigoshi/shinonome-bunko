import pytesseract
import os
from PIL import Image

# Get relative path
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Generalised function to recognise text from image
def recognise_text(img_path, lang, title):
    print(f"{__location__}/images/{img_path}")
    img = Image.open(f"{__location__}/images/{img_path}")
    str = pytesseract.image_to_string(img, lang=lang)
    with open(f"{__location__}/out/{title}.txt", "w") as text_file:
        print(str, file=text_file)
        
recognise_text('python_import_this.png', 'eng', 'str')
recognise_text('amenimo_makezu.jpg', 'jpn', 'str_jp')
recognise_text('discours_de_la_methode.png', 'jpn_vert', 'str_jp_vert')