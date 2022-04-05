from flask import Flask 
<<<<<<< HEAD
from flask_restful import Resource, Api
import pandas as pd
from data_user_info import topartists as ta, toptracks as tt, playlists as pl, user_info as ui
=======
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
>>>>>>> main

app = Flask(__name__)
api = Api(app)

class Playlists(Resource):
<<<<<<< HEAD
    def get(self):
        return pl(), 200
=======
    # methods go here
    pass
>>>>>>> main

class Playlist(Resource):
    # methods go here
    pass

class topArtists(Resource):
<<<<<<< HEAD
    def get(self):
        return ta(), 200
        
class topTracks(Resource):
    def get(self):
        return tt(), 200
    
=======
    # methods go here
    pass


class topTracks(Resource):
    # methods go here
    pass

>>>>>>> main
api.add_resource(Playlists, '/playlists') # returns all playlists, playlistImage, playlistName, numberOfTracks, playlistID
api.add_resource(Playlist, '/playlists/{playlistId}') # returns specific playlist and top genres

api.add_resource(topArtists, '/topArtists') #returns top artists short-term, medium and long term 
api.add_resource(topTracks, '/topTracks')   #returns top tracks short-term, medium and long term 

<<<<<<< HEAD

if __name__ == '__main__':
    app.run(debug = True)  
=======
if __name__ == '__main__':
    app.run()  # run our Flask app
>>>>>>> main
