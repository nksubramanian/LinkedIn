from database import Database
import unittest
import mongomock

class AppTests(unittest.TestCase):
    def test_unsuccesful_creation_song(self):
        client = mongomock.MongoClient()
        database = Database(client)
        d = {'a': 'b'}
        database.add_song(3232, d)
        doc = client.mydatabase.Song.find_one({'_id': 3232})
        assert doc['a'] == 'b'


