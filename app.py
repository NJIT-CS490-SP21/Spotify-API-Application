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

artists = ["Taylor Swift", "Drake","Ariana Grande", "The Weeknd", "Eminem"]
ids = ['06HL4z0CvFAxyc27GXpf02', 
'3TVXtAsR1Inumwj472S9r4',
'66CXWjxzNUsdJxJ2JdwvnR',
'1Xyo4u8uXC1ZmMpatF05PJ',
'7dGJo4pcD2V6oG8kP0tJRR'
]

recent = []
for i in range(5):
    add = requests.get('https://api.spotify.com/v1/artists/{}/top-tracks'.format(ids[i]), headers=data)
    add = add.json()
    recent.append(add)



# FLASK

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Updated printline")
    
    return render_template(
        "index.html", 
        artists = artists,
        artLen = len(artists),
        api = recent
    
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)