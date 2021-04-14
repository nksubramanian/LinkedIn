from audio_file import AudioBookAudioFile, SongAudioFile, PodcastAudioFile
from business_errors import UserInputError
from database import Database


class AudioService:

    def __init__(self):
        self.database = Database(None)

    def __create_audio_file_handler(self, audio_file_type, database):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            return AudioBookAudioFile(self.database)
        if audio_file_type == "song":
            return SongAudioFile(self.database)
        if audio_file_type == "podcast":
            return PodcastAudioFile(self.database)
        else:
            raise UserInputError('The audio file type is not understood')

    def add_audio_file(self, audio_file_type, audio_file_id, creation_request):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
        audio_file_handler.add_audio_file(audio_file_id, creation_request)

    def get_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
        return audio_file_handler.get_audio_file(audio_file_id)

    def delete_file(self, audio_file_type, audio_file_id):
        audio_file_handler = self.__create_audio_file_handler(audio_file_type, self.database)
        return audio_file_handler.delete_audio_file(audio_file_id)














