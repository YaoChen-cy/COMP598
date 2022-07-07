import pandas as pd
import random
import json
import os, sys


def select_post(output_file,json_file,num_posts_to_output):
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(json_file, "r") as file:
        lines=file.readlines()
        count=len(lines)
        name_list = []
        title_list = []
        if(int(num_posts_to_output) >= count):
            for post in lines:
                post= json.loads(post)
                name_list+=[post["data"]["name"]]
                title_list+=[post["data"]["title"]]
        else:
            posts = random.sample(lines,int(num_posts_to_output))
            for post in posts:
                post=json.loads(post)
                name_list += [post["data"]["name"]]
                title_list += [post["data"]["title"]]
        df=pd.DataFrame({"Name":name_list,"title":title_list})
        df["coding"]=""
        df.to_csv(output_file, sep='\t', index=False)


def main():
    output_file=sys.argv[2]
    json_file=sys.argv[3]
    num_posts_to_output=sys.argv[4]
    select_post(output_file,json_file,num_posts_to_output)


if __name__=='__main__':
    main()