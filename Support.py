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

def compareTrackLists(compareList, appendList, includedTracks):
    # Comparison variable
    isCommon = False
    excludedTracks = []

    # Compare tracks to check if GPM tracks common with SPTF
    for i in range(len(compareList)):
        for j in range(len(appendList)):
            # compare tracks to add common tracks to list
            if compareList[i] == appendList[j]:
                if (compareList[i] not in includedTracks):
                    includedTracks.append(compareList[i])
                isCommon = True
                break

        # add uncommon tracks to list
        if (isCommon == False):
            excludedTracks.append(compareList[i])

        isCommon = False

    return [includedTracks, excludedTracks]