import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
import random

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

ids = [
'4O15NlyKLIASxsJ0PrXPfz',
'0xOeVMOz2fVg5BJY3N6akT',
'4Gso3d4CscCijv0lmajZWs',
'5K4W6rqBFWDnAN6FQUkS6x',
'4LLpKhyESsyAXpc4laK94U',
'1Bl6wpkWCQ4KVgnASpvzzA'
]


# FLASK

app = Flask(__name__)

@app.route('/')
def spotify():
    print("Updated printline")
    
    song_audio = None
    while song_audio == None:
        i = random.randint(0,len(ids))
        add = requests.get(
            'https://api.spotify.com/v1/artists/{}/top-tracks'.format(ids[i]), 
           headers=data, 
           params = {'market':'ES'} 
        )
        add = add.json()
        
        
        #track_num = len(add['tracks'])
    
        rand = 0 #random.randint(track_num)
        song_name = add['tracks'][rand]['name'] 
        song_artist = add['tracks'][rand]['artists'][0]['name']
        song_image = add['tracks'][rand]['album']['images'][0]['url']
        song_audio = add['tracks'][rand]['preview_url'] 

    
    return render_template(
        "index.html", 
        song_name = song_name,
        song_artist = song_artist,
        song_image = song_image,
        song_audio = song_audio
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)