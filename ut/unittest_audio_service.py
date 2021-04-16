import unittest
from unittest.mock import MagicMock

from mongomock import MongoClient

from audio_service import AudioFileService
from persistance_gateway import PersistenceGateway
from ut.audio_service_test_base import AudioServiceTestBase


class AudioServiceTests(unittest.TestCase, AudioServiceTestBase):
    def setUp(self):
        (service, gateway) = self.create_service_and_gateway()
        self.service = service
        self.gateway = gateway

    def test_add_audio_file(self):
        tests = [
            ("song", 999, {'name': 'b', 'duration': 4, 'uploaded_time': '2031-04-14 14:41:32'}),
            ("podcast", 999, {'name': 'gh',
                              'duration': 45,
                              'uploaded_time': '2031-04-14 14:41:32',
                              'host': 'abced',
                              "participants": ["ac", "ca"]}),
            ("audiobook", 999, {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78,
                                "uploaded_time": '2031-04-14 14:41:32'})
        ]

        for test in tests:
            self.gateway.add = MagicMock(return_value=None)
            assert self.service.add_audio_file(test[0], test[1], test[2]) is None
            args = self.gateway.add.call_args.args
            assert args[0] == test[0]
            assert args[1] == test[1]
            assert args[2] == test[2]

    def test_get_audio_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        files = {"id": 45, 'something': 'a'}
        self.gateway.get = MagicMock(return_value=files)
        for audio_file_type in audio_file_types:
            actual_files = self.service.get_file(audio_file_type, 45)
            call_args = self.gateway.get.call_args.args
            assert actual_files == files
            print(files)
            print(actual_files)
            assert call_args[0] == audio_file_type

    def test_delete_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        self.gateway.delete = MagicMock(return_value=None)
        for audio_file_type in audio_file_types:
            assert self.service.delete_file(audio_file_type, 45) is None
            call_args = self.gateway.delete.call_args.args
            assert call_args[0] == (audio_file_type)

    def test_get_files(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        files = [{"_id": 45, 'something': 'a'}, {"_id": 46, 'something': 'b'}]
        self.gateway.get_all = MagicMock(return_value=files)
        for audio_file_type in audio_file_types:
            actual_files = self.service.get_files(audio_file_type)
            call_args = self.gateway.get_all.call_args.args
            assert actual_files == files
            assert call_args[0] == (audio_file_type)
