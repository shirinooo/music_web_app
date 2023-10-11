
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '' \
        'Album(1, An American Prayer, 1978, 1)' 



"""
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

"""

def test_post_album(web_client, db_connection):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.post('/albums', data={
        'title': 'Voyage',
        'release_year': '2022',
        'artist_id': '2'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Album created succefully!'

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, An American Prayer, 1978, 1)\n" \
        "Album(2, Voyage, 2022, 2)"


"""
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

"""
def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Pop)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)"



"""
# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

"""

def test_post_artist(web_client, db_connection):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Artist was added succefully!'

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Pop)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Wild nothing, Indie)"
        




# === Example Code Below ===

# """
# GET /emoji
# """
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
