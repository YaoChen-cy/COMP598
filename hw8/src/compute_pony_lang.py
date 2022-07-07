import json
import os, sys
import math
import re


def compute_score(json_file,num_words):
    with open(json_file,"r") as file:
        data = json.load(file)
        num_p_use_word={}
        num_pony=len(data)
        for pony in data:
            for word in data[pony]:
                if word in num_p_use_word:
                    num_p_use_word[word]+=1
                else:
                    num_p_use_word[word]=1
        for pony in data:
            for word in data[pony]:
                data[pony][word]=data[pony][word]*math.log(num_pony/num_p_use_word[word])
            data[pony] = sorted(data[pony].items(), key=lambda x: x[1], reverse=True)
            data[pony] = {k: v for k, v in data[pony]}
        result = {}
        for pony in data:
            result[pony] = list(data[pony].keys())[:int(num_words)]
    return result


def main():
    json_file = sys.argv[2]
    num_words= sys.argv[4]
    result=compute_score(json_file,num_words)
    a = json.dumps(result)
    print(re.sub('\{', '{\n     ',re.sub('\],', '],\n    ',re.sub('\]\}', ']\n}', a))))


if __name__ == "__main__":
    main()