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


# GET SONG INFORMATION
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
    
   
    # choose artist and grab top tracks from artist
    i = random.randint(0,len(ids) - 1)
    add = requests.get(
        'https://api.spotify.com/v1/artists/{}/top-tracks'.format(ids[i]), 
       headers=data, 
       params = {'market':'ES'} 
    )
    add = add.json()
   
    # do while, conditions below
    while True:
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
        
        break
        
    return [song_name, song_artist, song_image, song_audio]

def get_lyric_url(song_name):
    search_url = 'https://api.genius.com/search'
    
    load_dotenv(find_dotenv())
    genius_access_token = os.getenv('genius-access-token')
    # print("\n\n\n\nToken:",genius_access_token, "\n\n\n\n")
    headers = {
        'Authorization': 'Bearer {}'.format(genius_access_token)
    }
    
    data={'q': song_name }
    genius_dict = requests.get(search_url, headers=headers, data=data)
    genius_dict = genius_dict.json()
    
    for hit in genius_dict['response']['hits']:
        if 'lyrics' in hit['result']['url']:
            return hit['result']['url']

    # grab first hit if there are not lyrics
    return genius_dict['response']['hits'][0]['result']['url']

# FLASK
app = Flask(__name__)

@app.route('/')
def spotify():
    data = GET_AUTHORIZATION()
    info = get_song_info(data)
    lyric_url = get_lyric_url(info[0]) # song_name = info[0]
    
    print("LRYICS HTMLS:", lyric_url)
    return render_template(
        "index.html", 
        song_name = info[0],
        song_artist = info[1],
        song_image = info[2],
        song_audio = info[3],
        lyric_url = lyric_url
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)