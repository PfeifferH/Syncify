from gmusicapi import Mobileclient

def authGPM(email, password):
    api = Mobileclient()
    logged_in = api.login(email, password, '352bb0c3576e547d')
    # logged_in is True if login was successful

    return api


def getTracksGPM (api):



    #Get unformatted tracks list
    tracksDictionary = Mobileclient.get_all_songs(api,False,None)

    tracksList = []


    for i in range(len(tracksDictionary)):

        song = tracksDictionary[i] ['title']
        song = song.upper()
        if '(' in song:
            song = song.split(' (')[0]

        artist = tracksDictionary[i] ['artist']
        artist = artist.upper()

        tracksList.append(song + ' - ' + artist)

    return tracksList


def addTracksGPM (trackList, api):


    idList = []

    for i in range(len(trackList)):
        tracks = Mobileclient.search(api, trackList[i], 50)['song_hits'][0]['track']
        idList.append(tracks['storeId'])

    if(len(idList > 0)):
        Mobileclient.add_store_tracks(api, idList)

    else:
        print("All Google Play Music tracks are already added")
    return None