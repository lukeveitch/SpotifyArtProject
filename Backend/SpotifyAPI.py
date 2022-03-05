import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import pprint

# Personal CID and Secret access from spotify dashboard.
cid = 'a34f732b034c40e3825a5349f686af69'
secret = '4684e50124d9452b9f77c352e0e48333'

#Authentication with the access keys above.
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


def get_the_goods(id): 
    playlist_features_list = ["artist","album","track_name",  "track_id", "danceability","energy","popularity","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"]
    playlist_df = pd.DataFrame(columns = playlist_features_list)

    playlist = sp.user_playlist_tracks('spotify', id)['tracks']['items']
    for trackdict in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = trackdict["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = trackdict["track"]["album"]["name"]
        playlist_features["track_name"] = trackdict["track"]["name"]
        playlist_features["track_id"] = trackdict["track"]["id"]

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)

    return playlist_df


Luke_df = get_the_goods('7tE5HvMmp8bTX9Hypss0Gv?si=a3c9598685614538')

print(Luke_df.head())



#Luke_df.to_csv('Luke_df.csv', index = False)


# 0YJmUjzwx0aXGryEVjPb57?si=913eb69ca9d84a66 - Michal
# 1OiuDYP2nveEaxJkG58bI4?si=d979c68f7c104cdf - Elisa
# 1EKl9t3fjJaEhu6UHKRKUR?si=c51633c7659546d2 - Leonel
# 0DaYW3ckeMH2nVUtFkxBSY?si=c816810a7fb441f0 - Anna
# 1ygNs7ZLOToZSAPCTPMIz7?si=8944576fdae343a9 - Luke

#Get all the metadata
# goods = []
# for index in range(len(playlist_info)):
#     goods.append(playlist_info[index]['track'])

# df = pd.DataFrame(goods)
# print(df.head())
#df.to_csv('AlisaTest.csv')
# dfs = [] #Create a list of dataframes
# for i in range(len(goods)):
#     df = pd.DataFrame(goods[i]['artists']) #Get the artist list and join all dicts together as a dataframe
#     dfs.append(df)

# alldfs = pd.concat(dfs)
# artist_names = list(alldfs['name'])

# print(artist_names)
