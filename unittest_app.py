import unittest
from unittest.mock import MagicMock
from app import app
import json

class AppTests(unittest.TestCase):
    def test_successful_creation_song(self):
        app.service.add_audio_file = MagicMock(return_value=None)
        tester = app.test_client(self)
        response = tester.post("/song/83662", json={
            'name': 'b', 'duration': 4, 'uploaded_time': 'b'
        })
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == "Record added"
        app.service.add_audio_file.assert_called_once()
        last_call_detail = app.service.add_audio_file.call_args
        assert last_call_detail.args[2] == {'name': 'b', 'duration': 4, 'uploaded_time': 'b'}
        assert last_call_detail.args[0] == "song"
        assert last_call_detail.args[1] == 83662


    def test_successful_creation_podcast(self):
        app.service.add_audio_file = MagicMock(return_value=None)
        tester = app.test_client(self)
        response = tester.post("/podcast/662", json={
            'name': 'gh',
            'duration': 45,
            'uploaded_time': 1234,
            'host': 'abced',
            "participants": ["ac", "ca"]
        })
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == "Record added"
        app.service.add_audio_file.assert_called_once()
        last_call_detail = app.service.add_audio_file.call_args
        assert last_call_detail.args[2] == {'name': 'gh',
                                            'duration': 45,
                                            'uploaded_time': 1234,
                                            'host': 'abced',
                                            "participants": ["ac", "ca"],
                                            }
        assert last_call_detail.args[0] == "podcast"
        assert last_call_detail.args[1] == 662

    def test_successful_creation_audiobook(self):
        app.service.add_audio_file = MagicMock(return_value=None)
        tester = app.test_client(self)
        response = tester.post("/audiobook/66", json={"title": "aaa",
                                                      "author": 45,
                                                      "narrator": 1234,
                                                      "duration": 78,
                                                      "uploaded_time": 34})
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == "Record added"
        app.service.add_audio_file.assert_called_once()
        last_call_detail = app.service.add_audio_file.call_args
        assert last_call_detail.args[2] == {"title": "aaa",
                                            "author": 45,
                                            "narrator": 1234,
                                            "duration": 78,
                                            "uploaded_time": 34}
        assert last_call_detail.args[0] == "audiobook"
        assert last_call_detail.args[1] == 66

    def test_successful_retrieval_song(self):
        app.service.get_file = MagicMock(return_value={'name': 'b', 'duration': 4, 'uploaded_time': 'b'})
        tester = app.test_client(self)
        response = tester.get("/song/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == {"duration": 4, "name": "b", "uploaded_time": "b"}
        last_call_detail = app.service.get_file.call_args
        assert last_call_detail.args[0] == "song"
        app.service.get_file.assert_called_once()
        assert last_call_detail.args[1] == 66


    def test_successful_retrieval_podcast(self):
        body_data = {'name': 'gh', 'duration': 45,'uploaded_time': 1234, 'host': 'abced', "participants": ["ac", "ca"]}
        app.service.get_file = MagicMock(return_value=body_data)
        tester = app.test_client(self)
        response = tester.get("/podcast/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == body_data
        last_call_detail = app.service.get_file.call_args
        assert last_call_detail.args[0] == "podcast"
        app.service.get_file.assert_called_once()
        assert last_call_detail.args[1] == 66

    def test_successful_retrieval_audiobook(self):
        body_data = {"title": "aaa", "author":45, "narrator":1234, "duration":78, "uploaded_time":34}
        app.service.get_file = MagicMock(return_value=body_data)
        tester = app.test_client(self)
        response = tester.get("/audiobook/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == body_data
        last_call_detail = app.service.get_file.call_args
        assert last_call_detail.args[0] == "audiobook"
        app.service.get_file.assert_called_once()
        assert last_call_detail.args[1] == 66

    def test_successful_deletion_song(self):
        app.service.delete_file = MagicMock(return_value={'name': 'b', 'duration': 4, 'uploaded_time': 'b'})
        tester = app.test_client(self)
        response = tester.delete("/song/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == {"duration": 4, "name": "b", "uploaded_time": "b"}
        last_call_detail = app.service.delete_file.call_args
        assert last_call_detail.args[0] == "song"
        app.service.delete_file.assert_called_once()
        assert last_call_detail.args[1] == 66







