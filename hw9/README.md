The file structure is shown below:
```
hw9
├── src
    ├── build_interaction_network.py
    ├── compute_network_stats.py
├── interaction_network.json
├── stats.json
├── other folders
```
This project conduct the fundamentals of network modeling by analyzing the conversation network of the My Little Ponies.\
In this project, the interaction network are modeling as who speaks to who.\
There is an (undirected) edge between two characters that speak to one another. The weight of the edge is how many times they speak to one another.\
To keep our life simple, we’re going to use a very simple proxy for “speaking to one another”. \
We will say that character X speaks to character Y whenever character Y has a line IMMEDIATELY after character X in an episode.

So, for the following excerpt of dialog from an episode...\
Twilight Sparkle: Hey Pinkie. Sorry I accused you of being nosy. \
Pinkie Pie: It’s okay, Twilight – we all have our rough days. \
Applejack: Come on, everypony! We need to get a move-on. \
Spike: Hurray!

In this excerpt, we have the following interactions:\
Twilight Sparkles speaks to Pinkie Pie \
Pinkie Pie speaks to Apple Jack \
Applejack speaks to Spike

The script, build_interaction_network.py, should work as follows
```
python build_interaction_network.py -i /path/to/<script_input.csv> -o /path/to/<interaction_network.json>
```
where the interaction network json file should have structure...
```
      {
            “twilight sparkle”: {
                  “spike”: <# of interactions between twilight sparkle and spike>,
                  “applejack”: <# of interactions between ts and aj>,
                  “pinkie pie”: <# of interactions between ts and pp>,
                  ...
            },
            “pinkie pie”: {
                  “twilight sparkle”: <# of interactions between ts and pp> 
                  ...

            } ...
      }
```
The script compute_network_stats.py which is run as follows:
```
python compute_network_stats.py -i /path/to/<interaction_network.json> -o /path/to/<stats.json>
```
We compute the following by using the networkx library:
- The top three most connected characters by # of edges.
- The top three most connected characters by sum of the weight of edges.
- The top three most central characters by betweenness.

