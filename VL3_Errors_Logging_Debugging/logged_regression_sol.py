import pandas as pd
import numpy as np
from scipy.stats import linregress
import os
import logging 
logging.basicConfig(filename='logged_regression.log', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

data_file = os.path.join(os.path.dirname(__file__), 
                         'data/women_in_parliament_processed.csv')
df = pd.read_csv(data_file)
timestamps = [int(i) for i in df.index.tolist()]
de_parl = df["Germany"].tolist()

def fit_trendline(year_timestamps, data):
    logging.info("Called fit trendline")
    try: 
        result = linregress(year_timestamps, data)
    except Exception as e:
        logging.error("An exception occurred")
        logging.exception(e)
    else:
        slope = round(result.slope, 3)
        r_squared = round(result.rvalue**2, 3)
        logging.info(f"Completed call to fit trendline, slope is {slope}, r^2 is {r_squared}")
        return slope, r_squared

slope, r_squared = fit_trendline(timestamps, de_parl)