from numpy import number
from auth import token
import spotipy
import pprint

sp = spotipy.Spotify(auth=token)


results = sp.current_user_saved_tracks()
spotify_user = sp.current_user()
spotify_user_playlists = sp.current_user_playlists()


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
    # print('-----------')


# # ## TOP TRACKS
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

pprint.pprint(user_info())

# # print(f'---------------------')
# # print(f'Hi {name}. Welcome to this art spotify art project.')
# # print(f'---------------------')
# # print(f'You have {number_of_songs_saved} songs saved')
# # print(f'---------------------')
# # print(f'You have {number_of_playlists} playlists')
# # print(f'---------------------')
# # print(f'---------------------')
# # print(f'---------------------')

# #playlist_info = input('Would you like more information about your playlists? y/n\n>>')

# # if playlist_info == 'y':

# playlists_less_than_ten = {}
# playlists = {}

# for item in spotify_user_playlists['items']:  
#     # pprint.pprint(item)

#     #playlist information
#     playlist_id = item['id']
#     playlist_name = item['name']
#     playlist_owner = item['owner']['display_name']
#     playlist_image = item['images']
#     number_of_playlist_tracks = item['tracks']['total']

#     if number_of_playlist_tracks <= 10:
#         playlists_less_than_ten[playlist_name] = playlist_id

#     ## PLAYLIST ID, NAME, OWNER, NUMBER OF TRACKS
#     print(f'Playlist id: {playlist_id}\nName: {playlist_name}\nCreated by: {playlist_owner}\nNumber of tracks: {number_of_playlist_tracks}')

#     ## PLAYLIST IMAGE
#     for el in playlist_image:
#         for key, value in el.items():
#             if key =='url':
#                 print(key, value)
#     print('---------------------')


# ## DICTIONARY OF ALL THE PLAYLISTS WITH LESS THAN 10 TRACKS
# num = len(playlists_less_than_ten)
# print(f'You have {num} playlists that are less than 10 tracks.')
# print(playlists_less_than_ten)

# elif playlist_info == 'n': 
#     print('Stop being a fat cunt')
# else:
#     pass
# playlist_cover_image
# playlist_tracks