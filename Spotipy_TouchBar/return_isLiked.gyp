import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecoder
import AuthedSpotifyObject
spotifyObject = spotipy.Spotify(auth=AuthedSpotifyObject.token)


#print(json.dumps(isplaying,sort_keys=True,indent=4))

while True:
    currentTrack = spotifyObject.current_user_playing_track()
    isPlaying = str(currentTrack['is_playing'])
  #  print(isPlaying)
   # print("isPlaying?  : "+str(str(isPlaying) == "True"))
    if isPlaying == "True":
      #  print("ok, carry on then")

       # print('pass')
        playingType = currentTrack['currently_playing_type'] # track
        #context = currentTrack['context'] # {external_urls,href,type,uri":}
        #contextURI = context['uri'] # []

        item = currentTrack['item']
        itemName = item['name']
        itemArtist = item['artists'][0]['name']
        itemURI = item['uri']
        itemID = item['id']
        #print(json.dumps(currentTrack,sort_keys=True,indent=4))
        #
        #potter = spotifyObject.current_playback()
        #print(json.dumps(potter,sort_keys=True,indent=4))
        #anal = spotifyObject.audio_analysis(itemID)
        #print('playing '+itemName+' by '+itemArtist)
        # analTemp = anal
        #print(json.dumps(analTemp,sort_keys=True,indent=4))
        #print jazz
        

        isLiked = spotifyObject.current_user_saved_tracks_contains([itemID])[0]
        print(isLiked)
        #userTracks = spotifyObject.current_user_saved_tracks()
        #thisTrtack = userTracks['items']
        #print(thisTrtack)
        # Using for loop 
        #for i in thisTrtack: 
        #    print(i['track']['name'])
        #print(json.dumps(thisTrtack,sort_keys=True,indent=4))
        break 
    else:
       # print("sayonara, Robocop")
        #exit()
        break
        #sys.exit("Error message")

#print(json.dumps(VARIABLE,sort_keys=True,indent=4))