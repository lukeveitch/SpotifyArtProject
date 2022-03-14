import requests
import datetime
import base64
import datetime
# from secrets import client_id, client_secret

client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

class SpotifyAPI(object):
    client_id = None
    client_secret = None

    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs): # always need the client id and secret.#
        self.client_id = client_id 
        self.client_secret = client_secret

    def encode_those_creds_bs4(self):
        client_id = self.client_id
        client_secret = self.client_secret
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())

        return client_creds_b64.decode()

###Request Access Token
    def get_token_headers(self):
        return {
            "Authorization": f"Basic {self.encode_those_creds_bs4()}" # <base64 encoded client_id:client_secret>
        }

    def get_token_data(self):
        return {
        "grant_type": "client_credentials"
        }

    def perform_request(self):

        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()

        ### Make the request
        r = requests.post(token_url, data=token_data, headers=token_headers)
        data = r.json()
        if not r.status_code in range(200,299):
            print(f"Error with the request\nRequest status code: {r.status_code}")

        access_token = data['access_token']
        now = self.access_token_expires
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)

        #update the access token expires time and change did expire to false
        self.access_token_expires = expires
        self.access_token_did_expire = expires <= now # if expires is greater than (which it should be) it will change the variable to false
        self.access_token = access_token 
        # if self.access_token_did_expire:
        #     print(f"The access HaduToken expires at {self.access_token_expires}")
        return "Authentication successful"
 

spotify = SpotifyAPI(client_id, client_secret)
token = spotify.access_token
print(token)
print(spotify.access_token_expires)
print(spotify.access_token_did_expire)
