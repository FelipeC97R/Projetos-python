from PyPDF2 import PdfMerger
from os import listdir

merger = PdfMerger()
fileList = listdir()
fileList.sort()

pdfList = list()

for file in fileList:
    if  file[-4:] == '.pdf':
        pdfList.append(file)

for pdf in pdfList:
    merger.append(pdf)

merger.write('MergedFiles.pdf')