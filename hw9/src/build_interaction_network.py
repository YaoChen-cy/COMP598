import pandas as pd
import os, sys
import json


def generate_freq_char(df):
    pony_dict = {}
    df["pony"] = df["pony"].str.lower()
    a = df[~df["pony"].str.contains(r'(?:\s|^)others(?:\s|$)')]
    a = a[~a["pony"].str.contains(r'(?:\s|^)ponies(?:\s|$)')]
    a = a[~a["pony"].str.contains(r'(?:\s|^)and(?:\s|$)')]
    a = a[~a["pony"].str.contains(r'(?:\s|^)all(?:\s|$)')]
    b = a.groupby('pony').size().sort_values(ascending=False).head(101).to_frame().reset_index()
    freq_101 = b["pony"]
    for i in freq_101:
        pony_dict[i] = {}
    return pony_dict


def count_interaction(df,pony_dict):
    df1 = df[['title', 'pony']]
    i = 1
    for character in df1['pony']:
        if i == 1:
            prev_char = character
            pass
        if prev_char in pony_dict:
            if (character in pony_dict) and (prev_char != character) and (df1.iloc[i - 2, 0] == df1.iloc[i - 1, 0]):
                if prev_char in pony_dict[character]:
                    pony_dict[character][prev_char] += 1
                else:
                    pony_dict[character][prev_char] = 1
                if character in pony_dict[prev_char]:
                    pony_dict[prev_char][character] += 1
                else:
                    pony_dict[prev_char][character] = 1
                prev_char = character
            else:
                prev_char = character
        else:
            prev_char = character
        i = i + 1

    for char in pony_dict:
        temp = sorted(pony_dict[char].items(), key=lambda x: x[1], reverse=True)
        temp = {k: v for k, v in temp}
        pony_dict[char] = temp
    return pony_dict


def main():
    pathName = os.getcwd()
    input_file = sys.argv[2]
    output_file = sys.argv[4]
    df = pd.read_csv(input_file)
    pony_dict=generate_freq_char(df)
    result_pony_dict=count_interaction(df,pony_dict)

    directory = os.path.dirname(os.path.join(pathName,output_file))
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(output_file, "w") as file:
        json.dump(result_pony_dict,file,indent=4)


if __name__ == "__main__":
    main()