import pandas as pd
import json
import os, sys


def main():
    if (len(sys.argv)>3 and sys.argv[3] == "-o"):
        tsv_file = sys.argv[2]
        output_file = sys.argv[4]
        directory = os.path.dirname(output_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
        df=pd.read_csv(tsv_file, sep='\t', header=0)
        output = {"course-related": int((df.coding == 'c').sum()), "food-related": int((df.coding == 'f').sum()),
                  "residence-related": int((df.coding == 'r').sum()), "other": int((df.coding == 'o').sum())}
        with open(output_file, "w") as file:
            json.dump(output,file,indent=0)
    else:
        tsv_file = sys.argv[2]
        df = pd.read_csv(tsv_file, sep='\t', header=0)
        output={"course-related":(df.coding=='c').sum(),"food-related":(df.coding=='f').sum(),"residence-related":(df.coding=='r').sum(),"other":(df.coding=='o').sum()}
        print(output)


if __name__ == '__main__':
    main()
