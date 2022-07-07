import pandas as pd
#import numpy as np

#data collection step
tweets = pd.read_csv('IRAhandle_tweets_1.csv',nrows=10000)
tweets_eng=tweets.loc[tweets['language'] == 'English']
temp=tweets_eng['content']
tweets_noQ=tweets_eng[tweets_eng['content'].str.contains('?', regex=False)==False]
tweets_noQ.to_csv('data_collect.tsv', sep = '\t',index=False)

#data annotation
tweets_AC = open("data_collect.tsv")
tweets_TA=pd.read_csv(tweets_AC, delimiter="\t")
tweets_TA['trump_mention']=(tweets_TA['content'].str.replace('[^a-zA-Z0-9]',' ',regex=True).str.center(len(tweets_TA['content']), " ")).str.contains(" Trump ")

dataset=pd.DataFrame({'tweet_id':tweets_TA['tweet_id'],'publish_date':tweets_TA['publish_date'],'content':tweets_TA['content'],'trump_mention':tweets_TA['trump_mention']})
dataset.to_csv('dataset.tsv',sep = '\t',index=False,header=["tweet_id","publish_date","content","trump_mention"])

#analysis
tweets_data= open("dataset.tsv")
data=pd.read_csv(tweets_data, delimiter="\t")
T=data['trump_mention'].values.sum()
F=(~data['trump_mention']).values.sum()
result=pd.DataFrame({'result':["frac-trump-mentions"],'value':[round(T/(T+F),3)]})
result.to_csv('results.tsv',sep = '\t',header=["result","value"],index=False)

