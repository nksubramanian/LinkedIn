from database import Database
from datetime import datetime

#move to a file called user_error
class UserInputError(Exception):
    pass

class AudioBookAudioFile:
    def __init__(self, database):
        self.database = database

    def add_audio_file(self, audio_file_id, creation_request):
        self.assert_audiobook_parameters(audio_file_id, creation_request)
        self.database.add_audiobook(audio_file_id, creation_request)

    def assert_audiobook_parameters(self, audio_file_id, r):
        #if title is empty
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
        if 'uploaded_time' not in r.keys():
            raise UserInputError("date is mandatory")
        if type(r['uploaded_time']) != str:
            raise UserInputError("date needs to be in string format")
        if datetime.now() > datetime.fromisoformat(r['uploaded_time']):
            raise UserInputError("date cannot be in the past")

class SongAudioFile:
    def __init__(self, database):
        self.database = database

    def add_audio_file(self, audio_file_id, creation_request):
        self.assert_song_parameters(audio_file_id, creation_request)
        self.database.add_song(audio_file_id, creation_request)

    def assert_song_parameters(self, audio_file_id, r):
        if type(audio_file_id) is not int:
            raise UserInputError("Audio file Id has to be integer")
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
        if 'uploaded_time' not in r.keys():
            raise UserInputError("uploaded_time is mandatory")
        if type(r['uploaded_time']) != str:
            raise UserInputError("date needs to be in string format")
        if datetime.now() > datetime.fromisoformat(r['uploaded_time']):
            raise UserInputError("date cannot be in the past")


class PodcastAudioFile:
    def __init__(self, database):
        self.database = database

    def add_audio_file(self, audio_file_id, creation_request):
        self.assert_podcast_parameters(audio_file_id, creation_request)
        self.database.add_podcast(audio_file_id, creation_request)

    def assert_podcast_parameters(self, audio_file_id, r):
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
        if 'uploaded_time' not in r.keys():
            raise UserInputError("uploaded_time is mandatory")
        if type(r['uploaded_time']) != str:
            raise UserInputError("uploaded_time needs to be in string format")
        if datetime.now() > datetime.fromisoformat(r['uploaded_time']):
            raise UserInputError("uploaded_time cannot be in the past")





class AudioService:

    def __init__(self):
        self.database = Database(None)

    def add_audio_file(self, audio_file_type, audio_file_id, creation_request):
        audio_file_type = audio_file_type.lower()
        if audio_file_type == "audiobook":
            audio_file = AudioBookAudioFile(self.database)
            audio_file.add_audio_file(audio_file_id, creation_request)
        elif audio_file_type == "song":
            audio_file = SongAudioFile(self.database)
            audio_file.add_audio_file(audio_file_id, creation_request)
        elif audio_file_type == "podcast":
            audio_file = PodcastAudioFile(self.database)
            audio_file.add_audio_file(audio_file_id, creation_request)
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














