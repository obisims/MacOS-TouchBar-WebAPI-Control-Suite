import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder


#print(' '+displayName + '(' + str(followers) + ')')
#export SPOTIPY_REDIRECT_URI='http://google.com/'
#while True:

import AuthedSpotifyObject
spotifyObject = spotipy.Spotify(auth=AuthedSpotifyObject.token)
#userPlaylists = spotifyObject.current_user_playlists()

userPlaylists = spotifyObject.current_user_playlists()
#artist_uri = userPlaylists['uri']
#print(json.dumps(userPlaylists,sort_keys=True,indent=4))
#print(artist_uri)
userPlaylists_limit = userPlaylists['limit']
userPlaylists_offset = userPlaylists['offset']
userPlaylists_total = userPlaylists['total']

userPlaylists_thisPage = userPlaylists['href']
userPlaylists_nextPage = userPlaylists['next']
userPlaylists_prevPage = userPlaylists['previous']

userPlaylists_items = userPlaylists['items']
#print(json.dumps(userPlaylists_items,sort_keys=True,indent=4))
#print(randomChoice_item['name']+" ["+randomChoice_item['uri']+"]")

allPlaylistsArray = []

import math
pages = math.ceil(userPlaylists_total/userPlaylists_limit)-1

allPlaylistsArray += userPlaylists_items


for _ in range(pages):
    thisPage = _+1
    userPlaylists_thisPage = spotifyObject.current_user_playlists(limit=50, offset=userPlaylists_limit*thisPage)['items']
    allPlaylistsArray += userPlaylists_thisPage 
    #print (str(thisPage)+" Some thing")

#print (allPlaylists)

#for __ in range(userPlaylists_total):
#    print(str(__)+" "+allPlaylistsArray[__]['name'])

import random
#print(*userPlaylists_items['name'], sep='\n')
randomChoice_item = random.choice(allPlaylistsArray)
#print(randomChoice_item)
#print()

print(randomChoice_item['uri'])