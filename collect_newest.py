import requests
import json
import os, sys


def collect_post(output_file,subreddit,headers):
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(output_file,"w") as file:
        url="https://oauth.reddit.com{}/new.json".format(subreddit)
        r=requests.get(url,headers=headers,params={'limit':'100'})
        root_element=r.json()['data']['children']
        i=1
        for line in root_element:
            if(i==100):
                json.dump(line, file)
                break
            else:
                json.dump(line,file)
                file.write('\n')
            i=i+1


def main():
    output_file=sys.argv[2]
    subreddit=sys.argv[4]
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
    #headers={'User-Agent': 'myapp/0.0.1', 'Authorization': 'bearer 1264617591283-o-uTRjqmDbfxo5e3y5iclgcLCNarjQ'}
    collect_post(output_file,subreddit,headers)

if __name__=='__main__':
    main()
