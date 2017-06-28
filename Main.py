import sys
import spotipy
import spotipy.util as util
from SPTF import getTracksSPTF

#sptfusername = input('Enter your Spotify username:')
sptfUsername = 'acepilotirl'

print(getTracksSPTF(sptfUsername))