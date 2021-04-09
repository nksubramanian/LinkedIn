from database import Database

database = Database()


class AudioService:
    def add_song(self, audio_file_id, r):
        mydict = {"audio_file_type": "SONG",
                  "name": r.name,
                  "duration": r.duration,
                  "uploaded_time": r.uploaded_time}
        database.add_song(audio_file_id, mydict)



