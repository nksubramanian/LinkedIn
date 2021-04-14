from audio_file_handler import AudioBookHandler, SongHandler, PodcastHandler
from business_errors import UserInputError
from database import UnableToInsertDueToDuplicateKeyError
from persistance_gateway import PersistanceGateway


class AudioService:

    def __init__(self):
        self.database = PersistanceGateway(None)

    def __create_audio_file_handler(self, audio_file_type, database):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            return AudioBookHandler(self.database)
        if audio_file_type == "song":
            return SongHandler(self.database)
        if audio_file_type == "podcast":
            return PodcastHandler(self.database)
        else:
            raise UserInputError('The audio file type is not understood')

    def add_audio_file(self, audio_file_type, audio_file_id, creation_request):
        try:
            audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
            audio_file_handler.add_audio_file(audio_file_id, creation_request)
        except UnableToInsertDueToDuplicateKeyError as error:
            raise UserInputError('ID already exist')

    def get_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
        return audio_file_handler.get_audio_file(audio_file_id)

    def delete_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
        audio_file_handler.delete_audio_file(audio_file_id)














