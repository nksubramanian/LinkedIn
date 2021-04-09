from database import Database

database = Database()


class AudioService:
    def add_song(self, audio_file_id, r):
        database.add_song(audio_file_id, r)



