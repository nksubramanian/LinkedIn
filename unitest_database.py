from persistance_gateway import PersistanceGateway
import unittest
import mongomock

class AppTests(unittest.TestCase):
    def test_successful_add_method_db(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        database = PersistanceGateway(client)
        database.add_song(3232, body_data)
        assert client.mydatabase.Song.find_one({'_id': 3232}) == body_data
        database.add_podcast(3232, body_data)
        assert client.mydatabase.Podcast.find_one({'_id': 3232}) == body_data
        database.add_audiobook(3232, body_data)
        assert client.mydatabase.Audiobook.find_one({'_id': 3232}) == body_data


    def test_successful_get_method_db(self):
        body_data = {'_id':56, 'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        database = PersistanceGateway(client)
        database.add_song(3232, body_data)
        assert body_data == database.get_song(3232)
        database.add_podcast(3232, body_data)
        assert body_data == database.get_podcast(3232)
        database.add_audiobook(3232, body_data)
        assert body_data == database.get_audiobook(3232)


    def test_successful_delete_method_db(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        database = PersistanceGateway(client)
        database.add_song(3443, body_data)
        assert client.mydatabase.Song.count_documents({'_id': 3443}) == 1
        database.delete_song(3443)
        assert client.mydatabase.Song.count_documents({'_id': 3443}) == 0
        database.add_podcast(3443, body_data)
        assert client.mydatabase.Podcast.count_documents({'_id': 3443}) == 1
        database.delete_podcast(3443)
        assert client.mydatabase.Podcast.count_documents({'_id': 3443}) == 0
        database.add_audiobook(3443, body_data)
        assert client.mydatabase.Audiobook.count_documents({'_id': 3443}) == 1
        database.delete_audiobook(3443)
        assert client.mydatabase.Audiobook.count_documents({'_id': 3443}) == 0









