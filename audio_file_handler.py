from datetime import datetime
from business_errors import UserInputError


class AudioBookHandler:
    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway
        self.collection = "audiobook"

    def update_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.update(self.collection, audio_file_id, filtered_creation_request)

    def add_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.add(self.collection, audio_file_id, filtered_creation_request)

    def __assert_creation_parameters_are_correct(self, audio_file_id, r):
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

    def get_audio_file(self, audio_file_id):
        return self.persistence_gateway.get(self.collection, audio_file_id)

    def delete_audio_file(self, audio_file_id):
        self.persistence_gateway.delete(self.collection, audio_file_id)

    def __filter_audio_file(self, creation_request):
        filtered_creation_request = dict((key, value) for key, value in creation_request.items() if key in {"title", "author","narrator","duration","uploaded_time"})
        return filtered_creation_request

    def get_audio_files(self):
        return self.persistence_gateway.all_records(self.collection)




class SongHandler:
    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway
        self.collection = "song"

    def update_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.update(self.collection, audio_file_id, filtered_creation_request)

    def add_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.add(self.collection, audio_file_id, filtered_creation_request)

    @staticmethod
    def __assert_creation_parameters_are_correct(audio_file_id, r):
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

    def get_audio_file(self, audio_file_id):
        return self.persistence_gateway.get(self.collection, audio_file_id)

    def delete_audio_file(self, audio_file_id):
        return self.persistence_gateway.delete(self.collection, audio_file_id)

    def __filter_audio_file(self, creation_request):
        filtered_creation_request = dict((key, value) for key, value in creation_request.items() if key in {"name", "duration", "uploaded_time"})
        return filtered_creation_request

    def get_audio_files(self):
        return self.persistence_gateway.all_records(self.collection)


class PodcastHandler:
    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway
        self.collection = 'podcast'

    def update_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.update(self.collection, audio_file_id, filtered_creation_request)

    def add_audio_file(self, audio_file_id, creation_request):
        self.__assert_creation_parameters_are_correct(audio_file_id, creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.add(self.collection, audio_file_id, filtered_creation_request)


    @staticmethod
    def __assert_creation_parameters_are_correct(audio_file_id, r):
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

    def get_audio_file(self, audio_file_id):
        return self.persistence_gateway.get(self.collection, audio_file_id)

    def delete_audio_file(self, audio_file_id):
        return self.persistence_gateway.delete(self.collection, audio_file_id)

    def __filter_audio_file(self, creation_request):
        filtered_creation_request = dict((key, value) for key, value in creation_request.items() if key in {"name", "duration", "uploaded_time", "host", "participants"})
        return filtered_creation_request

    def get_audio_files(self):
        return self.persistence_gateway.all_records(self.collection)

