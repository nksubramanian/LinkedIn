import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#Conection string should come from config
mydb = myclient["mydatabase"]
song_collection = mydb["Song"]

class AudioService:
    def add_song(self, audio_file_id, r):
        mydict = {"_id": audio_file_id,
                  "audio_file_type": "SONG",
                  "name": r.name,
                  "duration": r.duration,
                  "uploaded_time": r.uploaded_time}

        x = song_collection.insert_one(mydict).inserted_id

