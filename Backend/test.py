from auth import token
import spotipy
import pprint as pp
import pandas as pd

sp = spotipy.Spotify(auth=token)
playlist = sp.user_playlist_tracks('spotify', '0sUfaZFPAzgj7XGTYhXqk8?si=iYAVSiWJQAeOX-p9Gkp_bw')


playlist_name = playlist['name'] # Name of the playlist - need to return at the end
playlist_info = playlist['tracks']['items']

#Get all the metadata
goods = []
for index in range(len(playlist_info)):
    goods.append(playlist_info[index]['track'])

dfs = [] #Create a list of dataframes
for i in range(len(goods)):
    df = pd.DataFrame(goods[i]['artists']) #Get the artist list and join all dicts together as a dataframe
    dfs.append(df)

alldfs = pd.concat(dfs)
artist_names = list(alldfs['name'])
print(artist_names)