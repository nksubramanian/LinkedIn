import unittest

from business_errors import UserInputError
from ut.audio_service_test_base import AudioServiceTestBase


class PodcastCreationParameterTests(unittest.TestCase, AudioServiceTestBase):
    def setUp(self):
        (service, gateway) = self.create_service_and_gateway()
        self.service = service
        self.gateway = gateway

    def get_tests(self):
        return[
            ("podcast",
             "Name of the podcast is mandatory",
             {"namea": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Name of the podcast is mandatory",
             {"name": "", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Name of the podcast is mandatory",
             {"name": "  ", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Name of the podcast is mandatory",
             {"name": "", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Name has to be a string",
             {"name": 34, "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Name cannot be greater than 100 characters",
             {"name": "abcde"*21, "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Duration of the song is mandatory",
             {"name": "aaa", "duration1": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "duration has to be integer",
             {"name": "aaa", "duration": "fg", "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "duration has to be a positive integer",
             {"name": "aaa", "duration": -45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "uploaded_time is mandatory",
             {"name": "aaa", "duration": 45, "uploaded_time1": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "uploaded_time needs to be in string format ex.2034-06-01 01:10:20",
             {"name": "aaa", "duration": 45, "uploaded_time": [1,2], "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "uploaded_time cannot be in the past",
             {"name": "aaa", "duration": 45, "uploaded_time": "2014-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Host is mandatory",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host1": "abcdefgh",
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Host cannot be greater than 100 characters",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh"*23,
              "participants": ["ac", "ca"]},
             4),
            ("podcast",
             "Host has to be a string",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": 34},
             4),
            ("podcast",
             "Host has to be a string",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": 34,
              "participants": {"ac", "ca"}},
             4),
            ("podcast",
             "participants has to be a list",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"}},
             4),
            ("podcast",
             "participants can have maximum of 10 members",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["1",  "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]},
             4),
            ("podcast",
             "Each member of the participant has to be string",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": [1, "ca"]},
             4),
            ("podcast",
             "maximum characters allowed for all participants in 100",
             {"name": "aaa", "duration": 45, "uploaded_time": "2034-06-01 01:10:20", "host": "abcdefgh",
              "participants": ["123"*34, "ca"]},
             4)

        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])



