import pandas as pd
import numpy as np
import plotly.express as px
import scipy.stats as stats
from scipy.signal import savgol_filter
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import glob

SPAN = 150
WINDOW_LENGTH = 51
POLY_ORDER = 8

def calculateAverageEngagementsPerDay(dataframe):
    dataframe['engagement_rate'] = dataframe['like_count'].astype(int) + dataframe['reply_count'].astype(int) + dataframe['retweet_count'].astype(int) + dataframe['quote_count'].astype(int)
    
    engagements_per_day = dataframe.groupby(['created_at']).agg({'engagement_rate':'sum'}).reset_index()
    tweets_per_day = (dataframe.groupby(['created_at'])['tweet'].count()).to_frame('tweets_per_day')
    
    average_engagements_per_day = tweets_per_day.merge(engagements_per_day, how='inner', on='created_at')
    average_engagements_per_day['average_engagement_per_day'] = np.round((average_engagements_per_day['engagement_rate']/ (4 * average_engagements_per_day['tweets_per_day'])), 2)
    
    return average_engagements_per_day

INFLUENCERS_PATH = '../../data/con_sentimientos/influencers/'
MEDIA_PATH = '../../data/con_sentimientos/prensa_escrita/'
TELEVISION_PATH = '../../data/con_sentimientos/television/'

user_info_df = pd.read_csv('../../data/user_info_updated.csv')

leaders_avg_engagements_per_day_df = pd.DataFrame()

