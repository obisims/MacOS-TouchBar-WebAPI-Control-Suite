import os
import sys
import json
import spotipy
import webbrowser
import random
import spotipy.util as util
from json.decoder import JSONDecoder

import AuthedSpotifyObject
spotifyObject = spotipy.Spotify(auth=AuthedSpotifyObject.token)

#print(' '+displayName + '(' + str(followers) + ')')
#export SPOTIPY_REDIRECT_URI='http://google.com/'
#while True:
currentTrack = spotifyObject.current_playback()

#print(json.dumps(currentTrack,sort_keys=True,indent=4))
#playingType = currentTrack['currently_playing_type'] # track

context = currentTrack['context'] # {external_urls,href,type,uri":}
#print("context=null: "+str((context == 'null')))
#print(currentTrack)
while True:
   # print(isPlaying)
    #print(isPlaying)
    #print("isPlaying?  : "+str(str(isPlaying) == "True"))
    #print(context)
    #print('test2')
    #print('pass?: '+str(str(context) == ('None' or 'Null' or 'nul')))
    if str(context) == ('None' or 'Null' or 'nul'):
        #thisDumper = "nnuull"
       # print(json.dumps(thisDumper,sort_keys=True,indent=4))
        #print('🔊 Radio')
        print('')
        break
    else:
    #print('test3')
        if context['type'] == "artist":
        #  print('test4')
            context_uri = context['uri']
            context_type= context['type']
            isPlaying = str(currentTrack['is_playing'])
            thisArtist = spotifyObject.artist(context_uri)

            thisGenre = thisArtist['genres'] #['','']
            #thisName = thisArtist['name'] #['','']
            # .join() with sets
            comma = ', '
            #print()
            popularity = thisArtist['popularity']
            followers = thisArtist['followers']['total']
            #print(thisGenre)
            #print(json.dumps(thisArtist,sort_keys=True,indent=4))
            if thisGenre == []:
                
                randomGenre = ""
                if followers ==0:
                    print("☆ "+str('{:,}'.format(popularity)))
                else:
                    print("⚐ "+str('{:,}'.format(followers))+" ☆ "+str('{:,}'.format(popularity)))
            else:
                randomGenre = str(random.choice(thisGenre))
                if followers ==0:
                    thisDumper = "🎭 "+ randomGenre+" ☆ "+str('{:,}'.format(popularity))
                    #comma.join(thisGenre)
                    print(thisDumper)   
                else:
                    thisDumper = "🎭 "+ randomGenre+" ⚐ "+str('{:,}'.format(followers))+" ☆ "+str('{:,}'.format(popularity))
                    #comma.join(thisGenre)
                    print(thisDumper)
            break
        if context['type'] == "playlist":
        # print('test')
            context_uri = context['uri']
            #href
            context_type= context['type']
            isPlaying = str(currentTrack['is_playing'])
            thisPlaylist = spotifyObject.playlist(context_uri)

            #print(json.dumps(thisPlaylist,sort_keys=True,indent=4))

            #thisGenre = thisPlaylist['genres'] #['','']
            thisName = thisPlaylist['name'] #['','']
            followers = thisPlaylist['followers']['total']
            owner = thisPlaylist['owner']['display_name']
            
            import re
            r = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)", re.I)
                
            if len(owner.split()) > 1:
                #more then 1
                owner_r = owner.split(' ', 1)[0]
            else:
                owner_r = owner
            if len(thisName.split()) > 1:
                #more then 1
                #thisName_r = (''.join(r.findall(thisName)))
                #thisName_r = thisName
                thisName_r = (thisName[:25] + '..') if len(thisName) > 25 else thisName
            else:
                thisName_r = thisName
            if followers <= 1:
                if (owner_r == "Spotify" or owner_r == "Obi"):
                    thisDumper = "☰  "+thisName_r
                else:
                    thisDumper = "☰  "+thisName_r+" by "+owner_r
            else:
                if owner_r == "Spotify":
                    #print(owner_r)
                    thisDumper = "☰  "+thisName_r+" "+" ⚐ "+str('{:,}'.format(followers))
                else:
                    if owner_r == "Obi":
                        thisDumper = "☰  "+thisName_r+""+" ⚐ "+str('{:,}'.format(followers))+" ( /^ω^)/♪♪"
                    else:
                        thisDumper = "☰  "+thisName_r+" by "+owner_r+" ⚐ "+str('{:,}'.format(followers))
            print(thisDumper)
            #print(thisPlaylist)
            break
        else:
            break
    break

#print(json.dumps(VARIABLE,sort_keys=True,indent=4))
