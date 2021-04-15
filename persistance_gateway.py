import pymongo


class PersistenceGateway:
    def __init__(self, client):
        self.myclient = client
        self.mydb = self.myclient["mydatabase"]

    def add(self, collection, id, data_dictionary):
        try:
            data_dictionary["_id"] = id
            self.mydb[collection].insert_one(data_dictionary)
        except pymongo.errors.DuplicateKeyError as error:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def get(self, collection, audio_file_id):
        x = self.mydb[collection].find_one({'_id': audio_file_id})
        if x is None:
            raise ItemNotFound()
        x['id'] = x.pop('_id')
        return x

    def delete(self, collection, audio_file_id):
        result = self.mydb[collection].delete_one({'_id': audio_file_id})
        if result.deleted_count == 0:
            raise ItemNotFound()

    def all_records(self, collection):
        temp = []
        for doc in self.mydb[collection].find():
            doc['id'] = doc.pop('_id')
            temp.append(doc)
        return temp


class UnableToInsertDueToDuplicateKeyError(Exception):
    pass


class ItemNotFound(Exception):
    pass
