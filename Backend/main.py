import requests
from spotify_token import access

endpoint = "https://api.spotify.com/v1/me"
access_token = access
r = requests.get(endpoint, headers = {"Accept": "application/json",
                                        "Content-Type": "application/json",
                                        "Authorization": "Bearer "})

class QueryEndpoints:
    def __init__(self):
        #self.user_id = user_id
        pass

    def get_resource(self, lookup_id, resource_type='albums', version='v1'):

        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = token_auth.get_resource_header()

        r = requests.get(endpoint, headers=headers)
        return r.json()

    def get_user_id(self, _id):
        return self.get_resource(_id, resource_type='me')

    def get_playlists(self, _id):
        pass #return self.get_resource(_id, resource_type='albums')

    def playlist_info(self):
    #return playlist image, name and number of tracks
        pass

    def get_last_six_months(self, _id):
        #return top artist names

        #return top tracks and the artists of those tracks
        #return self.get_resource(_id, resource_type='artists')
        pass

    def last_six_months(self):
        #return top artist names

        #return top tracks and the artists of those tracks
        pass
    def top_genres_in_playlist(self):
        #return top genres

        #return top 3 most common genres in a users playlist
        pass

#endpoints = QueryEndpoints