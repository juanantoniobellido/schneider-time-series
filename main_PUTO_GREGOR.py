#%%
import os
from icecream import ic
import PDFplumber

"""def read_PDF_files_in_data():
    listPDFFiles = os.listdir("data/train6/")
    print (listPDFFiles)

    for PDFFile in listPDFFiles:
        temp = open(PDFFile, 'rb')
        PDF_read = PyPDF2.PdfFileReader(temp)
        first_page = PDF_read.getPage(0)
        ic(first_page.extractText())"""

    


listPDFFiles = os.listdir("data/train6/")
print (listPDFFiles)

with PDFplumber.open("data/train6/pdfs-1.pdf") as temp:
  first_page = temp.pages[0]
  print(first_page.extract_text())


temp = open("data/train6/pdfs-1.pdf", 'rb')
PDF_read = PyPDF2.PdfFileReader(temp)
first_page = PDF_read.getPage(0)
ic(first_page.extractText())
# %%
