from auth import token
import spotipy
import pprint

sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_tracks()
spotify_user = sp.current_user()
spotify_user_playlists = sp.current_user_playlists()
top_artists = sp.current_user_top_artists(time_range = "long_term")
top_tracks = sp.current_user_top_tracks(time_range = "long_term")
for count, items in enumerate(top_artists['items']):
    print(count+1, items['name'])
print('-----------')
for count, items in enumerate(top_tracks['items']):
    print(count+1, items['name'])
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




# print(f'---------------------')
# print(f'Hi {name}. Welcome to this art spotify art project.')
# print(f'---------------------')
# print(f'You have {number_of_songs_saved} songs saved')
# print(f'---------------------')
# print(f'You have {number_of_playlists} playlists')
# print(f'---------------------')
# print(f'---------------------')
# print(f'---------------------')

#playlist_info = input('Would you like more information about your playlists? y/n\n>>')

#if playlist_info == 'y':

# playlists_less_than_ten = {}

# for item in spotify_user_playlists['items']:  
        
#     #playlist information
#     playlist_id = item['id']
#     playlist_name = item['name']
#     playlist_owner = item['owner']['display_name']
#     number_of_playlist_tracks = item['tracks']['total']

#     if number_of_playlist_tracks <= 10:
#         playlists_less_than_ten[playlist_name] = playlist_id
    
#     print(f'Playlist id: {playlist_id}\nName: {playlist_name}\nCreated by: {playlist_owner}\nNumber of tracks: {number_of_playlist_tracks}')
#     print('---------------------')

# num = len(playlists_less_than_ten)
# print(f'You have {num} playlists that are less than 10 tracks.')
# print(playlists_less_than_ten)

# elif playlist_info == 'n': 
#     print('Stop being a fat cunt')
# else:
#     pass