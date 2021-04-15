from pymongo.errors import DuplicateKeyError

from persistance_gateway import PersistenceGateway, UnableToInsertDueToDuplicateKeyError, ItemNotFound
import unittest
import mongomock


class AppTests(unittest.TestCase):
    def test_successful_add_method_db(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 3232, body_data)
        assert client.mydatabase[collection_name].find_one({'_id': 3232}) == body_data

    def test_successful_get_method_db(self):
        body_data = {'_id': 56, 'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        collection_name = 'collection_name'
        persistence_gateway = PersistenceGateway(client)
        client.mydatabase[collection_name].insert_one(body_data)
        body_data['id'] = body_data.pop('_id')
        assert body_data == persistence_gateway.get(collection_name, 56)

    def test_successful_delete_method_db(self):
        body_data = {'_id': 56, 'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        collection_name = 'collection_name'
        client.mydatabase[collection_name].insert_one(body_data)
        persistence_gateway.delete(collection_name, 56)
        find_result = client.mydatabase[collection_name].find_one({'_id' : 56})
        assert find_result is None


    def test_failure_for_duplicate_creation(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date': 'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 3232, body_data)
        with self.assertRaises(UnableToInsertDueToDuplicateKeyError):
            persistence_gateway.add(collection_name, 3232, body_data)

    def test_failure_for_invalid_get(self):
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        with self.assertRaises(ItemNotFound):
            persistence_gateway.get(collection_name, 3422)

    def test_failure_for_invalid_delete(self):
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        with self.assertRaises(ItemNotFound):
            persistence_gateway.delete(collection_name, 3422)