# todos los influencers
imprimir = []
imprimir.append("****INFLUENCERS****")
for file in glob.glob(INFLUENCERS_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
   
    username = user_df['username'].unique()[0]
    user_impact = user_info_df[user_info_df['username'] == username]['user_impact_scaled'].unique()[0]
    
    
    # Calculate average engagement per day & it's Exponential Moving Average
    pre_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] < '2019-10-18T00:00:00Z'])
    pre_user_avg_engagements_per_day['EMA']= pre_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    pre_user_avg_engagements_per_day['user'] = username  
    pre_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    pre_user_avg_engagements_per_day['zscore'] = stats.zscore(pre_user_avg_engagements_per_day['EMA'])
    pre_user_avg_engagements_per_day = pre_user_avg_engagements_per_day[(pre_user_avg_engagements_per_day.zscore >= -3) & (pre_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    pre_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(pre_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    pre_user_avg_engagements_per_day['EMA*user_impact'] = pre_user_avg_engagements_per_day['EMA:Degree8'].mul(pre_user_avg_engagements_per_day['user_impact'])
    
    # Calculate average engagement per day & it's Exponential Moving Average
    post_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] > '2019-10-18T00:00:00Z'])
    post_user_avg_engagements_per_day['EMA']= post_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    post_user_avg_engagements_per_day['user'] = username  
    post_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    post_user_avg_engagements_per_day['zscore'] = stats.zscore(post_user_avg_engagements_per_day['EMA'])
    post_user_avg_engagements_per_day = post_user_avg_engagements_per_day[(post_user_avg_engagements_per_day.zscore >= -3) & (post_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    post_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(post_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    post_user_avg_engagements_per_day['EMA*user_impact'] = post_user_avg_engagements_per_day['EMA:Degree8'].mul(post_user_avg_engagements_per_day['user_impact'])
    
    
    imprimir.append(str(username+' pre:' + str(round(pre_user_avg_engagements_per_day['EMA*user_impact'].mean(),3))+ ' post:'+ str(round(post_user_avg_engagements_per_day['EMA*user_impact'].mean(),3) )))

    
    
# todos media y radio
imprimir.append("****PRENSA Y RADIO****")
for file in glob.glob(MEDIA_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
   
    username = user_df['username'].unique()[0]
    user_impact = user_info_df[user_info_df['username'] == username]['user_impact_scaled'].unique()[0]
    
    if username == "Tele13_Radio":
        continue
    
    # Calculate average engagement per day & it's Exponential Moving Average
    pre_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] < '2019-10-18T00:00:00Z'])
    pre_user_avg_engagements_per_day['EMA']= pre_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    pre_user_avg_engagements_per_day['user'] = username  
    pre_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    pre_user_avg_engagements_per_day['zscore'] = stats.zscore(pre_user_avg_engagements_per_day['EMA'])
    pre_user_avg_engagements_per_day = pre_user_avg_engagements_per_day[(pre_user_avg_engagements_per_day.zscore >= -3) & (pre_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    pre_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(pre_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    pre_user_avg_engagements_per_day['EMA*user_impact'] = pre_user_avg_engagements_per_day['EMA:Degree8'].mul(pre_user_avg_engagements_per_day['user_impact'])
    
    # Calculate average engagement per day & it's Exponential Moving Average
    post_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] > '2019-10-18T00:00:00Z'])
    post_user_avg_engagements_per_day['EMA']= post_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    post_user_avg_engagements_per_day['user'] = username  
    post_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    post_user_avg_engagements_per_day['zscore'] = stats.zscore(post_user_avg_engagements_per_day['EMA'])
    post_user_avg_engagements_per_day = post_user_avg_engagements_per_day[(post_user_avg_engagements_per_day.zscore >= -3) & (post_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    post_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(post_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    post_user_avg_engagements_per_day['EMA*user_impact'] = post_user_avg_engagements_per_day['EMA:Degree8'].mul(post_user_avg_engagements_per_day['user_impact'])
    
    
    imprimir.append(str(username+' pre:' + str(round(pre_user_avg_engagements_per_day['EMA*user_impact'].mean(),3))+ ' post:'+ str(round(post_user_avg_engagements_per_day['EMA*user_impact'].mean(),3) )))

# todos television
imprimir.append("****TELEVISION****")
for file in glob.glob(TELEVISION_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
   
    username = user_df['username'].unique()[0]
    user_impact = user_info_df[user_info_df['username'] == username]['user_impact_scaled'].unique()[0]
    if username == "CNNChile":
        continue
    
    # Calculate average engagement per day & it's Exponential Moving Average
    pre_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] < '2019-10-18T00:00:00Z'])
    pre_user_avg_engagements_per_day['EMA']= pre_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    pre_user_avg_engagements_per_day['user'] = username  
    pre_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    pre_user_avg_engagements_per_day['zscore'] = stats.zscore(pre_user_avg_engagements_per_day['EMA'])
    pre_user_avg_engagements_per_day = pre_user_avg_engagements_per_day[(pre_user_avg_engagements_per_day.zscore >= -3) & (pre_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    pre_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(pre_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    pre_user_avg_engagements_per_day['EMA*user_impact'] = pre_user_avg_engagements_per_day['EMA:Degree8'].mul(pre_user_avg_engagements_per_day['user_impact'])
    
    # Calculate average engagement per day & it's Exponential Moving Average
    post_user_avg_engagements_per_day = calculateAverageEngagementsPerDay(user_df[user_df['created_at'] > '2019-10-18T00:00:00Z'])
    post_user_avg_engagements_per_day['EMA']= post_user_avg_engagements_per_day.iloc[:,3].ewm(span=SPAN, adjust=False).mean()
    post_user_avg_engagements_per_day['user'] = username  
    post_user_avg_engagements_per_day['user_impact'] = user_impact
    
    #  Calculate z-score & Remove outliers
    post_user_avg_engagements_per_day['zscore'] = stats.zscore(post_user_avg_engagements_per_day['EMA'])
    post_user_avg_engagements_per_day = post_user_avg_engagements_per_day[(post_user_avg_engagements_per_day.zscore >= -3) & (post_user_avg_engagements_per_day.zscore <= 3)]

    # Curve Smoothing
    post_user_avg_engagements_per_day['EMA:Degree8'] = savgol_filter(post_user_avg_engagements_per_day['EMA'], WINDOW_LENGTH, POLY_ORDER)
    
    # Add user-impact to EMA    
    post_user_avg_engagements_per_day['EMA*user_impact'] = post_user_avg_engagements_per_day['EMA:Degree8'].mul(post_user_avg_engagements_per_day['user_impact'])
    
    
    imprimir.append(str(username+' pre:' + str(round(pre_user_avg_engagements_per_day['EMA*user_impact'].mean(),3))+ ' post:'+ str(round(post_user_avg_engagements_per_day['EMA*user_impact'].mean(),3) )))
    
   
for texto in imprimir:
    print(texto)
    print("*"*50)