#%%
# Importar librerías de programación
import os

import pandas as pd

dfAux = pd.DataFrame()

for file in os.listdir("data/"):
    if file.endswith(".csv"):
        try:
            df = pd.read_csv("data/" + file)
        except:
            df = pd.read_csv("data/" + file, sep=";")
        pd.concat([dfAux, df], ignore_index=True)



# %%
# Import from API

import os

files = os.listdir("data/")
for file in os.listdir("data/"):
    if file.endswith(".csv"):
        try:
            df = pd.read_csv("data/" + file)
        except:
            df = pd.read_csv("data/" + file, sep=";")
        pd.concat([dfAux, df], ignore_index=True)