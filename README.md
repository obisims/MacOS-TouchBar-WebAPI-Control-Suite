# MacOS TouchBar WebAPI Control Suite
Putting together some stuff using spotipy and mtmr to control spoitify from the macOS touchbar.

![Alt text](https://developer.spotify.com/assets/branding-guidelines/color1@2x.png)


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
```mermaid
graph TD

TB0((MTMR<br>Settings)) --> ck1{Checker}
subgraph ToolBar Display
ck1---|Loop ever n seconds|ck1
ck1 --> as1{AppleScript}

as1 --> sp1>Spotipy]
sp1>Spotipy] --> w1>WebApi]
end
as1 --> TB1
w1>WebApi] --> TB1((TouchBar<br>Display))

TB((TouchBar<br>Display))---|Touch Interaction|as2{AppleScript}
subgraph ToolBar Action
as2 --> sp2>Spotipy]
sp2>Spotipy] --> w2>WebApi]
as2 --> si
w2>WebApi] --> si[Spotify Interaction]
end
```
### Shuffle & Repeat Buttons
```mermaid
graph TD
chkPl{Spotify}
chkPl ---|if playing|ck
chkPl ---|if playing|ck2

subgraph ShuffleOn Display
    ck{Shuffle<br>IsOn}
    TBH((Hide<br> Icon))
    ck---|if false|TBH
end
ck---|if true|TB1
TB1((Shuffle On<br> Icon))
TB1---|Touch Interaction|as1

subgraph ShuffleOn Action
    as1[Toggle Shuffle]
end
as1 --> si

subgraph ShuffleOff Display

TBH2((Hide<br> Icon))
ck2{Shuffle<br>IsOff}

ck2---|if false|TBH2
end

ck2---|if true|TB3
TB3((Shuffle Off<br> Icon))
TB3---|Touch Interaction|as2

subgraph ShuffleOff Action
    as2[Toggle_Shuffle]
end

as2 --> si2
si[Spotify Interaction]
si2[Spotify Interaction]
```

### Like ♥︎
```mermaid
graph TD

chkPl{Spotify} ---|if playing|ck
subgraph Like Display
ck{Check if<br>Liked}-->py1>grab current track]
py1-->py2
py2>Is Track Liked?]



py2---|if true|heartOn((Full Heart<br> Icon))
py2---|if false|heartOff((Empty Heart<br> Icon))

end

heartOn --> heart
heartOff --> heart
heart---|Long-Touch Interaction|as2
heart---|Tap-Touch Interaction|as1

subgraph Like Action
as1[Toggle Liked] --> ts>action_Toggle_Like]
ts ---|if not liked|f0>like song]
ts ---|if liked|f1>unlike song]
end
subgraph OpenAlbum Action
as2[open Album]-->py3>get Current<br>Playing Album]
end
py3-->fin[Open Album<br>in Spotify]
```

### Current Artist
```mermaid
graph TD
chkPl{Spotify} ---|if playing|ck
subgraph Artist Display
ck{Grab Current<br>Artist}

ck---|trunacate if long|display((Artist Name))
end


display---|Long-Touch Interaction|longInteraction
display---|Tap-Touch Interaction|tapInteraction

subgraph Launch Or Play Or Next Action
tapInteraction[Launch or Play or Skip]
a_as2[Launch]
a_as3[Play]
a_as4[Skip]

tapInteraction ---|if off|a_as2
tapInteraction ---|if on and<br>not playing|a_as3
tapInteraction ---|if on and<br>playing|a_as4
end
a_as2-->a_as3
a_as3-->si
a_as4-->si

si[spotify interaction]


subgraph Open Artist Action
longInteraction[open Artist]-->py3>get Current<br>Playing Artist]
end
py3-->fin[Open Artist<br>in Spotify]
```

### Context Panel (Playlist/Artist)
```mermaid
graph TD
chkPl
chkPl{Spotify} ---|if playing|ck
subgraph Artist Display
    ck{Generate<br>Context Panel}
    ck-->context
    context>grab Context]
    context---|if no context|noContext_string
    context---|if artist|artst_v1
    context---|if playlist|plst_v1

    subgraph No Context
        noContext_string[blank]
    end
    
    subgraph Artist Context
        artst_v1>popularity]
        artst_v2>followers]
        artist_string_final>rotatingGenre]
        
        artst_v1---|if >1|artst_v2
        artst_v2---|if >1|artist_string_final
    end

    subgraph Playlist Context
        plst_v1>popularity]
        plst_v2>followers]
        plst_string_final>rotatingGenre]
        
        plst_v1---|if >1|plst_v2
        plst_v2---|if >1|plst_string_final
    end
    
    artist_string_final-->string
    noContext_string-->string
    plst_string_final-->string
end



string[return string]
string---|trunacate if long|display
display((Context String))

display---|Long-Touch Interaction|longInteraction
display---|Tap-Touch Interaction|tapInteraction

tapInteraction-->shortInteration
longInteraction-->longInteration

subgraph Play Random Playlist
    shortInteration[Short Interaction]
    rand_v1>Get All of<br>User's Playlists]
    rand_v2>Select Random URI]
    
    shortInteration-->rand_v1
    rand_v1-->rand_v2
end
rand_v2-->rand_v3
rand_v3[Play Playlist]

subgraph Open Context/Playlist
    longInteration[Long Interaction]
    con_v1>Get Current<br>Context URI]
    longInteration-->con_v1
end
con_v2[Open Context<br>Page]
con_v1-->con_v2

```

## Notes
Will add to.
### Changes to files
#### spotipy filepath
all `API_XXX.scpt` files need the `pythonpath` changed to wherever your spotipy installation directory is.
```applescript
set pythonPath to (the POSIX path of (path to home folder)) & "{path to spotipy-master}"
```
#### spotify API creds
