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
             4)
        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])
