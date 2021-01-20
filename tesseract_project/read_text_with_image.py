import cv2
import pytesseract

img = cv2.imread('/Users/dmitry/Downloads/how-to-overlay-text-on-images-5-simple-methods-1-638.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config))



