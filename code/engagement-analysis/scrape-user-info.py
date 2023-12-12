import pandas as pd
import tweepy
import math
import datetime
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, minmax_scale
import plotly.express as px

bearer_token = "AAAAAAAAAAAAAAAAAAAAAOsdogEAAAAA%2BMtlseMuguvcM34Femu6urbtK%2FE%3DXIaOptkcJcY2cBGCUHRidzdUiDpfCEmM1PfyBwRtbE4c4RNnqr"
client = tweepy.Client(bearer_token=bearer_token)




usernames = [    "PolarBearby", "Izkia", "Pa__tty", "FrancoBassoSotz", "El_Ciudadano", "Vitalicio7020", "RockandRolec", "UPLaRadio", "FelipeParadaM", "csantander23", "reddeemergencia", "INFORMADORCHILE", "CEBioBio", "bomberoschillan", "PiensaPrensa", "alegriagonzaa", "MauricioAmpuero", "ablanch4", "S_Schwartzmann", "InfoNuble", "MrRangerR1", "CapuchaCreativa", "JackoProu", "SpreenDMC", "camilaemiliasv", "Chileno17039890", "rsumen", "perzzzz90","ayala_rodolfo","Cachoescalona1"]

user_info = client.get_users(usernames=usernames, user_fields=['created_at','public_metrics','description','location','verified'])

user_info_df = pd.DataFrame(columns=['created_at','name','username','followers_count','following_count','tweet_count','listed_count','description','location','verified'])

for user in user_info.data:    
    user_info_df = user_info_df.append({'created_at':user.created_at, 'name':user.name, 'username':user.username, 'followers_count':user.public_metrics.get('followers_count'),
                                        'following_count': user.public_metrics.get('following_count'), 'tweet_count':user.public_metrics.get('tweet_count'), 
                                        'listed_count':user.public_metrics.get('listed_count'), 'description':user.description, 'location':user.location, 'verified':user.verified}, 
                                       ignore_index=True)

user_info_df.to_csv('../../data/user_info2.csv', index=False)