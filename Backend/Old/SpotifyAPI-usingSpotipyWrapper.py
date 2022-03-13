import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import pprint

# Personal CID and Secret access from spotify dashboard.
cid = ''
secret = ''

#Authentication with the access keys above.
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


def get_the_goods(id): 
    playlist_features_list = ["artist","album","track_name",  "track_id", "popularity","danceability","energy","key","loudness","mode", "speechiness","instrumentalness","liveness","valence","tempo", "duration_ms","time_signature"] #"bpm"
    playlist_df = pd.DataFrame(columns = playlist_features_list)
    
    playlist = sp.user_playlist_tracks('spotify', id)['tracks']['items']
    #playlistkeys = sp.user_playlist_tracks('spotify', id)['tracks']['items'][0]['track']

    for trackdict in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = trackdict["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = trackdict["track"]["album"]["name"]
        playlist_features["track_name"] = trackdict["track"]["name"]
        playlist_features["track_id"] = trackdict["track"]["id"]
        playlist_features["popularity"] = trackdict["track"]["popularity"]

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[5:]:
            playlist_features[feature] = audio_features[feature]
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)

    return playlist_df


# df = get_the_goods('0sUfaZFPAzgj7XGTYhXqk8?si=2ffc266403894d42')

df2 = get_the_goods('5seDwcnO3NmUxV5EXAeezb?si=9f89e3f0dc874ed1')
avgDancibility = df2["danceability"].mean()
avgEnergy = df2["energy"].mean()
avgPopularity = df2["popularity"].mean()
avgBPM = df2["tempo"].mean()

print(avgDancibility, avgEnergy, avgPopularity, avgBPM)
