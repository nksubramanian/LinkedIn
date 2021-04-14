from app import app
from audio_service import AudioFileService
from persistance_gateway import PersistenceGateway
from pymongo import MongoClient

import os
database_uri = os.environ['AUDIO_FILE_SERVER_DATABASE_URI']
if database_uri is None:
    database_uri = "mongodb://localhost:27017/"

mongo_client = MongoClient(database_uri)
persistence_gateway = PersistenceGateway(mongo_client)
audio_file_service = AudioFileService(persistence_gateway)
app.service = audio_file_service

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

