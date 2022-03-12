import requests
import datetime
import base64


client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())


token_url = "https://accounts.spotify.com/api/token"


method = "POST"

token_data = {
    "grant_type": "client_credentials"
}
token_headers = {
    "Authorization": f"Basic {client_creds_b64.decode()}" # <base64 encoded client_id:client_secret>
}


r = requests.post(token_url, data=token_data, headers=token_headers)
valid_request = r.status_code in range(200, 299)

print(r.json())
if valid_request:
    token_response_data = r.json()
    now = datetime.datetime.now()
    access_token = token_response_data['access_token']
    expires_in = token_response_data['expires_in'] # seconds
    expires = now + datetime.timedelta(seconds=expires_in)
    did_expire = expires < now