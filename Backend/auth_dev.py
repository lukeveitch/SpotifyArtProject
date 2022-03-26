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

#print(token)
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    spotify_user = sp.current_user()
    name = spotify_user['display_name']
    number_of_followers = spotify_user['followers']['total']
    user_uri = spotify_user['uri']
    number_of_songs_saved = results['total']



    print(f'---------------------')
    print(f'Hi {name}. Welcome to this art spotify art project.')
    print(f'---------------------')
    print(f'You have {number_of_songs_saved} songs saved')
    print(f'---------------------')
    print(f'---------------------')
    print(f'---------------------')
    print(f'---------------------')

    


#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)

