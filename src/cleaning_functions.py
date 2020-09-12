import numpy as np
import pandas as pd

def brand_name(row):
    """This function returns the brand name for the product or brand
    being tweeted about
    """
    
    apple_list = ['iPhone', 'iPad or iPhone App',
                  'iPad','Apple',
                  'Other Apple product or service']
    google_list = ['Google', 'Android',
                   'Android App', 'Other Google product or service']
    
    if row in apple_list:
        return 'Apple'
    elif row in google_list:
        return 'Google'
    else:
        return np.nan
    
def emotion_name(row):
    """This function returns the emotion being projected in the tweet
    either: Positive, Negative or Neutral_or_unknown
    """
    
    if row == 'Positive emotion':
        return 'Positive'
    elif row == 'Negative emotion':
        return 'Negative'
    else:
        return 'Neutral_or_unknown'
    
def brand_name_for_missing_brannds(row):
    """This function returns the brand name 
    
    """
    from re import search
    if search(r'Apple|iPad|iPhone', row['tweet_text']):
        return 'Apple'
    elif search(r'android|Google', row['tweet_text']):
        return 'Google'
    else:
        return np.nan