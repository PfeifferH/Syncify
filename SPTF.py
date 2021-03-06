#Author: Hayden Pfeiffer
#Uses Spotipy library created by GitHub user plamere

import sys
import spotipy
import spotipy.util as util
from Support import trackFormat

scope = 'user-library-modify'

def authSPTF (username):

    print("Spotify username: " + username)
    token = util.prompt_for_user_token(username, scope, '4d8051659f54443e9bea64aad8350768', '38ed408d7ff644d1b97c05321a847c82', 'https://www.spotify.com/ca-en/')
    print(token)
    return token

def getTracksSPTF (token):

    if token:
        sp = spotipy.Spotify(auth=token)

        #List to store tracks
        trackList = []

        #Formatted track name
        trackName = ''

        #Limit default is 20
        LIMIT = 20
        thisNum = 20
        offset = 0
        while thisNum == LIMIT:
            thisNum = 0
            results = sp.current_user_saved_tracks(offset=offset)
            for item in results['items']:
                track = item['track']
                thisNum+=1
                trackName = track['name'].upper()
                artistName = track['artists'][0]['name'].upper()

                #Use Support.py to format track
                trackList.append(trackFormat(trackName, artistName))
            offset = offset + LIMIT

        return trackList

    else:
        print("Can't get token")

        return None

#Adds tracks to spotify
def addTracksSPTF (trackList, token):


    if token:

        sp = spotipy.Spotify(auth=token)

        #List of track ids to add to spotify
        idList = []

        #Search for song using list input
        for i in range(len(trackList)):
            results = sp.search(q = trackList[i], type = 'track')
            items = results['tracks']['items']
            idList.append(items[0]['id'])

        #Add the list of tracks
        if(len(idList) > 0):
            sp.current_user_saved_tracks_add(idList)

        else:
            print("All Spotify tracks are already added")

    else:
        print("Can't get token")


    return None