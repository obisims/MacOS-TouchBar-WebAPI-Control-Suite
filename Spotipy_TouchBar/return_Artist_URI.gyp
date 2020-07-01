import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder

import AuthedSpotifyObject
spotifyObject = spotipy.Spotify(auth=AuthedSpotifyObject.token)
#userPlaylists = spotifyObject.current_user_playlists()

currentTrack = spotifyObject.current_user_playing_track()
artist = currentTrack['item']['artists'][0]
artist_uri = artist['uri']
#print(json.dumps(artist_uri,sort_keys=True,indent=4))
print(artist_uri)