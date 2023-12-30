import cv2
import time

import psycopg2
from openpyxl import load_workbook
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def remove(string): 
    return "".join(string.split()) 


img = cv2.imread('t.jpg',0)
edges = cv2.Canny(img,100,150)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()


alphanum=pytesseract.image_to_string(edges)
no=str(alphanum)
n = remove(no)
print("Number is: ",n)

conn = psycopg2.connect(database = "ocrdb", user = "postgres", password = "root", host = "localhost", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute("INSERT INTO ocrtable (characters) VALUES ('{%s}')" % (n))
conn.commit()
print("Records created successfully")
conn.close()