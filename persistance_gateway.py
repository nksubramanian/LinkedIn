import pymongo


class PersistanceGateway:
    def __init__(self, client):
        if client is None:
            self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        else:
            self.myclient = client
        # Conection string should come from config
        self.mydb = self.myclient["mydatabase"]
        self.song_collection = self.mydb["Song"]
        self.podcast_collection = self.mydb["Podcast"]
        self.audiobook_collection = self.mydb["Audiobook"]

    def add(self, collection, id, data_dictionary):
        try:
            data_dictionary["_id"] = id
            self.mydb[collection].insert_one(data_dictionary)
        except pymongo.errors.DuplicateKeyError as error:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def get(self, collection, audio_file_id):
        x = self.mydb[collection].find_one({'_id': audio_file_id})
        if x is not None:
            return x
        raise ItemNotFound()

    def delete(self, collection, audio_file_id):
        result = self.mydb[collection].delete_one({'_id': audio_file_id})
        if result.deleted_count == 0:
            raise ItemNotFound()


class UnableToInsertDueToDuplicateKeyError(Exception):
    pass


class ItemNotFound(Exception):
    pass
