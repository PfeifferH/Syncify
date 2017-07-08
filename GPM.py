from gmusicapi import Mobileclient



def getTracksGPM (email, password):
    api = Mobileclient()
    logged_in = api.login(email, password, '352bb0c3576e547d')
    # logged_in is True if login was successful


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