from database import Database

database = Database()


class UserInputError(Exception):
    pass


class AudioService:

    def __init__(self):
        self.database = database

    def add_audio_file(self, audio_file_type, audio_file_id, r):
        if audio_file_type.lower() == "audiobook":
            self.assert_audiobook_parameters(audio_file_type, audio_file_id, r)
            self.database.add_audiobook(audio_file_type, audio_file_id, r)
        if audio_file_type.lower() == "song":
            self.assert_song_parameters(audio_file_type, audio_file_id, r)
            self.database.add_song(audio_file_type,audio_file_id, r)
        if audio_file_type.lower() == "podcast":
            self.assert_podcast_parameters(audio_file_type, audio_file_id, r)
            self.database.add_podcast(audio_file_type,audio_file_id, r)

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

    def assert_song_parameters(self, audio_file_type, audio_file_id, r):
        if type(audio_file_id) is not int:
            raise UserInputError("Audio file Id has to be integer")
        if 'name' not in r.keys():
            raise UserInputError("Name of the song is mandatory")
        if 'duration' not in r.keys():
            raise UserInputError("Duration of the song is mandatory")
        if type(r['duration']) != int:
            raise UserInputError("duration has to be integer")
        if r['duration'] < 0:
            raise UserInputError("duration has to be a positive integer")
        if len(r['name']) > 100:
            raise UserInputError("Name cannot be greater than 100 characters")
        if 'date' not in r.keys():
            raise UserInputError("date is mandatory")


    def assert_podcast_parameters(self, audio_file_type, audio_file_id, r):
        if 'name' not in r.keys():
            raise UserInputError("Name of the song is mandatory")
        if len(r['name']) > 100:
            raise UserInputError("Name cannot be greater than 100 characters")
        if 'duration' not in r.keys():
            raise UserInputError("Duration of the song is mandatory")
        if type(r['duration']) != int:
            raise UserInputError("duration has to be integer")
        if r['duration'] < 0:
            raise UserInputError("duration has to be a positive integer")
        if 'host' not in r.keys():
            raise UserInputError("Host is mandatory")
        if len(r['host']) > 100:
            raise UserInputError("Host cannot be greater than 100 characters")
        if 'participants' in r.keys():
            if type(r['participants'])!=list:
                raise UserInputError("participants has to be a list")
            if len(r['participants']) > 10:
                raise UserInputError("participants can have maximum of 10 members")
            for member in r['participants']:
                if len(member) > 100:
                    raise UserInputError("maximum characters allowed for all participants in 100")

    def assert_audiobook_parameters(self, audio_file_type, audio_file_id, r):
        if 'title' not in r.keys():
            raise UserInputError("Name of the song is mandatory")
        if len(r['title']) > 100:
            raise UserInputError("Title cannot be greater than 100 characters")
        if 'author' not in r.keys():
            raise UserInputError("Name of the song is mandatory")
        if len(r['author']) > 100:
            print(r['author'])
            raise UserInputError("Author cannot be greater than 100 characters")
        if 'narrator' not in r.keys():
            raise UserInputError("Narrator is mandatory")
        if len(r['narrator']) > 100:
            raise UserInputError("Narrator cannot be greater than 100 characters")
        if 'duration' not in r.keys():
            raise UserInputError("Duration of the song is mandatory")
        if type(r['duration']) != int:
            raise UserInputError("duration has to be integer")
        if r['duration'] < 0:
            raise UserInputError("duration has to be a positive integer")








