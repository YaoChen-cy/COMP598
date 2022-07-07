import pandas as pd
import urllib.request
import json
import os, sys

def remove_punc(line):
    punc = '''()[]],-.?!:;#&'''
    for ele in line:
        if ele in punc:
            line=line.replace(ele, " ")
    return line


def remove_nonalpha(line):
    return ' '.join([i for i in line.split() if i.isalpha()])

def remove_stopword(inp_line):
    print(inp_line)
    stopword_list = []
    for line in urllib.request.urlopen(
            "https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt"):
        word = str(line.decode('utf-8')).rstrip('\n').lower()
        if (not "#" in word):
            stopword_list.append(word)
    for word in stopword_list:
        for ele in line.split():
            if(ele==word):
                inp_line=inp_line.replace(ele,"")
    print(inp_line)
    return inp_line

def create_dict(csv_file):
    df = pd.read_csv(csv_file)
    ponys = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]
    result = {}
    sum_dic = {}
    for pony in ponys:
        pony_tbl = df[df['pony'].str.fullmatch(pony, case=False)]
        stopword_list = []
        for line in urllib.request.urlopen(
                "https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt"):
            word = str(line.decode('utf-8')).rstrip('\n').lower()
            if (not "#" in word):
                stopword_list.append(word)
        dic = {}
        for line in pony_tbl["dialog"]:
            line = str(line).lower()
            line = remove_punc(line)
            line = remove_nonalpha(line)
            for ele in line.split():
                if (not ele in stopword_list):
                    if ele not in dic:
                        dic[ele] = 1;
                    else:
                        dic[ele] = dic[ele] + 1;
                    if ele not in sum_dic:
                        sum_dic[ele] = 1;
                    else:
                        sum_dic[ele] = sum_dic[ele] + 1;
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        dic = {k: v for k, v in dic}
        result[pony] = dic

    for pony in list(result):
        for word in list(result[pony]):
            if (result[pony][word] < 5) and (sum_dic[word] < 5):
                del result[pony][word]
    return result


def main():
    output_file = sys.argv[2]
    csv_file = sys.argv[4]
    result=create_dict(csv_file)

    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(output_file,"w") as file:
        json.dump(result,file,indent=4)


if __name__ == "__main__":
    main()