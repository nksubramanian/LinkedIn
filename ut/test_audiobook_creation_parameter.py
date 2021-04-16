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
             {"title1": "aaa", "author":"ssss", "narrator":"1234", "duration":78, "uploaded_time":"2034-06-01 01:10:20"},
             4)
        ]

    def test_parameter(self):
        for t in self.get_tests():
            with self.assertRaises(UserInputError) as context:
                self.service.add_audio_file(t[0], t[3], t[2])
            self.assertTrue(t[1] == context.exception.args[0])