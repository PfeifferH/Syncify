import sys
import spotipy
import spotipy.util as util
from SPTF import getTracksSPTF
from GPM import getTracksGPM

#sptfusername = input('Enter your Spotify username:')
sptfUsername = 'acepilotirl'

gmail = 'pfeifferhayden@gmail.com'
gpw = 'Hoppy6858'

print("Google Play: ")
print(getTracksGPM(gmail, gpw))
print("Spotify: " )
print(getTracksSPTF(sptfUsername))

#Tracks lists
gpmList = getTracksGPM(gmail, gpw)
sptfList = getTracksSPTF(sptfUsername)

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