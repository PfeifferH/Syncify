#Author: Hayden Pfeiffer
#Uses Spotipy library created by GitHub user plamere

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-modify'

def authSPTF (username):
    token = util.prompt_for_user_token(username, scope, '4d8051659f54443e9bea64aad8350768', '38ed408d7ff644d1b97c05321a847c82', 'https://www.spotify.com/ca-en/')

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
                #Get rid of title discrepancies
                if '(' in trackName:
                    trackName = trackName.split(' (')[0]
                if ' -' in trackName:
                    trackName = trackName.split(' -')[0]
                trackList.append(trackName + ' - ' + track['artists'][0]['name'].upper())
            offset = offset + LIMIT

        return trackList

    else:
        print("Can't get token for", username)

        return None

#Adds tracks to spotify
def addTracksSPTF (trackList, token):

    if token:

        sp = spotipy.Spotify(auth=token)

        print(sp.current_user_saved_tracks(offset = 0)['items'])
        print(sp.track('2374M0fQpWi3dLnB54qaLX'))
        lst = ['2374M0fQpWi3dLnB54qaLX']
        sp.current_user_saved_tracks_add(lst)

    return None