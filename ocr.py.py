import pytesseract
import cv2
import matplotlib.pyplot as plt 
from PIL import Image
Image = cv2.imread(r"C:\Users\user\Desktop\GRIP\stop.jpg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'
string = pytesseract.image_to_string(Image)
print(string)