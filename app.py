from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import pymongo


app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
SongCollection = mydb["Song"]



class Request:
    def __init__(self, dictionary):
        self.__dict__ = dictionary


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def join_room(audio_file_type, audio_file_id):
    print(audio_file_type)
    print(audio_file_id)
    r = Request(request.get_json())
    print(r.name)
    print(r.duration)
    print(r.uploaded_time)

    mydict = {"_id": audio_file_id,
              "audio_file_type": "SONG",
              "name": r.name,
              "duration": r.duration,
              "uploaded_time": r.uploaded_time }

    x = SongCollection.insert_one(mydict).inserted_id
    print(x)
    return "ddd"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
