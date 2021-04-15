from audio_file_handler import AudioBookHandler, SongHandler, PodcastHandler
from business_errors import UserInputError
from persistance_gateway import PersistenceGateway, UnableToInsertDueToDuplicateKeyError, ItemNotFound


class AudioFileService:

    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway

    def __create_audio_file_handler(self, audio_file_type, database):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            return AudioBookHandler(self.persistence_gateway)
        if audio_file_type == "song":
            return SongHandler(self.persistence_gateway)
        if audio_file_type == "podcast":
            return PodcastHandler(self.persistence_gateway)
        else:
            raise UserInputError('The audio file type is not understood')

    def add_audio_file(self, audio_file_type, audio_file_id, creation_request):
        try:
            audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.persistence_gateway)
            audio_file_handler.add_audio_file(audio_file_id, creation_request)
        except UnableToInsertDueToDuplicateKeyError as error:
            raise UserInputError('ID already exist')

    def get_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.persistence_gateway)
        try:
            return audio_file_handler.get_audio_file(audio_file_id)
        except ItemNotFound as error:
            raise UserInputError("The requested item was not found")

    def delete_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.persistence_gateway)
        try:
            audio_file_handler.delete_audio_file(audio_file_id)
        except ItemNotFound as error:
            raise UserInputError("Item to be deleted is not found")

    def get_files(self, audio_file_type):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.persistence_gateway)
        return audio_file_handler.get_audio_files()
















