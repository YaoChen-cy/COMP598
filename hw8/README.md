The file structure is shown below:
```
hw8
├── src
    ├── compile_word_counts.py
    ├── compute_pony_lang.py
├── test
    ├── test_tasks.py
├── word_counts.json
├── other folders
```
This project computs each pony’s most frequent words using TF-IDF. \
The script compile_word_counts.py computes word counts for each pony from all episodes of MLP. \
*only 6 ponies are considered: "twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy".\
It should run as follows:
```
python compile_word_counts.py -o <word_counts_json> -d <clean_dialog.csv file>
```
The script compute_pony_lang.py compute the <num_words> for each pony that has the highest TF-IDF score. \
It is run as follows:
```
python compute_pony_lang.py -c <pony_counts.json> -n <num_words>
```
The test file test_tasks.py contains two unit tasks. One test for task 1, one for task 2. \
For the first task, the unit test pickup a mini script file and produce counts that are checked against a JSON file containing ground truth counts.\
For the second task, the unit test pickup the ground truth counts and compute TF-IDF scores that are checked against a JSON file containing ground truth TF-IDF scores.\
