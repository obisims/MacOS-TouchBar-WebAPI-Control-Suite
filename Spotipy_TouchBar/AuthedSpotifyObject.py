
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder

CLIENT_ID = "f53677e9fa5742ceac61a266dc6596a9"
CLIENT_SECRET = "854a9cae8b434760943b25adab311139"
username = "12121388895"
SPOTIPY_REDIRECT_URI='http://google.com/'
#spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
scope = 'playlist-read-private playlist-modify-public user-library-modify user-library-read user-read-currently-playing user-read-playback-state'

try:
    token = util.prompt_for_user_token(
        username,
        scope,
        CLIENT_ID,
        CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI)
except:
    os.remove(".cache-"+username+"")
    token = util.prompt_for_user_token(
        username,
        scope,
        CLIENT_ID,
        CLIENT_SECRET,
        SPOTIPY_REDIRECT_URI)