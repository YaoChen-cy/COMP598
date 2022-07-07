```
hw7
├── src
    ├── collect_newest.py
    ├── extract_to_tsv.py
    ├── analyze.py
├── concordia.json
├── mcgill.json
├── annotated_concordia.tsv
├── annotated_mcgill.tsv
├── other folders
```
In this project, we are trying to find some insight from in the main topics discussed on the /r/mcgill subreddit vs. the /r/concordia subreddit.\
Task1: Data Collection
The script "collect_newest.py" collects the 100 newest posts in the subreddit specified. It should run as follows:\
python3 collect_newest.py -o <output_file> -s <subreddit>\
Collect two data files, one for mcgill and one for concordia subreddits.

Task2: Prep for coding
The script extract_to_tsv.py accepts one of the files collected from Reddit and outputs a random selection of posts from that file to a tsv (tab separated value) file. It should function like this:\
python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>\
If <num_posts_to_output> is greater than the file length, then the script should just output all lines.\
If there are more than <num_posts_to_output> (which is likely the case), then it should randomly select num_posts_to_output of them and just output those.

Task3: Code Post
The typology are defined into three categories:
- course-related (c)
- food-related (f)
- residence-related (r)
- other (o)

All the posts in annotated_mcgill.tsv and annotated_concordia.tsv are coded.

Task4: Analyze
The script analyze.py outputs the number of each category that appears in annotated files. \
The script should run like this:\
python3 analyze.py -i <coded_file.tsv> [-o <output_file>]
