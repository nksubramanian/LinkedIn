from database import Database

database = Database()


class AudioService:
    def add_audio_file(self, audio_file_type, audio_file_id, r):
        if audio_file_type.lower() == "song":
            database.add_song(audio_file_id, r)



