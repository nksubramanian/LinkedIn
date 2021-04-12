import unittest
from unittest.mock import MagicMock
from app import app


class AppTests(unittest.TestCase):
    def test_successful_creation(self):
        app.service.add_audio_file = MagicMock(return_value=None)
        tester = app.test_client(self)
        response = tester.post("/song/83662")
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == "Record added"
        app.service.add_audio_file.assert_called_once()
        last_call_detail = app.service.add_audio_file.call_args
        assert last_call_detail.args[0] == "song"
        assert last_call_detail.args[1] == 83662


