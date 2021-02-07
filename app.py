import requests
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
import random

# SPOTIFY API
def GET_AUTHORIZATION():
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
    
    return data



def get_song_info(data):
    # more artists for more diversability
    ids = [
    '4O15NlyKLIASxsJ0PrXPfz',
    '0xOeVMOz2fVg5BJY3N6akT',
    '4Gso3d4CscCijv0lmajZWs',
    '5K4W6rqBFWDnAN6FQUkS6x',
    '4LLpKhyESsyAXpc4laK94U',
    '1Bl6wpkWCQ4KVgnASpvzzA',
    '5he5w2lnU9x7JFhnwcekXX',
    '64KEffDW9EtZ1y2vBYgq8T',
    '7dGJo4pcD2V6oG8kP0tJRR',
    '246dkjvS1zLTtiykXe5h60',
    '6eUKZXaKkcviH0Ku9w2n3V',
    '6qqNVTkY8uBg9cP3Jd7DAH'
    ]
    
    # array to decide which information to show
    rand_info = []
    for i in range(4):
        rand_info.append(random.randint(0,1) )
    song_audio = None
    
    
    # do while, conditions below
    while True:
        # choose artist and grab top tracks from artist
        i = random.randint(0,len(ids) - 1)
        add = requests.get(
            'https://api.spotify.com/v1/artists/{}/top-tracks'.format(ids[i]), 
           headers=data, 
           params = {'market':'ES'} 
        )
        add = add.json()
        
        # sometimes getting errors that 'tracks' is not a good keywork sometimes it happens and sometimes it doesn't
        try:
            track_num = len(add['tracks'])
            rand = random.randint(0, track_num-1)
            
            song_name = add['tracks'][rand]['name'] 
            song_artist = add['tracks'][rand]['artists'][0]['name']
            song_image = add['tracks'][rand]['album']['images'][0]['url']
            song_audio = add['tracks'][rand]['preview_url'] 
        except:
            continue
        
        # do while conditions: if we send audio, keep finding different songs until audio is grabbed
        if rand_info[3] == 0:
            break
        if song_audio != None and rand_info[3] == 1:
            break
        
    return [song_name, song_artist, song_image, song_audio, rand_info]

# FLASK

app = Flask(__name__)

@app.route('/')
def spotify():
    data = GET_AUTHORIZATION()
    info = get_song_info(data)
    
    return render_template(
        "index.html", 
        song_name = info[0],
        song_artist = info[1],
        song_image = info[2],
        song_audio = info[3],
        rand_info = info[4]
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)