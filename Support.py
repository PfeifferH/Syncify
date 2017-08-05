#Format track names before adding to list
def trackFormat(track, artist):

    track, artist = track.upper(), artist.upper()

    if '(' in track:
        track = track.split(' (')[0]
    if ' -' in track:
        track = track.split(' -')[0]

    if '$' in artist:
        artistNameList = artist.split('$')
        artist = artistNameList[0] + 'S' + artistNameList[1]

    trackName = track + " - " + artist
    return trackName;