from gmusicapi import Mobileclient, Webclient
from Support import trackFormat


def authGPM(email, password):

    #Log in to GPM
    print("Email: " + email + " Password: " + password)
    api = Mobileclient()
    logged_in = api.login(email, password, '352bb0c3576e547d')
    # logged_in is True if login was successful

    print(logged_in)

    return api


def getTracksGPM (api):



    #Get unformatted tracks list
    tracksDictionary = Mobileclient.get_all_songs(api,False,None)

    tracksList = []


    for i in range(len(tracksDictionary)):

        trackName = tracksDictionary[i] ['title'].upper()
        artistName = tracksDictionary[i] ['artist'].upper()

        tracksList.append(trackFormat(trackName, artistName))

    return tracksList

#Adds tracks to Google Play Music
def addTracksGPM (trackList, api):

    #List of Song id's
    idList = []

    #Searches store for each track id and adds it too list
    for i in range(len(trackList)):
        tracks = Mobileclient.search(api, trackList[i], 50)['song_hits'][0]['track']
        idList.append(tracks['storeId'])

    #Add tracks to user library
    if(len(idList) > 0):
        Mobileclient.add_store_tracks(api, idList)

    else:
        print("All Google Play Music tracks are already added")
    return None

