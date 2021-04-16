from abc import abstractmethod
from datetime import datetime
from business_errors import UserInputError


class Handler:
    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway

    @abstractmethod
    def _assert_creation_parameters_are_correct(self, creation_parameters):
        pass

    @abstractmethod
    def _get_valid_properties(self):
        pass

    @abstractmethod
    def _get_collection(self):
        pass

    def __filter_audio_file(self, creation_request):
        valid_properties = self._get_valid_properties()
        filtered = dict((key, value) for key, value in creation_request.items() if key in valid_properties)
        return filtered

    def update_audio_file(self, audio_file_id, creation_request):
        self._assert_creation_parameters_are_correct(creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.update(self._get_collection(), audio_file_id, filtered_creation_request)

    def add_audio_file(self, audio_file_id, creation_request):
        if type(audio_file_id) is not int:
            raise UserInputError("Audio file Id has to be an integer")
        self._assert_creation_parameters_are_correct(creation_request)
        filtered_creation_request = self.__filter_audio_file(creation_request)
        self.persistence_gateway.add(self._get_collection(), audio_file_id, filtered_creation_request)

    def get_audio_file(self, audio_file_id):
        return self.persistence_gateway.get(self._get_collection(), audio_file_id)

    def delete_audio_file(self, audio_file_id):
        self.persistence_gateway.delete(self._get_collection(), audio_file_id)

    def get_audio_files(self):
        return self.persistence_gateway.get_all(self._get_collection())


class AudioBookHandler(Handler):
    def __init__(self, persistence_gateway):
        super(AudioBookHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "audiobook"

    def _get_valid_properties(self):
        return {"title", "author", "narrator", "duration", "uploaded_time"}

    def _assert_creation_parameters_are_correct(self, creation_parameters):
        if 'title' not in creation_parameters.keys():
            raise UserInputError("Name of the song is mandatory")
        if len(creation_parameters['title']) > 100:
            raise UserInputError("Title cannot be greater than 100 characters")
        if 'author' not in creation_parameters.keys():
            raise UserInputError("Name of the song is mandatory")
        if len(creation_parameters['author']) > 100:
            print(creation_parameters['author'])
            raise UserInputError("Author cannot be greater than 100 characters")
        if 'narrator' not in creation_parameters.keys():
            raise UserInputError("Narrator is mandatory")
        if len(creation_parameters['narrator']) > 100:
            raise UserInputError("Narrator cannot be greater than 100 characters")
        if 'duration' not in creation_parameters.keys():
            raise UserInputError("Duration of the song is mandatory")
        if type(creation_parameters['duration']) != int:
            raise UserInputError("duration has to be integer")
        if creation_parameters['duration'] < 0:
            raise UserInputError("duration has to be a positive integer")
        if 'uploaded_time' not in creation_parameters.keys():
            raise UserInputError("date is mandatory")
        if type(creation_parameters['uploaded_time']) != str:
            raise UserInputError("date needs to be in string format")
        if datetime.now() > datetime.fromisoformat(creation_parameters['uploaded_time']):
            raise UserInputError("date cannot be in the past")


class SongHandler(Handler):
    def __init__(self, persistence_gateway):
        super(SongHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "song"

    def _assert_creation_parameters_are_correct(self, r):
        if 'name' not in r.keys():
            raise UserInputError("Name of the song is mandatory")
        if (type(r['name'])) is not str:
            raise UserInputError("Name has to be a string")
        if len(r['name']) > 100:
            raise UserInputError("Name cannot be greater than 100 characters")
        if len(r['name']) == r['name'].count(" "):
            raise UserInputError("Name cannot be a blank string")
        if r['name'] == "":
            raise UserInputError("Name cannot be a blank string")
        if 'duration' not in r.keys():
            raise UserInputError("Duration of the song is mandatory")
        if type(r['duration']) != int:
            raise UserInputError("duration has to be integer")
        if r['duration'] < 0:
            raise UserInputError("duration has to be a positive integer")
        if 'uploaded_time' not in r.keys():
            raise UserInputError("uploaded_time is mandatory")
        if type(r['uploaded_time']) != str:
            raise UserInputError("date needs to be in string format ex.2034-06-01 01:10:20")
        if datetime.now() > datetime.fromisoformat(r['uploaded_time']):
            raise UserInputError("date cannot be in the past")

    def _get_valid_properties(self):
        return {"name", "duration", "uploaded_time"}


class PodcastHandler(Handler):
    def __init__(self, persistence_gateway):
        super(PodcastHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "podcast"

    def _assert_creation_parameters_are_correct(self, r):
        if 'name' not in r.keys():
            raise UserInputError("Name of the podcast is mandatory")
        if type(r['name']) is not str:
            raise UserInputError("Name has to be a string")
        if r['name'] == '':
            raise UserInputError("Name of the podcast is mandatory")
        if r['name'].count(" ") == len(r['name']):
            raise UserInputError("Name of the podcast is mandatory")
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
            raise UserInputError("uploaded_time needs to be in string format")
        if datetime.now() > datetime.fromisoformat(r['uploaded_time']):
            raise UserInputError("uploaded_time cannot be in the past")
        if 'host' not in r.keys():
            raise UserInputError("Host is mandatory")
        if len(r['host']) > 100:
            raise UserInputError("Host cannot be greater than 100 characters")
        if type(r['host']) is not str:
            raise UserInputError("Host has to be a string")
        if 'participants' in r.keys():
            if type(r['participants']) != list:
                raise UserInputError("participants has to be a list")
            if len(r['participants']) > 10:
                raise UserInputError("participants can have maximum of 10 members")
            for member in r['participants']:
                if type(member) is not str:
                    raise UserInputError("Each member of the participant has to be string")
            for member in r['participants']:
                if len(member) > 100:
                    raise UserInputError("maximum characters allowed for all participants in 100")

    def _get_valid_properties(self):
        return {"name", "duration", "uploaded_time", "host", "participants"}
