import sys
import spotipy
import spotipy.util as util
from creds import client_id, client_secret
import pprint

# endpoint = 'https://accounts.spotify.com/authorize?' +


username = 'spotify'
scope = 'user-library-read'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri='https://puginarug.com/')


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    spotify_user = sp.current_user()
    spotify_user_playlists = sp.current_user_playlists()
    
    # time_range = ['short_term', 'medium_term', 'long_term']
    # for period in time_range:
    #     print(period)
    #     pprint.pprint(sp.current_user_top_tracks(time_range = period))
    #time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term
    # current_user_top_artists
    # playlist
    # playlist_cover_image
    # playlist_tracks
    # playlist_tracks



    #User information variables
    name = spotify_user['display_name']
    number_of_followers = spotify_user['followers']['total']
    user_uri = spotify_user['uri']
    number_of_songs_saved = results['total']
    number_of_playlists = spotify_user_playlists['total']



    
    print(f'---------------------')
    print(f'Hi {name}. Welcome to this art spotify art project.')
    print(f'---------------------')
    print(f'You have {number_of_songs_saved} songs saved')
    print(f'---------------------')
    print(f'You have {number_of_playlists} playlists')
    print(f'---------------------')
    print(f'You have {number_of_playlists} playlists')
    print(f'---------------------')
    print(f'You have {number_of_playlists} playlists')
    print(f'---------------------')

    for item in spotify_user_playlists['items']:  

        #playlist information
        playlist_id = item['id']
        playlist_name = item['name']
        playlist_owner = item['owner']['display_name']
        number_of_playlist_tracks = item['tracks']['total']

        
        print(f'Playlist id: {playlist_id}\nName: {playlist_name}\nCreated by: {playlist_owner}\nNumber of tracks: {number_of_playlist_tracks}')
        print('---------------------')


#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)

