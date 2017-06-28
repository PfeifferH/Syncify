#Author: Hayden Pfeiffer
#Uses Spotipy library created by GitHub user plamere

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'


def getTracksSPTF (username):

    token = util.prompt_for_user_token(username, scope, '4d8051659f54443e9bea64aad8350768', '38ed408d7ff644d1b97c05321a847c82', 'https://www.spotify.com/ca-en/')

    if token:
        sp = spotipy.Spotify(auth=token)

        #List to store tracks
        trackList = []

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
                trackList.append(track['name'] + ' - ' + track['artists'][0]['name'])
            offset = offset + LIMIT

        return trackList

    else:
        print("Can't get token for", username)

        return None

