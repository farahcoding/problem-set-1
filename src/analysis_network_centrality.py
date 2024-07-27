'''
PART 1: NETWORK CENTRALITY METRICS

Using the imbd_movies dataset
- Guild a graph and perform some rudimentary graph analysis, extracting centrality metrics from it. 
- Below is some basic code scaffolding that you will need to add to. 
- Tailor this code scaffolding and its stucture to however works to answer the problem
- Make sure the code is line with the standards we're using in this class 
'''

import numpy as np
import pandas as pd
import networkx as nx

import json
from datetime import date,datetime

# Build the graph
g = nx.Graph()

# Set up your dataframe(s) -> the df that's output to a CSV should include at least the columns 'left_actor_name', '<->', 'right_actor_name'

def runCentralityFunction(m):
    with open(m,'r') as in_file:
        # Don't forget to comment your code
        for line in in_file:
            #print(line)
            # Don't forget to include docstrings for all functions

            # Load the movie from this line
            this_movie = json.loads(line)
                
            # Create a node for every actor
            for actor_id,actor_name in this_movie['actors']:
            # add the actor to the graph
                g.add_node(actor_id, name=actor_name)

            # Iterate through the list of actors, generating all pairs
            ## Starting with the first actor in the list, generate pairs with all subsequent actors
            ## then continue to second actor in the list and repeat
            i = 0 #counter
            for left_actor_id, left_actor_name in this_movie['actors']:
                for right_actor_id, right_actor_name in this_movie['actors'][i+1:]:
                    # Get the current weight, if it exists
                    #todo
                    
                    # Add an edge for these actors
                    g.add_edge(left_actor_id, right_actor_id)
                    
                i += 1 

    # Print the info below
    print("Nodes:", len(g.nodes))

    #Print the 10 the most central nodes
    """computing the degree centrality for nodes"""
    centrality = nx.degree_centrality(g)

    """creating a dataframe to hold the data about top 10 nodes"""
    nodesdata=[]

    """sorting nodes based on their centrality degree and print the first 10"""
    for n in sorted(centrality, key=centrality.get, reverse=True)[:10]:
        print(n, g.nodes[n]['name'], centrality[n])
        nodesdata.append ([n, g.nodes[n]['name'], centrality[n]])

    # Output the final dataframe to a CSV named 'network_centrality_{current_datetime}.csv' to `/data`
    """"getting current datetime"""
    dateandtime = str(datetime.now().isoformat(timespec='seconds')).replace('T','_').replace(':','')
    outputfile = f'../data/network_centrality_{dateandtime}.csv'

    """sending the output o a csv file """
    df = pd.DataFrame(nodesdata, columns=['actor_id', 'actor_name', 'centrality'])
    #print(df)
    df.to_csv(outputfile, sep=',', index=False)


