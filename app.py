import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from flask import Flask, request


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    repository.create(album)
    return 'Album created succefully!'

@app.route('/albums')
def get_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(f"{album}" for album in repository.all())


@app.route('/artists')
def get_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(f"{artist}" for artist in repository.all())

@app.route('/artists', methods=['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return 'Artist was added succefully!'




# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
# @app.route('/emoji', methods=['GET'])
# def get_emoji():
#     return ":)"

# # This imports some more example routes for you to see how they work
# # You can delete these lines if you don't need them.
# from example_routes import apply_example_routes
# apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

