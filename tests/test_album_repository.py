from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get all records in the database.
"""

def test_all_records(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = AlbumRepository(db_connection)

    result = repository.all()

    assert result == [
        Album(1, 'An American Prayer', 1978, 1)] 


"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, 'Voyage', 2022, 2))
    result = repository.all()
 
    assert result == [
        Album(1, 'An American Prayer', 1978, 1),
        Album(2, 'Voyage', 2022, 2) 
    ]