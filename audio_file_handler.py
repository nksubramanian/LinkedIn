from abc import abstractmethod
from datetime import datetime
from business_errors import UserInputError


class Handler:
    def __init__(self, persistence_gateway):
        self.persistence_gateway = persistence_gateway

    @abstractmethod
    def _assert_creation_parameters_are_correct(self, creation_parameters):  # pragma: no cover
        pass

    @abstractmethod
    def _get_valid_properties(self):  # pragma: no cover
        pass

    @abstractmethod
    def _get_collection(self):  # pragma: no cover
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

    def _assert_property_is_valid_string(self, dictionary, property_name, max_length):
        if property_name not in dictionary.keys():
            raise UserInputError(f"{property_name} is mandatory")
        val = dictionary[property_name]
        if type(val) != str:
            raise UserInputError(f"{property_name} has to be a string")
        if val.isspace():
            raise UserInputError(f"{property_name} is mandatory")
        if len(val) > max_length:
            raise UserInputError(f"{property_name}'s max length is {max_length}")
        if len(val) == 0:
            raise UserInputError(f"{property_name} is mandatory")

    def _assert_property_is_positive_integer(self, dictionary, property_name):
        if property_name not in dictionary.keys():
            raise UserInputError(f"{property_name} is mandatory")
        val = dictionary[property_name]
        if type(val) != int:
            raise UserInputError(f"{property_name} has to be a integer")
        if val <= 0:
            raise UserInputError(f"{property_name} has to be a positive integer")

    def _assert_property_is_valid_datetime_string(self, r, property_name):
        if property_name not in r.keys():
            raise UserInputError(f"{property_name} is mandatory")
        if type(r[property_name]) != str:
            raise UserInputError(f"{property_name} needs to be in string format ex.2034-06-01 01:10:20")
        try:
            if datetime.now() > datetime.fromisoformat(r[property_name]):
                raise UserInputError(f"{property_name} cannot be in the past")
        except ValueError:
            raise UserInputError(f"{property_name} needs to be in string format ex.2034-06-01 01:10:20")

class AudioBookHandler(Handler):
    def __init__(self, persistence_gateway):
        super(AudioBookHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "audiobook"

    def _get_valid_properties(self):
        return {"title", "author", "narrator", "duration", "uploaded_time"}

    def _assert_creation_parameters_are_correct(self, creation_parameters):
        self._assert_property_is_valid_string(creation_parameters, 'title', 100)
        self._assert_property_is_valid_string(creation_parameters, 'author', 100)
        self._assert_property_is_valid_string(creation_parameters, 'narrator', 100)
        self._assert_property_is_positive_integer(creation_parameters, 'duration')
        self._assert_property_is_valid_datetime_string(creation_parameters, 'uploaded_time')


class SongHandler(Handler):
    def __init__(self, persistence_gateway):
        super(SongHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "song"

    def _assert_creation_parameters_are_correct(self, r):
        self._assert_property_is_valid_string(r, 'name', 100)
        self._assert_property_is_positive_integer(r, 'duration')
        self._assert_property_is_valid_datetime_string(r, 'uploaded_time')

    def _get_valid_properties(self):
        return {"name", "duration", "uploaded_time"}


class PodcastHandler(Handler):
    def __init__(self, persistence_gateway):
        super(PodcastHandler, self).__init__(persistence_gateway)

    def _get_collection(self):
        return "podcast"

    def _assert_creation_parameters_are_correct(self, r):
        self._assert_property_is_valid_string(r, 'name', 100)
        self._assert_property_is_positive_integer(r, 'duration')
        self._assert_property_is_valid_datetime_string(r, 'uploaded_time')
        self._assert_property_is_valid_string(r, 'host', 100)
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
