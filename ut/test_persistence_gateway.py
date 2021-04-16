from pymongo.errors import DuplicateKeyError

from persistance_gateway import PersistenceGateway, UnableToInsertDueToDuplicateKeyError, ItemNotFound
import unittest
import mongomock
from flask import jsonify


class AppTests(unittest.TestCase):
    def test_add(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 3232, body_data)
        assert client.mydatabase[collection_name].find_one({'_id': 3232}) == body_data

    def test_update(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 3232, body_data)
        new_data = {'name': 'xxx'}
        persistence_gateway.update(collection_name, 3232, new_data)
        from_db = client.mydatabase[collection_name].find_one({'_id': 3232})
        assert from_db == new_data

    def test_get(self):
        body_data = {'_id': 56, 'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        collection_name = 'collection_name'
        persistence_gateway = PersistenceGateway(client)
        client.mydatabase[collection_name].insert_one(body_data)
        body_data['id'] = body_data.pop('_id')
        assert body_data == persistence_gateway.get(collection_name, 56)

    def test_delete(self):
        body_data = {'_id': 56, 'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        collection_name = 'collection_name'
        client.mydatabase[collection_name].insert_one(body_data)
        persistence_gateway.delete(collection_name, 56)
        find_result = client.mydatabase[collection_name].find_one({'_id' : 56})
        assert find_result is None


    def test_add_duplicate(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date': 'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 3232, body_data)
        with self.assertRaises(UnableToInsertDueToDuplicateKeyError):
            persistence_gateway.add(collection_name, 3232, body_data)

    def test_get_invalid(self):
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        with self.assertRaises(ItemNotFound):
            persistence_gateway.get(collection_name, 3422)

    def test_delete_invalid(self):
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        with self.assertRaises(ItemNotFound):
            persistence_gateway.delete(collection_name, 3422)

    def test_update_invalid(self):
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date': 'wef'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        with self.assertRaises(ItemNotFound):
            persistence_gateway.update(collection_name, 3232, body_data)

    def test_get_all(self):
        body_data1 = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        body_data2 = {'name': 'bsd', 'duration': 44, 'uploaded_time': 'gfdb', 'date': 'wefgs'}
        collection_name = 'collection_name'
        client = mongomock.MongoClient()
        persistence_gateway = PersistenceGateway(client)
        persistence_gateway.add(collection_name, 1, body_data1)
        persistence_gateway.add(collection_name, 2, body_data2)
        first_entry = persistence_gateway.get(collection_name, 1)
        second_entry = persistence_gateway.get(collection_name, 2)
        assert (len(persistence_gateway.get_all(collection_name))) == 2
        assert(first_entry in persistence_gateway.get_all(collection_name))
        assert (second_entry in persistence_gateway.get_all(collection_name))






