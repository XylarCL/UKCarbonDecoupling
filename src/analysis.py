import pandas as pd
import numpy as np
#from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt

# Visual Normality Test
def  visual_normality_test(df, x, countries, start_year, end_year):
    for i in countries:
            plt.hist(df[df["country"] == i][x], histtype="bar")
            plt.ylabel(x)
            print(df[df["country"]==i].min())
            #plt.axis([start_year, end_year, df[df["country"]==i][x].min(), df[df["country"]==i][x].max()])
            plt.title("Histogram " + i)
            plt.show()

