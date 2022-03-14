# from SpotifyToken import token
# import requests


# # class SpotifyUser:
# #     user_id_endpoint = 'https://api.spotify.com/v1/me'

# #     def _init__(self, client_id, client_secret):
# #         self.client_secret = client_secret
# #         self.client_id = client_id

# #     def get_header(self):
# #         return {
# #             "Content-Type": "application/json",
# #             "Authorization": f"Bearer {token}"
# #         }


# def get_user_id():

#     r = requests.get('https://api.spotify.com/v1/me', 
#                                 headers = {
#                                     "Content-Type": "application/json",
#                                     "Authorization": f"Bearer {token}"
#                                 })
#     return r.json()
# print(get_user_id())

###Request User Authorization
    #Get request to https://accounts.spotify.com/authorize endpoint
    #client_id
    #response_type
    #redirect_uri
    #state
    #scope
    #show_dialog = True