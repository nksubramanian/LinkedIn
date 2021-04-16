import unittest
from unittest.mock import MagicMock

from pymongo.errors import DuplicateKeyError

from business_errors import UserInputError
from persistance_gateway import UnableToInsertDueToDuplicateKeyError, ItemNotFound
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

    def test_add_audio_file_extra_parameters_are_not_persisted(self):
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
            creation_data = dict(test[2])
            creation_data['extra_field'] = "extra"
            assert self.service.add_audio_file(test[0], test[1], creation_data) is None
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
            assert call_args[0] == audio_file_type
            assert call_args[1] == 45

    def test_delete_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        for audio_file_type in audio_file_types:
            self.gateway.delete = MagicMock(return_value=None)
            assert self.service.delete_file(audio_file_type, 45) is None
            call_args = self.gateway.delete.call_args.args
            assert call_args[0] == audio_file_type
            assert call_args[1] == 45

    def test_get_files(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        files = [{"id": 45, 'something': 'a'}, {"id": 46, 'something': 'b'}]
        for audio_file_type in audio_file_types:
            self.gateway.get_all = MagicMock(return_value=files)
            actual_files = self.service.get_files(audio_file_type)
            call_args = self.gateway.get_all.call_args.args
            assert actual_files == files
            assert call_args[0] == audio_file_type

    def test_update_audio_file(self):
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
            self.gateway.update = MagicMock(return_value=None)
            assert self.service.update_audio_file(test[0], test[1], test[2]) is None
            args = self.gateway.update.call_args.args
            assert args[0] == test[0]
            assert args[1] == test[1]
            assert args[2] == test[2]

    def test_invalid_audio_type_get_files(self):
        with self.assertRaises(UserInputError):
            self.service.get_files("invalid file type")

    def test_invalid_audio_type_add_file(self):
        with self.assertRaises(UserInputError):
            self.service.add_audio_file("invalid file type", 34, {'s': 's'})

    def test_invalid_audio_type_delete_file(self):
        with self.assertRaises(UserInputError):
            self.service.delete_file("invalid file type", 34)

    def test_invalid_audio_type_update_file(self):
        with self.assertRaises(UserInputError):
            self.service.update_audio_file("invalid file type", 34, {'s': 's'})

    def test_invalid_audio_type_get_file(self):
        with self.assertRaises(UserInputError):
            self.service.get_file("invalid file type", 34)

    def test_duplicate_add_audio_file(self):
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
            self.gateway.add = MagicMock(side_effect=UnableToInsertDueToDuplicateKeyError)
            with self.assertRaises(UserInputError):
                self.service.add_audio_file(test[0], test[1], test[2])
            args = self.gateway.add.call_args.args
            assert args[0] == test[0]
            assert args[1] == test[1]
            assert args[2] == test[2]

    def test_get_invalid_audio_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        files = {"id": 45, 'something': 'a'}
        self.gateway.get = MagicMock(side_effect=ItemNotFound)
        for audio_file_type in audio_file_types:
            with self.assertRaises(UserInputError):
                self.service.get_file(audio_file_type, 45)
            call_args = self.gateway.get.call_args.args
            assert call_args[0] == audio_file_type
            assert call_args[1] == 45

    def test_delete_invalid_file(self):
        audio_file_types = ["song", "audiobook", "podcast"]
        for audio_file_type in audio_file_types:
            self.gateway.delete = MagicMock(side_effect=ItemNotFound)
            with self.assertRaises(UserInputError):
                self.service.delete_file(audio_file_type, 45)
            call_args = self.gateway.delete.call_args.args
            assert call_args[0] == audio_file_type
            assert call_args[1] == 45
