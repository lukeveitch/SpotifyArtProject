import requests
import datetime
import base64
import datetime

client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

class SpotifyAPI(object):
    client_id = None
    client_secret = None

    access_token = None
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
        client_credentials_bs4 = self.encode_those_creds_bs4()
        return {
            "Authorization": f"Basic {client_credentials_bs4}" # <base64 encoded client_id:client_secret>
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            return False
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in'] # seconds
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

spotify = SpotifyAPI(client_id, client_secret)
print(spotify.perform_auth())
print(spotify.access_token_did_expire, spotify.access_token_expires)
