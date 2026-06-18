import pandas as pd
import numpy as np
from scipy.stats import shapiro, pearsonr, spearmanr
import matplotlib.pyplot as plt

# Visual Normality Test
def  visual_normality_test(df, x, countries):
    for i in countries:
            plt.hist(df[df["country"] == i][x], histtype="bar")
            plt.ylabel(x)
            #plt.axis([start_year, end_year, df[df["country"]==i][x].min(), df[df["country"]==i][x].max()])
            plt.title("Histogram " + i)
            #plt.show()

def statistical_normality_test(df, x, countries):
    for i in countries:
        stat, p = shapiro(df[df["country"] == i][x])
        print("Statistics=%.3f, p=%.3f" % (stat, p))
        if p > 0.05:
            print(x + " for " + i + " looks gausian (accept H0)")
        else:
            print(x + " for " + i + " looks non-gausian (reject H0)")