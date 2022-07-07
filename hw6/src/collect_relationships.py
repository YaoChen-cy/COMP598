import os,sys
import os.path as osp
import json
import hashlib
import requests
import bs4
def check_name(name1,name2):
    name1 = ''.join(filter(str.isalpha,name1)).lower()
    name2 = ''.join(filter(str.isalpha,name2)).lower()
    return not name1==name2

def find_relationship(CACHE_FILE,person_name):
    rela_list = []
    soup=bs4.BeautifulSoup(open(CACHE_FILE,'r'),'html.parser')
    relation=soup.find('div', attrs={"id": "ff-dating-history-list"})

    if(relation):
        relation1=relation.find_all('h4', attrs={"class": "ff-title"})
        if (relation1):
            for r in relation1:
                if (check_name(person_name, r.string)):
                    r = r.string.replace(' ', '-').lower()
                rela_list.append(r)
    return rela_list

def main():
    with open(sys.argv[2], "r") as file:
        line = json.load(file)
        dict={}
        for people in line["target_people"]:
            hashcontent=hashlib.sha1(people.encode("UTF-8")).hexdigest()
            CACHE_FILE="{}.html".format(hashcontent)
            CACHE_dir=osp.join(line["cache_dir"], CACHE_FILE)
            if not osp.exists(CACHE_dir):
                print(f'Loading webpage for {people}')
                url="https://www.whosdatedwho.com/dating/{}".format(people)
                r = requests.get(url, allow_redirects=True)
                os.makedirs(os.path.dirname(CACHE_dir), exist_ok=True)
                open(CACHE_dir, 'w').write(r.text)
                rela_list=find_relationship(CACHE_dir,people)
                dict[people]=rela_list

            else:
                print(f'Find CACHE_FILE for {people} ')
                rela_list=find_relationship(CACHE_dir,people)
                dict[people]=rela_list
        with open(sys.argv[4], "w") as file1:
            json.dump(dict,file1,indent=4)

if __name__=='__main__':
    main()
