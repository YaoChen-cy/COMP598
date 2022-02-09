import json
import os, sys
def cal_avg(file):
    i = 0
    n = 0
    for post in file:
        post=json.loads(post)
        n=n+len(post['data']['title'])
        i=i+1
    avg_title_len=n/i
    print("The average post title length is",round(avg_title_len,2))

def main():
    with open(sys.argv[1], 'r') as file:
        cal_avg(file)

if __name__=='__main__':
    main()
