import numpy as np
import pandas as pd

def brand_name(row):
    if row in apple_list:
        return 'Apple'
    elif row in google_list:
        return 'Google'
    else:
        return np.nan
    
def emotion_name(row):
    if row == 'Positive emotion':
        return 'Positive'
    elif row == 'Negative emotion':
        return 'Negative'
    else:
        return 'Neutral_or_unknown'
    
