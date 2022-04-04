from flask import jsonify
from auth import token
import spotipy
import pprint

sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_tracks()
spotify_user = sp.current_user()
spotify_user_playlists = sp.current_user_playlists()


## TOP ARTISTS
def topartists():
    terms = ["short_term", "medium_term", "long_term"]
    data = {}
    for term in terms: 
        data[term] = {}

        top_artists = sp.current_user_top_artists(time_range = term)
        # ## TOP ARTISTS
        for count, items in enumerate(top_artists['items']):
             data[term][count+1] = items['name']
    return data

## TOP TRACKS
def toptracks():
    terms = ["short_term", "medium_term", "long_term"]
    data = {}
    for term in terms: 
        data[term] = {}

        top_tracks = sp.current_user_top_tracks(time_range = term)
        # ## TOP ARTISTS
        for count, items in enumerate(top_tracks['items']):
             data[term][count+1] = {}
             data[term][count+1][items['artists'][0]['name']] = items['name']
    return data

## INFORMATION
def user_info():
    ## USER NAME
    name = spotify_user['display_name']
    ## FOLLOWERS
    number_of_followers = spotify_user['followers']['total']
    ## URI
    user_uri = spotify_user['uri']
    ## NUMBER OF SONGS SAVED
    number_of_songs_saved = results['total']
    ## NUMBER OF PLAYLISTS
    number_of_playlists = spotify_user_playlists['total']

    return {'name': name, 
            'number_of_followers': number_of_followers,
            'uri': user_uri,
            'songs_saved': number_of_songs_saved,
            'playlists': number_of_playlists
            }

def all_playlist_data_dump():
    return spotify_user_playlists

def playlists():
    ## PLAYLISTS
    playlists_less_than_ten = {}
    lst = []
    all_playlists = {}

    for item in spotify_user_playlists['items']:  
        playlist = {}
        #playlist information
        playlist['playlist_id'] = item['id']
        playlist['playlist_name'] = item['name']
        playlist['created_by'] = item['owner']['display_name']
        playlist['playlist_image'] = item['images']
        playlist['number_of_playlist_tracks'] = item['tracks']['total']

        if playlist['number_of_playlist_tracks'] <= 10:
            playlists_less_than_ten[item['name']] = item['id']

        ## PLAYLIST IMAGE
        for el in  item['images']:
            for key, value in el.items():
                if key =='url':
                    playlist[key] = value

        lst.append(playlist)

    all_playlists['items'] = lst
    return all_playlists, playlists_less_than_ten

pprint.pprint(playlists())

