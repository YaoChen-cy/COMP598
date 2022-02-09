import requests
import json
import os, sys
import os.path as osp
def collect_sample1(inp_subred_list,headers):
    sample1="../sample1.json"
    with open(sample1,"w") as file:
        for subred in inp_subred_list:
            url="https://oauth.reddit.com/r/{}/new.json".format(subred)
            r=requests.get(url,headers=headers,params={'limit':'100'})
            root_element=r.json()['data']['children']
            i=1
            for line in root_element:
                if(i>100):
                    break
                else:
                    json.dump(line,file)
                    file.write('\n')
                i=i+1

def collect_sample2(inp_subred_list,headers):
    sample2 = "../sample2.json"
    with open(sample2, "w") as file2:
        for subred in inp_subred_list:
            url = "https://oauth.reddit.com/r/{}/new.json".format(subred)
            r = requests.get(url, headers=headers,params={'limit':'100'})
            root_element = r.json()['data']['children']
            i = 1
            for line in root_element:
                if (i > 100):
                    break
                else:
                    json.dump(line, file2)
                    file2.write('\n')
                i = i + 1
                
def main():
    
    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth('rIMTsNcyM5NJpa-Rk_s4jQ', '7yImCfqha_GrSZH_q4RRVjFm1BOzRg')

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password','username': 'pxxxzq','password': 'chenyao2018'}

    headers = {'User-Agent': 'myapp/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value

    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    #headers={'User-Agent': 'myapp/0.0.1', 'Authorization': 'bearer 1264617591283-HOUUDXVTAiMGGY2uJpI_UjoxPXjy_g'}
    subred_by_subscrib=['funny', 'AskReddit', 'gaming', 'aww', 'pics', 'Music', 'science', 'worldnews', 'videos', 'todayilearned']
    subred_by_post = ['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends', 'unpopularopinion']
    collect_sample1(subred_by_subscrib,headers)
    collect_sample2(subred_by_post, headers)

if __name__=='__main__':
    main()
