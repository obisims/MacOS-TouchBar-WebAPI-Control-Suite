
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder

CLIENT_ID = "{YOUR CLIENT ID}"
CLIENT_SECRET = "{YOUR CLIENT SECRET}"
username = "{YOUR USERNAME}"
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