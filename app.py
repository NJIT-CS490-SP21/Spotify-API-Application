import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

# SPOTIFY API
load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('client-id')
CLIENT_SECRET = os.getenv('client-secret')

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
#print(access_token)

data = {'Authorization': 'Bearer {token}'.format(token=access_token)}

recent = requests.get('https://api.spotify.com/v1/browse/new-releases', headers=data)
recent = recent.json()
#print(recent)


artists = ["Taylor Swift", "Drake","Ariana Grande", "The Weeknd", "Eminem"]

# FLASK

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Updated printline")
    
    return render_template(
        "index.html", 
        artists = artists,
        artLen = len(artists)
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)