import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#Conection string should come from config
mydb = myclient["mydatabase"]
song_collection = mydb["Song"]
podcast_collection = mydb["Podcast"]
audiobook_collection = mydb["Audiobook"]


class Database:
    def add_song(self, id, data_dictionary):
        data_dictionary["_id"] = id
        x = song_collection.insert_one(data_dictionary).inserted_id

    def add_podcast(self, id, data_dictionary):
        data_dictionary["_id"] = id
        x = podcast_collection.insert_one(data_dictionary).inserted_id

    def add_audiobook(self, id, data_dictionary):
        data_dictionary["_id"] = id
        x = audiobook_collection.insert_one(data_dictionary).inserted_id

    def get_audiobook(self, audio_file_id):
        for x in audiobook_collection.find():
            if x["_id"] == audio_file_id:
                return x
        return {"audiobook":"audiobook does not exists"}

    def get_song(self, audio_file_id):
        for x in song_collection.find():
            if x["_id"] == audio_file_id:
                print("I am here")
                return x
        return {"song":"does not exists"}

    def get_podcast(self, audio_file_id):
        for x in audiobook_collection.find():
            if x["_id"] == audio_file_id:
                return x
        return {"podcast": "does not exists"}

    def delete_audiobook(self, audio_file_id):
        for x in audiobook_collection.find():
            if x["_id"] == audio_file_id:
                print("final")
                audiobook_collection.remove({'_id': audio_file_id})
                return {"audiobook": "audiobooks are deleted"}
        return {"audiobook": "audiobook does not exists"}

    def delete_song(self, audio_file_id):
        for x in song_collection.find():
            if x["_id"] == audio_file_id:
                song_collection.remove({'_id': audio_file_id})
                return {"song": "song is deleted"}
        return {"song": "song does not exists"}

    def delete_podcast(self, audio_file_id):
        for x in song_collection.find():
            if x["_id"] == audio_file_id:
                song_collection.remove({'_id': audio_file_id})
                return {"podcast": "podcast is deleted"}
        return {"podcast": "podcast does not exists"}

