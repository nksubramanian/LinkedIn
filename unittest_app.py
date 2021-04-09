import unittest
from unittest.mock import MagicMock
from app import app


class AppTests(unittest.TestCase):
    def test_successful_creation(self):
        app.service.add_audio_file = MagicMock(return_value=None)
        tester = app.test_client(self)
        response = tester.post("/song/11111333")
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == ""
        ##assert called with the correct parameter