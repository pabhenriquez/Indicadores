import pandas as pd
import numpy as np
import glob

# Lists as per different subsets
gender = ['male','female','transgender','lgbtq','men','women','girls','boys','fathers','mothers']
genero = ['hombre', 'mujer', 'trans', 'lgbt', 'mujeres', 'hombres', 'padres', 'madres', 'queer', 'homosexual', 'transexual', 'pansexual', 'gay', 'lesbiana']
age = ['children','child','youngsters','adults','elders','youth','parents','grandparents','family','families']
edad = ['niños', 'niño', 'niña', 'jóvenes', 'adultos', 'adultos mayores', 'abuelos', 'abuelas',  'familia', 'familias', 'abuela', 'abuelo']
culturalInferences = ['spanish','indigenious','gaelic','english','scottish','anglo-norman','arabian','islamic','persian','nordic','scandavian','british','french','african','anatolian','ottoman','celtic','pre-roman liberarian','european']
cultura = ['extranjero', 'extranjeros', 'peruano', 'venezolano', 'colombiano', 'haitiano']
ethnicity = ['mesitzo','celts','irish','indian','pakistan','bangladesh','iran','finnish','swedish','sami','roma','scottish','russian','norwegian','norway','native american indian','east asian','turks','neolithic','visigoths','greek','romans','pheonici ans moors','scandinavian','syrian','iraqi','white']
etnia = ['mestizo', 'mapuches', 'mapuche', 'originarios', 'aymara', 'selknam', 'diaguita', 'indígenas']
employmentSectors = ['health care','construction','tourism','manufacturing','agriculture','energy','machinery','textile','electronics','mining','automobile','logging','petroleum','retail']
sectores = ['salud', 'educación', 'construcción', 'minería', 'agricultura', 'energía', 'transporte', 'retail']
# Concat all subsets into one list
allCommunities = list(dict.fromkeys(genero + edad + cultura + etnia + sectores))

# Check for community mentions
INFLUENCERS_PATH = '../../data/incendios_2017/con_sentimientos/influencers/'
MEDIA_PATH = '../../data/incendios_2017/con_sentimientos/prensa_escrita/'
TELEVISION_PATH = '../../data/incendios_2017/television/'

# Todos los influencers
for file in glob.glob(INFLUENCERS_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]
    
    
    totalTweets_pre = user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_pre = 0
    for index, row in user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_pre += 1
                # print(row)

    totalTweets_post = user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_post = 0
    for index, row in user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_post += 1
                # print(row)                

    print(username)                
    print('Community Mentions pre:',communityMentions_pre)
    inclusivityDiversityRatio_pre = np.round(communityMentions_pre/totalTweets_pre, 3)
    print('Inclusivity/Diversity Strength pre:', inclusivityDiversityRatio_pre)
    print('Community Mentions post:',communityMentions_post)
    inclusivityDiversityRatio_post = np.round(communityMentions_post/totalTweets_post, 3)
    print('Inclusivity/Diversity Strength post:', inclusivityDiversityRatio_post)
    print('*'*50)

# Todos los medios y radio
for file in glob.glob(MEDIA_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]
    
    if username == "Tele13_Radio":
        continue
    
    totalTweets_pre = user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_pre = 0
    for index, row in user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_pre += 1
                # print(row)

    totalTweets_post = user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_post = 0
    for index, row in user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_post += 1
                # print(row)                

    print(username)                
    print('Community Mentions pre:',communityMentions_pre)
    inclusivityDiversityRatio_pre = np.round(communityMentions_pre/totalTweets_pre, 3)
    print('Inclusivity/Diversity Strength pre:', inclusivityDiversityRatio_pre)
    print('Community Mentions post:',communityMentions_post)
    inclusivityDiversityRatio_post = np.round(communityMentions_post/totalTweets_post, 3)
    print('Inclusivity/Diversity Strength post:', inclusivityDiversityRatio_post)
    print('*'*50)
    
# Toda la television
for file in glob.glob(TELEVISION_PATH+'/*.csv'):
    user_df = pd.read_csv(file)
    username = user_df['username'].unique()[0]
    
    if username == "CNNChile":
        continue
    
    totalTweets_pre = user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_pre = 0
    for index, row in user_df[user_df['created_at']< '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_pre += 1
                # print(row)

    totalTweets_post = user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].shape[0]
    communityMentions_post = 0
    for index, row in user_df[user_df['created_at'] > '2017-01-01T00:00:00Z'].iterrows():
        for phrase in allCommunities:
            tweet = str(row['tweet'])
            if phrase in tweet:
                communityMentions_post += 1
                # print(row)                

    print(username)                
    print('Community Mentions pre:',communityMentions_pre)
    inclusivityDiversityRatio_pre = np.round(communityMentions_pre/totalTweets_pre, 3)
    print('Inclusivity/Diversity Strength pre:', inclusivityDiversityRatio_pre)
    print('Community Mentions post:',communityMentions_post)
    inclusivityDiversityRatio_post = np.round(communityMentions_post/totalTweets_post, 3)
    print('Inclusivity/Diversity Strength post:', inclusivityDiversityRatio_post)
    print('*'*50)
    
