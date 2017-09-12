
from SPTF import authSPTF, getTracksSPTF, addTracksSPTF
from GPM import authGPM, getTracksGPM, addTracksGPM
from Support import compareTrackLists

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('mainPage.html')

# @app.route('/my_function', methods=['POST'])
# def my_function():
#     text = request.json['data']
#     processed_text = text.upper()
#     print(processed_text)
#     return processed_text

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/sync')
def sync():
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
    includedTracks = []

    #Compare lists
    includedTracks, excludedTracksSPTF = compareTrackLists(gpmList, sptfList, includedTracks)[0], compareTrackLists(gpmList, sptfList, includedTracks)[1]
    includedTracks, excludedTracksGPM = compareTrackLists(sptfList, gpmList, includedTracks)[0], compareTrackLists(sptfList, gpmList, includedTracks)[1]

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

    return '<html><meta http-equiv="refresh" content="0; url=/" /></html>'

if __name__ == '__main__':
    app.run()