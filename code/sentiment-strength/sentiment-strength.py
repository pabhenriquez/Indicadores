import numpy as np
import pandas as pd
import glob

INFLUENCERS_PATH = '../../data/covid/con_sentimientos/influencers/'
MEDIA_PATH = '../../data/covid/con_sentimientos/prensa_escrita/'
TELEVISION_PATH = '../../data/covid/con_sentimientos/television/'

## PENDIENTE FECHAS PRE Y POST ESTALLIDO

# todos los influencers
print("****INFLUENCERS****")
for file in glob.glob(INFLUENCERS_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]

    #Adaptar fecha a problema evaluando
    totalTweets_pre = user_df[user_df['created_at']< '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_pre = (user_df[user_df['created_at']<'2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_pre.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_pre = overall_sentiments_pre.iloc[overall_sentiments_pre['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
    
    # print(maxSentiment)
    if maxSentiment_pre == 'NEU':
        sentimentStrength_pre = 0.001
    elif maxSentiment_pre == 'POS':
        positiveTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(positiveTweets_pre/totalTweets_pre,3)
    elif maxSentiment_pre == 'NEG':
        negativeTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(-1*(negativeTweets_pre/totalTweets_pre),3)
        
    totalTweets_post = user_df[user_df['created_at']> '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_post = (user_df[user_df['created_at'] > '2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_post.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_post = overall_sentiments_post.iloc[overall_sentiments_post['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
     
     # print(maxSentiment)
    if maxSentiment_post == 'NEU':
        sentimentStrength_post = 0.001
    elif maxSentiment_post == 'POS':
        positiveTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(positiveTweets_post/totalTweets_post,3)
    elif maxSentiment_post == 'NEG': 
        negativeTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(-1*(negativeTweets_post/totalTweets_post),3)   
        
        
        
    print(username, sentimentStrength_pre, sentimentStrength_post)
    print('*'*50)

# todos media y radio
print("****PRENSA Y RADIO****")
for file in glob.glob(MEDIA_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]
    if username == "Tele13_Radio":
        continue
    
    totalTweets_pre = user_df[user_df['created_at']< '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_pre = (user_df[user_df['created_at']< '2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_pre.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_pre = overall_sentiments_pre.iloc[overall_sentiments_pre['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
    
    # print(maxSentiment)
    if maxSentiment_pre == 'NEU':
        sentimentStrength_pre = 0.001
    elif maxSentiment_pre == 'POS':
        positiveTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(positiveTweets_pre/totalTweets_pre,3)
    elif maxSentiment_pre == 'NEG':
        negativeTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(-1*(negativeTweets_pre/totalTweets_pre),3)
        
    totalTweets_post = user_df[user_df['created_at']> '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_post = (user_df[user_df['created_at'] > '2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_post.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_post = overall_sentiments_post.iloc[overall_sentiments_post['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
     
     # print(maxSentiment)
    if maxSentiment_post == 'NEU':
        sentimentStrength_post = 0.001
    elif maxSentiment_post == 'POS':
        positiveTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(positiveTweets_post/totalTweets_post,3)
    elif maxSentiment_post == 'NEG': 
        negativeTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(-1*(negativeTweets_post/totalTweets_post),3)   
        
        
        
    print(username, sentimentStrength_pre, sentimentStrength_post)
    print('*'*50)

# todos television
print("****TELEVISION****")
for file in glob.glob(TELEVISION_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]
    if username == "CNNChile":
        continue
    
    totalTweets_pre = user_df[user_df['created_at']< '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_pre = (user_df[user_df['created_at']< '2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_pre.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_pre = overall_sentiments_pre.iloc[overall_sentiments_pre['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
    
    # print(maxSentiment)
    if maxSentiment_pre == 'NEU':
        sentimentStrength_pre = 0.001
    elif maxSentiment_pre == 'POS':
        positiveTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(positiveTweets_pre/totalTweets_pre,3)
    elif maxSentiment_pre == 'NEG':
        negativeTweets_pre = overall_sentiments_pre[overall_sentiments_pre['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_pre = np.round(-1*(negativeTweets_pre/totalTweets_pre),3)
        
    totalTweets_post = user_df[user_df['created_at']> '2020-03-01T00:00:00Z'].shape[0]   
    overall_sentiments_post = (user_df[user_df['created_at'] > '2020-03-01T00:00:00Z'].groupby(['sentimiento'])['tweet'].count()).to_frame('sentimentTweetCount')
    overall_sentiments_post.reset_index(level=['sentimiento'], inplace=True)
    maxSentiment_post = overall_sentiments_post.iloc[overall_sentiments_post['sentimentTweetCount'].idxmax()][['sentimiento']].values[0]
     
     # print(maxSentiment)
    if maxSentiment_post == 'NEU':
        sentimentStrength_post = 0.001
    elif maxSentiment_post == 'POS':
        positiveTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'POS'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(positiveTweets_post/totalTweets_post,3)
    elif maxSentiment_post == 'NEG': 
        negativeTweets_post = overall_sentiments_post[overall_sentiments_post['sentimiento'] == 'NEG'][['sentimentTweetCount']].values[0][0]
        sentimentStrength_post = np.round(-1*(negativeTweets_post/totalTweets_post),3)   
        
        
        
    print(username, sentimentStrength_pre, sentimentStrength_post)
    print('*'*50)