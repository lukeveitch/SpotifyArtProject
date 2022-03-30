from flask import Flask 
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Playlists(Resource):
    # methods go here
    pass

class topArtists(Resource):
    # methods go here
    pass

class topTracks(Resource):
    # methods go here
    pass

api.add_resource(Playlists, '/playlists') # returns all playlists, playlistImage, playlistName, numberOfTracks, playlistID
api.add_resource(Playlists, '/playlists/{playlistId}') # returns specific playlist and top genres

api.add_resource(topArtists, '/topArtists') #returns top artists short-term, medium and long term 
api.add_resource(topTracks, '/topTracks')   #returns top tracks short-term, medium and long term 

