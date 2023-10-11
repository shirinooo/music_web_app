from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get all records in the database.
"""

def test_all_artist(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = ArtistRepository(db_connection)

    result = repository.all()

    assert result == [
        Artist(1, 'Pixies', 'Pop'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
        ] 


"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_artist(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, 'The Doors', 'Rock'))
    result = repository.all()
 
    assert result == [
        Artist(1, 'Pixies', 'Pop'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'The Doors', 'Rock')
        ] 