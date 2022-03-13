import requests
import datetime
import base64


client_id = 'a0ba4546898d4b79ba7b2eb7aaa3f3a5'
client_secret = '2cde9d2445884dd88f5b04ea5eb30887'

#Defining each step to be able to troubleshoot down de line/ 4 testing and tings

#create a client id:client secret string as the client credentials
#base 64 encode this string                         ## this can be a method
#pass the base 64 encoded client credentials into the authorization token headers
#Get the access token                               ## this can be a method
#use the token to make a request to the spotify enpoints        ## method
#finally check the the authorization actually worked            ## method
    # do this by checking if the expiration of the access token has not expired
    # if the access token has not expired 
    # then it must be a valid request and give me the data I require

        #data needs to be parsed -- seperate issue

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
