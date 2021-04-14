import pymongo

class UnableToInsertDueToDuplicateKeyError(Exception):
    pass


class Database:
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

    #delete
    def get_count(self, audio_file_type, audio_file_id):
        if audio_file_type == "song":
            return self.song_collection.count_documents({'_id': audio_file_id})
        if audio_file_type == "podcast":
            return self.podcast_collection.count_documents({'_id': audio_file_id})
        if audio_file_type == "audiobook":
            return self.audiobook_collection.count_documents({'_id': audio_file_id})


    def add_song(self, id, data_dictionary):
        try:
            data_dictionary["_id"] = id
            self.song_collection.insert_one(data_dictionary)
        except pymongo.errors.DuplicateKeyError as error:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def add_podcast(self, id, data_dictionary):
        try:
            data_dictionary["_id"] = id
            self.podcast_collection.insert_one(data_dictionary)
        except pymongo.errors.DuplicateKeyError as error:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def add_audiobook(self, id, data_dictionary):
        try:
            data_dictionary["_id"] = id
            self.audiobook_collection.insert_one(data_dictionary)
        except pymongo.errors.DuplicateKeyError as error:
            raise UnableToInsertDueToDuplicateKeyError("Id already exists")

    def get_audiobook(self, audio_file_id):
        return self.audiobook_collection.find_one({'_id': audio_file_id})
        #return {"audiobook":"audiobook does not exists"}

    def get_song(self, audio_file_id):
        return self.song_collection.find_one({'_id': audio_file_id})
        #return {"song":"does not exists"}

    def get_podcast(self, audio_file_id):
        return self.podcast_collection.find_one({'_id': audio_file_id})
        #return {"podcast": "does not exists"}

    def delete_audiobook(self, audio_file_id):
        for x in self.audiobook_collection.find():
            if x["_id"] == audio_file_id:
                print("final")
                self.audiobook_collection.remove({'_id': audio_file_id})
                return {"audiobook": "audiobooks are deleted"}
        return {"audiobook": "audiobook does not exists"}

    def delete_song(self, audio_file_id):
        for x in self.song_collection.find():
            if x["_id"] == audio_file_id:
                self.song_collection.remove({'_id': audio_file_id})
                return {"song": "song is deleted"}
        return {"song": "song does not exists"}

    def delete_podcast(self, audio_file_id):
        for x in self.podcast_collection.find():
            if x["_id"] == audio_file_id:
                self.podcast_collection.remove({'_id': audio_file_id})
                return {"podcast": "podcast is deleted"}
        return {"podcast": "podcast does not exists"}

