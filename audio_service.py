from audio_file import AudioBookAudioFile, SongAudioFile, PodcastAudioFile
from business_errors import UserInputError
from database import Database
from datetime import datetime


class AudioService:

    def __init__(self):
        self.database = Database(None)

    def __create_audio_file(self, audio_file_type, database):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            return AudioBookAudioFile(self.database)
        elif audio_file_type == "song":
            return SongAudioFile(self.database)
        elif audio_file_type == "podcast":
            return PodcastAudioFile(self.database)
        else:
            raise UserInputError('The audio file type is not understood')

    def add_audio_file(self, audio_file_type, audio_file_id, creation_request):
        audio_file = self.__create_audio_file(audio_file_type, self.database)
        audio_file.add_audio_file(audio_file_id, creation_request)


    def __retrieve_audio_file(self, audio_file_type, database):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            return AudioBookAudioFile(self.database)
        elif audio_file_type == "song":
            return SongAudioFile(self.database)
        elif audio_file_type == "podcast":
            return PodcastAudioFile(self.database)
        else:
            raise UserInputError('The audio file type is not understood')



    def get_file(self, audio_file_type, audio_file_id):
        if audio_file_type.lower() == "audiobook":
            return self.database.get_audiobook(audio_file_id)
        if audio_file_type.lower() == "song":
            return self.database.get_song(audio_file_id)
        if audio_file_type.lower() == "podcast":
            return self.database.get_podcast(audio_file_id)

    def delete_file(self, audio_file_type, audio_file_id):
        if audio_file_type.lower() == "audiobook":
            return self.database.delete_audiobook(audio_file_id)
        if audio_file_type.lower() == "song":
            return self.database.delete_song(audio_file_id)
        if audio_file_type.lower() == "podcast":
            return self.database.delete_podcast(audio_file_id)














