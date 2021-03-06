import unittest

from business_errors import UserInputError
from ut.audio_service_test_base import AudioServiceTestBase


class SongCreationParameterTests(unittest.TestCase, AudioServiceTestBase):
    def setUp(self):
        (service, gateway) = self.create_service_and_gateway()
        self.service = service
        self.gateway = gateway

    def get_tests(self):
        return [
            ("song",
             "name is mandatory",
             {'name': '', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "name is mandatory",
             {'name': '  ', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "Audio file Id has to be an integer",
             {'name': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             "t"),

            ("song",
             "name is mandatory",
             {'namea': 'gh', 'duration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "name's max length is 100",
             {
                 'name': 'a' * 101,
                 'duration': 45,
                 'uploaded_time': "2034-06-01 01:10:20"
             },
             4),

            ("song",
             "duration is mandatory",
             {'name': 'gh', 'ruration': 45, 'uploaded_time': "2034-06-01 01:10:20"},
             4),

            ("song",
             "duration has to be a integer",
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
             "uploaded_time needs to be in string format ex.2034-06-01 01:10:20",
             {'name': 'gh', 'duration': 45, 'uploaded_time': [2032, 3, 4]},
             4),

            ("song",
             "duration has to be a positive integer",
             {'name': 'gh', 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"},
             4),

            ("song",
             "name has to be a string",
             {'name': 34, 'duration': -45, 'uploaded_time': "2012-06-01 01:10:20"},
             4),

            ("song",
             "uploaded_time needs to be in string format ex.2034-06-01 01:10:20",
             {'name': 'sss', 'duration': 45, 'uploaded_time': "2034-06-01a 01:10:20"},
             4),
        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])
