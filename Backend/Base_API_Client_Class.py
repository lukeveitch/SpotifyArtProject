import requests
import datetime
import base64


client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

class SpotifyAPI(object):
    access_token = None
    