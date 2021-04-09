import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#Conection string should come from config
mydb = myclient["mydatabase"]


class Database:
    def add_song(self, id, data_dictionary):
        song_collection = mydb["Song"]
        data_dictionary["_id"] = id
        x = song_collection.insert_one(data_dictionary).inserted_id