import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder
import AuthedSpotifyObject
spotifyObject = spotipy.Spotify(auth=AuthedSpotifyObject.token)
user = spotifyObject.current_user()

displayName = user['display_name']
userID = user['id']
followers = user['followers']['total']
#print(' '+displayName + '(' + str(followers) + ')')
#export SPOTIPY_REDIRECT_URI='http://google.com/'
#while True:

currentTrack = spotifyObject.current_user_playing_track()

playingType = currentTrack['currently_playing_type'] # track
context = currentTrack['context'] # {external_urls,href,type,uri":}
contextURI = context['uri'] # []

item = currentTrack['item']
itemName = item['name']
itemArtist = item['artists'][0]['name']
itemURI = item['uri']
itemID = item['id']

albumURI = item['album']['uri']
#print(json.dumps(item,sort_keys=True,indent=4))
#isLiked = str(spotifyObject.current_user_saved_tracks_contains([itemID])[0])
isLiked = "True"
#print("isLiked: "+isLiked)
if isLiked is "True":
    #if the song is already liked
   # print("passed: "+itemID)
    ret = albumURI
    #spotifyObject.current_user_saved_tracks_add(tracks=itemID)
else:
    #if the song ain't liked
   # print("failed: "+itemID)
    ret = albumURI
#print("ret: "+str(ret))
#webbrowser.open(ret, new=0, autoraise=False)
print(ret)