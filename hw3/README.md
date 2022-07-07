The bash shell script stats.sh accepts as a command line argument a tweet file and prints out, on subsequent lines:
- The number of lines in the file.
- The first line of the file (i.e., the header row).
- The number of lines in the last 10,000 rows of the file that contain the string “potus” (case-insensitive).
- Of rows 100 – 200 (inclusive), how many of them that contain the word “fake”.

The script work on any file which has at least 10,000 lines in it. An error message will be printed if the input file is smaller than 10,000 lines.

The python script dialog_analysis.py computes and produces a JSON-formatted result where the JSON file has two keys:
- "count" shows the number of speech acts that each character has in the entire file. 
- "verbosity" gives fraction of dialogue, measured in # of speech acts produced by this pony. 
- For both cases, the values related to the six ponies are shown(the main characters of the cartoon). 
