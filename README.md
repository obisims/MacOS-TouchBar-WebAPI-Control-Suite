# MacOS TouchBar WebAPI Control Suite
Putting together some stuff using spotipy and mtmr to control spoitify from the macOS touchbar.
<img src="https://t.scdn.co/images/3099b3803ad9496896c43f22fe9be8c4.png" align="right"
     alt="Spotify Dev Logo" width="120">
> <img src="https://developer.spotify.com/assets/branding-guidelines/color1@2x.png" width="25"> I want to control spotify from my touchbar if i feel like.
> <img src="https://developer.spotify.com/assets/branding-guidelines/color1@2x.png" width="25"> I want a simple user experience for quick actions
> <img src="https://developer.spotify.com/assets/branding-guidelines/color1@2x.png" width="25"> I am also very... very bored.

![Spotify from touch bar simulated](reffs/inAction.gif)

## What's even the point?

So last week i smashed the screen of my 2015 macbook Pro (still sour) which led to a replacement which had one of these touch bars that i didn't see much utility in until i saw Better Touch Tools and checked out My Touchbar. My Rules. which got me excited to do something with it and the main thing that i do on my computer, regardless of task, is listen to spotify.

Unfortunately MTMR's custom stuff runs on AppleScript and Spotify doesn't dig that too much, thankfully we can give their WebAPI a reach-around with Python using Spotipy which gives us a more reasonable control to our spotify experience.

Some examples of the difference in access...
||AppleScript|WebAPI||
|---|---|---|---|
|Play/Pause|✓`|✓ |yeah, duh
|Next/Prev Song|✓|✓ |sure
|Song Name|✓|✓|cool
|Artist Name|✓|✓|that's nice
|Like Song|✖|✓|really?
|Playlist/Context Title|✖|✓|bummer
|Follow Counts|✖|✓|lame
|Popularity Stats|✖|✓|dammit
|Listing of Playlists|✖|✓|janet!
|Saving songs to Playlists|✖|✓|bogus.
|Playlist Author|✖|✓|aww

## WTF is going on?
![Spotify from touch bar simulated](reffs/flo_ControlSuiteGen.png)

## Install Notes
Will add to, still need to figure out what the easiest way to move it around is. So far i think it's this?
### Changes to files
#### spotipy filepath
all `API_XXX.scpt` files need the `pythonpath` changed to wherever your spotipy installation directory is.
```applescript
set pythonPath to (the POSIX path of (path to home folder)) & "{path to spotipy-master}"
```
#### spotify API creds
this section of `AuthedSpotifyObjectTemplate.py` needs to be filled out and retitled `AuthedSpotifyObject.py`
```python
CLIENT_ID = "{YOUR CLIENT ID}"
CLIENT_SECRET = "{YOUR CLIENT SECRET}"
username = "{YOUR USERNAME}"
```
#### movingFiles
idk what is needed but here is where i'm putting stuff
`Checkers`&`Actions` folders into `Users/Shared/MTMR`
`Spotipy_TouchBar` folder into `.../spotipy` dir.

### <img src="https://upload.wikimedia.org/wikipedia/commons/9/9b/Font_Awesome_5_brands_spotify.svg" width="15"> <b>That was fun... i'm bored again.</b>


## Details
### Shuffle & Repeat Buttons
![Spotify from touch bar simulated](reffs/flo_ShuffleAndRepeatButtons.png)
### Like ♥︎
![Spotify from touch bar simulated](reffs/flo_like.png)
### Current Artist
![Spotify from touch bar simulated](reffs/flo_currentArtist.png)
### Context Panel (Playlist/Artist)
![Spotify from touch bar simulated](reffs/flo_contextPanel.png)

