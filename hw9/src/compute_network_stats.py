import os,sys
import json
import networkx as nx


def main():
    pathName = os.getcwd()
    input_file = sys.argv[2]
    output_file = sys.argv[4]
    with open(input_file, "r") as file:
        inp=json.load(file)
        G = nx.Graph()
        weight = {}
        for character in inp:
            weight[character]=0
            for character1 in inp[character]:
                weight[character]+=inp[character][character1]
                if not G.has_edge(character, character1):
                    G.add_edge(character,character1,weight=inp[character][character1])
        edge={}
        for v in G.nodes():
            edge[v]=G.degree(v)
        betweenness=nx.betweenness_centrality(G)

        edge = sorted(edge.items(), key=lambda x: x[1], reverse=True)
        edge_list = list({k: v for k, v in edge}.keys())[:3]
        weight=sorted(weight.items(), key=lambda x: x[1], reverse=True)
        weight_list= list({k: v for k, v in weight}.keys())[:3]
        betweenness= sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
        betweenness_list = list({k: v for k, v in betweenness}.keys())[:3]

        result={"most_connected_by_num":edge_list,"most_connected_by_weight":weight_list,"most_central_by_betweenness":betweenness_list}

        directory = os.path.dirname(os.path.join(pathName, output_file))
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(output_file, "w") as file1:
            json.dump(result, file1,indent=4)


if __name__ == "__main__":
    main()