import plotly.figure_factory as pff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
dis_plot = pff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
dis_plot.show()