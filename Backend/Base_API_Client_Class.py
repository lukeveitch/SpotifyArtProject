import requests
import datetime
import base64


client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

class SpotifyAPI(object):
    client_id = None
    client_secret = None

    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    token_url = "https://accounts.spotify.com/api/token"



    def __init__(self, client_id, client_secret, *args, **kwargs): # always going to need the client id and secret.#
        super().__init__(*args, **kwargs)
        self.client_id = client_id 
        self.cliend_secret = client_secret

    def encode_those_creds_bs4(self):
        client_id = self.client_id
        client_secret = self.client_secret
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())

        return client_creds_b64.decode()

    def get_token_headers(self):
        return {
            "Authorization": f"Basic {self.encode_those_creds_bs4}" # <base64 encoded client_id:client_secret>
        }

    def get_token_data(self):
        return {
        "grant_type": "client_credentials"
        }

    def perform_request(self):
        ########## Making a request
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)

        ########## Valid request + extract the data
        if valid_request:
            token_response_data = r.json()
            now = datetime.datetime.now()
            access_token = token_response_data['access_token']
            expires_in = token_response_data['expires_in'] # seconds
            expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now
        