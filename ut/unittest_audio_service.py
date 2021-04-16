import unittest
from unittest.mock import MagicMock

from mongomock import MongoClient

from audio_service import AudioFileService
from business_errors import UserInputError
from persistance_gateway import PersistenceGateway

l = [
     ("song", "Name cannot be a blank string", {'name': '', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
     ("song", "Name cannot be a blank string", {'name': '  ', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
     ("song", "Audio file Id has to be an integer", {'name': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, "t"),
     ("song", "Name of the song is mandatory", {'namea': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
     ("song", "Name cannot be greater than 100 characters", {'name': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                                                             'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
    ("song", "Duration of the song is mandatory", {'name': 'gh', 'ruration': 45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
    ("song", "duration has to be integer", {'name': 'gh', 'duration': '4e5', 'uploaded_time': "2034-06-01 01:10:20"}, 4),
    ("song", "duration has to be a positive integer", {'name': 'gh', 'duration': -45, 'uploaded_time': "2034-06-01 01:10:20"}, 4),
    ("song", "uploaded_time is mandatory", {'name': 'gh', 'duration': 45, '1uploaded_time': "2034-06-01 01:10:20"}, 4),
    ("song", "date needs to be in string format ex.2034-06-01 01:10:20", {'name': 'gh', 'duration': 45, 'uploaded_time':  [2032, 3, 4]}, 4),
    ("song", "duration has to be a positive integer", {'name': 'gh', 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"}, 4),
    ("song", "Name has to be a string", {'name': 34, 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"}, 4)
     ]


class AudioServiceTestBase:
    def create_service_and_gateway(self):
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        return audio_file_service, persistence_gateway


class SongCreationParameterTests(unittest.TestCase, AudioServiceTestBase):
    def setUp(self):
        (service, gateway) = self.create_service_and_gateway()
        self.service = service
        self.gateway = gateway

    def get_tests(self):
        return [
            ("song",
            "Name cannot be a blank string",
             {'name': '', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "Name cannot be a blank string",
             {'name': '  ', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "Audio file Id has to be an integer",
             {'name': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             "t"),

            ("song",
             "Name of the song is mandatory",
             {'namea': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "Name cannot be greater than 100 characters",
             {
                 'name': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                 'duration': 45,
                 'uploaded_time': "2034-06-01 01:10:20"
             },
             4),

            ("song",
             "Duration of the song is mandatory",
             {'name': 'gh', 'ruration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "duration has to be integer",
             {'name': 'gh', 'duration': '4e5', 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "duration has to be a positive integer",
             {'name': 'gh', 'duration': -45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "uploaded_time is mandatory",
             {'name': 'gh', 'duration': 45, '1uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "date needs to be in string format ex.2034-06-01 01:10:20",
             {'name': 'gh', 'duration': 45, 'uploaded_time': [2032, 3, 4]},
             4),

            ("song",
             "duration has to be a positive integer",
             {'name': 'gh', 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"},
             4),

            ("song",
             "Name has to be a string",
             {'name': 34, 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"},
             4)
        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])




class AudioServiceTests(unittest.TestCase):
    def test_add_validation(self):
        global l
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        for t in l:
            try:
                audio_file_service.add_audio_file(t[0], t[3], t[2])
                exception_thrown = False
            except UserInputError as error:
                assert error.args[0] == t[1]
                exception_thrown = True
            assert exception_thrown is True



    def test_add_audio_file(self):
        song_body_data = {'name': 'b', 'duration': 4, 'uploaded_time': '2031-04-14 14:41:32', 'date':'wef'}
        podcast_body_data = {'name': 'gh',
                             'duration': 45,
                             'uploaded_time': '2031-04-14 14:41:32',
                             'host': 'abced',
                             "participants": ["ac", "ca"]}
        audiobook_body_data = {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78, "uploaded_time": '2031-04-14 14:41:32'}
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        audio_file_service.add_song = MagicMock(return_value=None)
        audio_file_service.add_podcast = MagicMock(return_value=None)
        audio_file_service.add_audiobook = MagicMock(return_value=None)
        assert audio_file_service.add_audio_file("song", 9999, song_body_data) is None
        assert audio_file_service.add_audio_file("podcast", 9999, podcast_body_data) is None
        assert audio_file_service.add_audio_file("audiobook", 9999, audiobook_body_data) is None


    def test_get_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        files = {"_id": 45, 'something':'a'}
        persistence_gateway.get = MagicMock(return_value=files)
        for audio_file_type in audio_file_types:
            actual_files = audio_file_service.get_file(audio_file_type, 45)
            call_args = persistence_gateway.get.call_args.args
            assert actual_files == files
            assert call_args[0] == (audio_file_type)


    def test_delete_file(self):
        song_body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        podcast_body_data = {'name': 'gh',
                             'duration': 45,
                             'uploaded_time': 1234,
                             'host': 'abced',
                             "participants": ["ac", "ca"]}
        audiobook_body_data = {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78, "uploaded_time": 34}
        audio_file_types = ["song", "audiobook", "podcast"]
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        persistence_gateway.delete = MagicMock(return_value=None)
        for audio_file_type in audio_file_types:
            assert audio_file_service.delete_file(audio_file_type, 45) is None
            call_args = persistence_gateway.delete.call_args.args
            assert call_args[0] == (audio_file_type)



    def test_get_files(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        database_uri = "mongodb_uri"
        mongo_client = MongoClient(database_uri)
        persistence_gateway = PersistenceGateway(mongo_client)
        audio_file_service = AudioFileService(persistence_gateway)
        files = [{"_id": 45, 'something':'a'}, {"_id": 46, 'something': 'b'}]
        persistence_gateway.get_all = MagicMock(return_value=files)
        for audio_file_type in audio_file_types:
            actual_files = audio_file_service.get_files(audio_file_type)
            call_args = persistence_gateway.get_all.call_args.args
            assert actual_files == files
            assert call_args[0] == (audio_file_type)





