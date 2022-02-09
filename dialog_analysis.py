import pandas as pd
import sys
import json

#read dialog data
dialog = pd.read_csv(sys.argv[3])
##dialog = pd.read_csv('../data/clean_dialog.csv')

#count the number of speech acts that each character
num_ts=len(dialog[dialog['pony'].str.fullmatch('twilight sparkle',case=False)])
num_aj=len(dialog[dialog['pony'].str.fullmatch('applejack',case=False)])
num_rr=len(dialog[dialog['pony'].str.fullmatch('rarity',case=False)])
num_pp=len(dialog[dialog['pony'].str.fullmatch('pinkie pie',case=False)])
num_rd=len(dialog[dialog['pony'].str.fullmatch('rainbow dash',case=False)])
num_fl=len(dialog[dialog['pony'].str.fullmatch('fluttershy',case=False)])

#get total number of speech in this dataset
tot=len(dialog.index)

#get fraction of dialogue for these 6 pony with 2 decimals
ts_v=round(num_ts/tot,2)
aj_v=round(num_aj/tot,2)
rr_v=round(num_rr/tot,2)
pp_v=round(num_pp/tot,2)
rd_v=round(num_rd/tot,2)
fl_v=round(num_fl/tot,2)

#write number of speech for these 6 pony by dataframe
count_sum_T=pd.DataFrame({'twilight sparkle':[num_ts],'applejack':[num_aj],'rarity':[num_rr],
                        'pinkie pie':[num_pp],'rainbow dash':[num_rd],'fluttershy':[num_fl]})

#transpost the dataframe
count_sum=count_sum_T.T

#add a colomun for the fraction of dialogue for each pony
count_sum.insert(1,'verbosity',[ts_v, aj_v, rr_v, pp_v, rd_v, fl_v], True)

#add the col name for the dataframe
count_sum.columns = ['count', 'verbosity']

#transfer the result to json format
result=count_sum.to_json()
parsed = json.loads(result)
parsed = json.dumps(parsed,indent=1)

#write the final result to json file
with open(sys.argv[2], 'w') as outfile:
##with open('../output.json', 'w') as outfile:
    outfile.write(parsed)
