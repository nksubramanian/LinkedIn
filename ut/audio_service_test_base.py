from pymongo import MongoClient

from audio_service import AudioFileService
from persistance_gateway import PersistenceGateway


class AudioServiceTestBase:
    def create_service_and_gateway(self):
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        return audio_file_service, persistence_gateway