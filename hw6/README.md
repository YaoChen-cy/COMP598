This mini project conduct API Data Collection.\
The Task 1 is to assess the average length of a Reddit post title.\
Since collect ALL Reddit posts is unpractical, two different ways of sampling posts to assess their length are considered:
- Sample 1: Collect the 1000 newest posts from the 10 most popular subreddits by subscribers: 
  funny, AskReddit, gaming, aww, pics, Music, science, worldnews, videos, todayilearned. 
  (collect 100 posts from each subreddits.)
- Sample 2: Collect the 1000 newest posts from the 10 most popular subreddits by # of posts by day: 
  AskReddit, memes, politics, nfl, nba, wallstreetbets, teenagers, PublicFreakout, leagueoflegends, unpopularopinion. 
  (collect 100 posts from each subreddits.)
The script collect.py collecting the data for BOTH of the sampling approaches. It should store the data in files sample1.json and sample2.json, respectively.\
The script compute_title_lengths.py accept an input file containing one JSON dict per line (corresponding to a subreddit post) and output the average post title length.\
The script is called like: python3 compute_title_lengths.py <input_file>.\

The Task 2 is to scraping data from website.\
The script collect_relationships.py that collects the relationships for a set of celebrities provided in a JSON configuration file as follows:
python3 collect_relationships.py -c <config-file.json> -o <output_file.json>
