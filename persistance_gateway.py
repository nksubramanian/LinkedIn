from pymongo.errors import DuplicateKeyError


class PersistenceGateway:
    def __init__(self, client):
        self.client = client
        self.db = self.client["mydatabase"]

    def update(self, collection, id_, data_dictionary):
        data_dictionary["_id"] = id_
        result = self.db[collection].replace_one({"_id": id_}, data_dictionary)
        if result.matched_count == 0:
            raise ItemNotFound()

    def add(self, collection, id_, data_dictionary):
        try:
            data_dictionary["_id"] = id_
            self.db[collection].insert_one(data_dictionary)
        except DuplicateKeyError:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def get(self, collection, audio_file_id):
        x = self.db[collection].find_one({'_id': audio_file_id})
        if x is None:
            raise ItemNotFound()
        x['id'] = x.pop('_id')
        return x

    def delete(self, collection, audio_file_id):
        result = self.db[collection].delete_one({'_id': audio_file_id})
        if result.deleted_count == 0:
            raise ItemNotFound()

    def get_all(self, collection):
        results = []
        for doc in self.db[collection].find():
            doc['id'] = doc.pop('_id')
            results.append(doc)
        return results


class UnableToInsertDueToDuplicateKeyError(Exception):
    pass


class ItemNotFound(Exception):
    pass
