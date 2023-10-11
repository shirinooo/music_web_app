from lib.artist import Artist

class ArtistRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    def create(self, artist):
            self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                    artist.name, artist.genre])
            return 'Artist was added succefully!'
            