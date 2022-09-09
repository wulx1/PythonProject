# -*- coding:utf-8 -*-
import os
from docx2pdf import convert
path = ("/Users/wulongxing/Desktop")
files = []
for file in os.listdir(path):
    if file.endswith(".doc"):
        files.append(path + file)

print(files)

for file in files:
    convert(file,file+'.pdf')
    print(file + "转换成功")
# convert("/Users/wulongxing/Desktop/lily(1).docx","/Users/wulongxing/Desktop/lily.pdf")
# from pdf2docx import Converter
# pdf_file = 'C:\\Users\\wuchenwei\\Desktop\\xlt\\xlt.pdf'
# docx_file = 'C:\\Users\\wuchenwei\\Desktop\\xlt\\xlt.docx'
# cv = Converter(pdf_file)
# cv.convert(docx_file, start=0, end=None)
# cv.close()
