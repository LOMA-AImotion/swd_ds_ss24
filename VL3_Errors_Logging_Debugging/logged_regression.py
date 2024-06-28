import pandas as pd
import numpy as np
from scipy.stats import linregress
import os

data_file = os.path.join(os.path.dirname(__file__), 
                         'data/women_in_parliament_processed.csv')
df = pd.read_csv(data_file)
timestamps = [int(i) for i in df.index.tolist()]
de_parl = df["Germany"].tolist()

def fit_trendline(year_timestamps, data):
    result = linregress(year_timestamps, data)
    slope = round(result.slope, 3)
    r_squared = round(result.rvalue**2, 3)
    return slope, r_squared

slope, r_squared = fit_trendline(timestamps, de_parl)