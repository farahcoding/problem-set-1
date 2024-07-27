'''
Pull down the imbd_movies dataset here and save to /data as imdb_movies_2000to2022.prolific.json
You will run this project from main.py, so need to set things up accordingly
'''

import json
import analysis_network_centrality
import analysis_similar_actors_genre

import requests
import os

# Ingest and save the imbd_movies dataset

url = 'https://raw.githubusercontent.com/cbuntain/umd.inst414/main/data/imdb_movies_2000to2022.prolific.json'
movies = '../data/imdb_movies_2000to2022.prolific.txt'

""""checking if the movies file already exist and delete it"""
if os.path.isfile(movies):
    os.remove(movies)

"""sending request to the website and output the content of response to """
with open(movies, 'a') as f:
    print( requests.get(url).text.strip() , file=f)

# Call functions / instanciate objects from the two analysis .py files
def main():
    analysis_network_centrality.runCentralityFunction(movies)
    #analysis_similar_actors_genre.runSimilarityFunction(movies)



if __name__ == "__main__":
    main()