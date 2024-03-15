"""GitHub Classroom autograding script."""

import os

import pandas as pd

from country_scientific_prodcution import main

main()

#
# Retorna error si la carpeta output/ no existe
if not os.path.exists("countries.csv"):
    raise FileNotFoundError("File 'countries.csv' not found")

#
# Lee el contenido del archivo output.txt
dataframe = pd.read_csv("countries.csv")
dataframe = dataframe.set_index("countries")

assert dataframe["count"]["United States of America"] == 579
assert dataframe["count"]["China"] == 273
assert dataframe["count"]["India"] == 174
assert dataframe["count"]["United Kingdom"] == 173
assert dataframe["count"]["Italy"] == 112

if not os.path.exists("map.html"):
    raise FileNotFoundError("File 'map.html' not found")
