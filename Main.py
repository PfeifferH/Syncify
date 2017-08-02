
from SPTF import authSPTF, getTracksSPTF, addTracksSPTF
from GPM import authGPM, getTracksGPM, addTracksGPM

from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    #sptfusername = input('Enter your Spotify username:')
    sptfUsername = 'acepilotirl'

    gmail = 'pfeifferhayden@gmail.com'
    gpw = 'Hoppy6858'

    #Authorize with spotify
    logSPTF = authSPTF(sptfUsername)

    #Authorize with Google Play Music
    logGPM = authGPM(gmail, gpw)

    print("Google Play: ")
    print(getTracksGPM(logGPM))
    print("Spotify: " )
    print(getTracksSPTF(logSPTF))


    #Tracks lists
    gpmList = getTracksGPM(logGPM)
    sptfList = getTracksSPTF(logSPTF)

    #Lists to compare which tracks are not common
    includedTracks = []
    excludedTracksSPTF = []
    #Comparison variable
    isCommon = False

    #Compare tracks to check if GPM tracks common with SPTF
    for i in range(len(gpmList)):
        for j in range(len(sptfList)):
            #compare tracks to add common tracks to list
            if gpmList[i] == sptfList[j]:
                includedTracks.append(gpmList[i])
                isCommon = True
                break

        #add uncommon tracks to list
        if (isCommon == False):
            excludedTracksSPTF.append(gpmList[i])

        isCommon = False

    #Do the same process but for Spotify tracks
    isCommon = False
    excludedTracksGPM = []

    for i in range(len(sptfList)):
        for j in range(len(gpmList)):
            #compare tracks to add common tracks to list
            if sptfList[i] == gpmList[j]:
                isCommon = True
                break

        #add uncommon tracks to list
        if (isCommon == False):
            excludedTracksGPM.append(sptfList[i])

        isCommon = False


    print("")
    print("Included Tracks: ")
    print(includedTracks)
    print("Excluded Tracks from Spotify: ")
    print(excludedTracksSPTF)
    print("Excluded Tracks from GPM: ")
    print(excludedTracksGPM)

    #Add tracks to Spotify and Google PLay Music
    addTracksSPTF(excludedTracksSPTF, logSPTF)
    addTracksGPM(excludedTracksGPM, logGPM)

    return "Completed"

if __name__ == '__main__':
    app.run()