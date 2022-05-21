# Importar librerías de programación
import os

import pandas as pd
from PyPDF2 import PDFFileReader


def read_csv_files_in_data():
    # variables auxiliar
    dfAux = pd.DataFrame()
    for file in os.listdir("data/"):
        if file.endswith(".csv"):
            try:
                df = pd.read_csv("data/" + file)
            except:
                df = pd.read_csv("data/" + file, sep=";")
            pd.concat([dfAux, df], ignore_index=True)











def read_PDF_files_in_data():
    listPDFFiles = os.listdir("data/train6/")
    print (listPDFFiles)

    for PDFFile in listPDFFiles:
        temp = open(PDFFile, 'rb')
        PDF_read = PDFFileReader(temp)
        first_page = PDF_read.getPage(0)
        print(first_page.extractText())

    









if "__name__" == "__main__":
    read_csv_files_in_data()
