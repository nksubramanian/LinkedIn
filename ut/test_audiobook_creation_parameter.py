import unittest

from business_errors import UserInputError
from ut.audio_service_test_base import AudioServiceTestBase


class AudioBookCreationParameterTests(unittest.TestCase, AudioServiceTestBase):
    def setUp(self):
        (service, gateway) = self.create_service_and_gateway()
        self.service = service
        self.gateway = gateway

    def get_tests(self):
        return [
            ("audiobook",
             "Title is mandatory",
             {"title1": "aaa", "author": "ssss", "narrator":"1234", "duration": 78, "uploaded_time":"2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Title cannot be greater than 100 characters",
             {"title": "aaa"*35, "author": "ssss", "narrator": "1234", "duration": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Author is mandatory",
             {"title": "aaa", "author1": "ssss", "narrator": "1234", "duration": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Author cannot be greater than 100 characters",
             {"title": "aaa", "author": "ssss"*30, "narrator": "1234", "duration": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Narrator is mandatory",
             {"title": "aaa", "author": "ssss", "narrator1": "abcdef", "duration": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Narrator cannot be greater than 100 characters",
             {"title": "aaa", "author": "ssss", "narrator": "1234"*30, "duration": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "Duration of the song is mandatory",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration1": 78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "duration has to be integer",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration": "a",
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "duration has to be a positive integer",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration": -78,
              "uploaded_time": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "uploaded_time is mandatory",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration": 78,
              "uploaded_time1": "2034-06-01 01:10:20"},
             4),
            ("audiobook",
             "uploaded_time needs to be in string format ex.2034-06-01 01:10:20",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration": 78,
              "uploaded_time": [1,2,3]},
             4),
            ("audiobook",
             "uploaded_time cannot be in the past",
             {"title": "aaa", "author": "ssss", "narrator": "1234", "duration": 78,
              "uploaded_time": "2014-06-01 01:10:20"},
             4)

        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])