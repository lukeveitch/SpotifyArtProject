import requests
import pprint

CLIENT_ID = 'a34f732b034c40e3825a5349f686af69'
CLIENT_SECRET = '4684e50124d9452b9f77c352e0e48333'
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
playlist_id = '5seDwcnO3NmUxV5EXAeezb?si=9f89e3f0dc874ed1'

# actual GET request with proper header
r = requests.get(BASE_URL + 'me/playlists', headers=headers)

r = r.json()
pprint.pprint(r)
