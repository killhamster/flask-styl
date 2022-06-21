import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_recommendations(search):

    #Init
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    #Search: return JSON of the first result
    result = sp.search(q = search, type = 'track', limit = 1)

    #Get ID of the track. Need a list for the recommendation lookup
    id_list = [result['tracks']['items'][0]['id']]

    recs = sp.recommendations(seed_tracks = id_list, limit = 10)

    if recs['tracks'] == False:
        return None
    else:
        return recs

def get_covers(recommendations):
    #Init
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

    id_list = [track['id'] for track in recommendations['tracks']]

    if not id_list:
        return None
    else:
        tracks = sp.tracks(id_list)
        cover_links = [image['album']['images'][2]['url'] for image in tracks['tracks']]
        return cover_links

def display(recommendations, covers):
    html_display = ''
    if len(recommendations['tracks']) != 0:
        for idx, track in enumerate(recommendations['tracks']):

            html_display += f'''
                <div class = 'row recommendation'>
                    <div class = 'col-md-2'>
                        <img src = "{covers[idx]}">
                    </div>
                    <div class = 'col-md-6 info'>
                        <p>{track['name']} by {track['artists'][0]['name']}</p>
                    </div>
                    <div class = 'col-md-4'>
                        <a href = "{track['external_urls']['spotify']}" target = '_blank'><button class = 'button'>Play It</button></a>
                    </div>
                </div>
            '''            
    else:
        html_display += f'''
                <div class = 'row recommendation'>
                    <div class = 'col-md-8 info'>
                        <p>Bummer! Spotify doesn't know enough about this track or artist!</p>
                    </div>
                </div>
            '''            
    return html_display