import spotipy
import spotipy.util as util
from creds import client_id, client_secret
import pprint

username = 'spotify'
scope = 'ugc-image-upload user-read-private user-read-email user-follow-read user-library-read user-top-read user-read-recently-played playlist-read-collaborative playlist-read-private'

token = util.prompt_for_user_token(username,
                           scope,
                           client_id=client_id,
                           client_secret=client_secret,
                           redirect_uri='https://puginarug.com/')
