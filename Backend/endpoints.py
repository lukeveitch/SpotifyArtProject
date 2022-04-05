from flask import Flask 
from flask_restful import Resource, Api
import pandas as pd
from data_user_info import topartists as ta, toptracks as tt, playlists as pl, user_info as ui

app = Flask(__name__)
api = Api(app)

class Playlists(Resource):
    def get(self):
        return pl(), 200

class Playlist(Resource):
    # methods go here
    pass

class topArtists(Resource):
    def get(self):
        return ta(), 200
        
class topTracks(Resource):
    def get(self):
        return tt(), 200
    
api.add_resource(Playlists, '/playlists') # returns all playlists, playlistImage, playlistName, numberOfTracks, playlistID
api.add_resource(Playlist, '/playlists/{playlistId}') # returns specific playlist and top genres

api.add_resource(topArtists, '/topArtists') #returns top artists short-term, medium and long term 
api.add_resource(topTracks, '/topTracks')   #returns top tracks short-term, medium and long term 


if __name__ == '__main__':
    app.run(debug = True)  