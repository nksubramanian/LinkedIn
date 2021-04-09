from database import Database

database = Database()


class UserInputError(Exception):
    pass


class AudioService:

    def __init__(self):
        self.database = database

    def add_audio_file(self, audio_file_type, audio_file_id, r):
        if 'name' not in r.keys():
            raise UserInputError("An error occurred")
        if audio_file_type.lower() == "song":
            self.database.add_song(audio_file_id, r)



