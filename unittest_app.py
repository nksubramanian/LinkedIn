import unittest
from unittest.mock import MagicMock
import unittest_helper
import business_errors
from app import app
from audio_service import AudioFileService


class AppTests(unittest.TestCase):
    def test_creation_with_user_exception(self):
        scenarios = ["song", "podcast", "audiobook"]
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b'}
        error_message = "SomeError"
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.add_audio_file = MagicMock(side_effect=business_errors.UserInputError(error_message))
            tester = app.test_client(self)
            response = tester.post(f"/{scenario}/83662", json=body_data)
            res_message = response.stream.response.data.decode("UTF-8")
            assert res_message == error_message, unittest_helper.assert_message(scenario, error_message, res_message)
            assert response.status_code == 400, unittest_helper.assert_message(scenario, 400, response.status_code)
            self.assert_method_called_once_with_params(self, app.service.add_audio_file, (scenario, 83662, body_data))

    def test_creation_with_system_exception(self):
        scenarios = ["song", "podcast", "audiobook"]
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b'}
        error_message = "SomeError"
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.add_audio_file = MagicMock(side_effect=Exception(error_message))
            tester = app.test_client(self)
            response = tester.post(f"/{scenario}/83662", json=body_data)
            res_message = response.stream.response.data.decode("UTF-8")
            assert res_message == error_message, unittest_helper.assert_message(scenario, error_message, res_message)
            assert response.status_code == 500, unittest_helper.assert_message(scenario, 500, response.status_code)
            self.assert_method_called_once_with_params(self, app.service.add_audio_file, (scenario, 83662, body_data))

    def test_successful_creation(self):
        scenarios = ["song", "podcast", "audiobook"]
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b'}
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.add_audio_file = MagicMock(return_value=None)
            tester = app.test_client(self)
            response = tester.post(f"/{scenario}/83662", json = body_data)
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == ""
            assert response.status_code == 200
            self.assert_method_called_once_with_params(self, app.service.add_audio_file, (scenario, 83662, body_data))

    def test_get_with_user_error(self):
        scenarios = ["song", "podcast", "audiobook"]
        error_message = "SomeError"
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.add_audio_file = MagicMock(side_effect=business_errors.UserInputError(error_message))
            tester = app.test_client(self)
            response = tester.post(f"/{scenario}/83662")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == error_message
            assert response.status_code == 400

    def test_get_with_system_error(self):
        scenarios = ["song", "podcast", "audiobook"]
        error_message = "SomeError"
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.add_audio_file = MagicMock(side_effect=Exception(error_message))
            tester = app.test_client(self)
            response = tester.post(f"/{scenario}/83662")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == error_message
            assert response.status_code == 500

    def test_successful_get(self):
        scenarios = ["song", "podcast", "audiobook"]
        body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b'}
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.get_file = MagicMock(return_value=body_data)
            tester = app.test_client(self)
            response = tester.get(f"/{scenario}/66")
            response_message = response.stream.response.data.decode("UTF-8")
            assert eval(response_message) == body_data
            assert response.status_code == 200
            self.assert_method_called_once_with_params(self, app.service.get_file, (scenario, 66))

    def test_unsuccesful_deletion(self):
        error_message = "SomeError"
        app.service.add_audio_file = MagicMock(side_effect=business_errors.UserInputError(error_message))
        tester = app.test_client(self)
        response = tester.post("/song/83662")
        response_message = response.stream.response.data.decode("UTF-8")
        assert response_message == error_message
        assert response.status_code == 400

    def test_successful_retrieval_podcast(self):
        body_data = {'name': 'gh', 'duration': 45,'uploaded_time': 1234, 'host': 'abced', "participants": ["ac", "ca"]}
        app.service.get_file = MagicMock(return_value=body_data)
        tester = app.test_client(self)
        response = tester.get("/podcast/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == body_data
        assert response.status_code == 200
        self.assert_method_called_once_with_params(self, app.service.get_file, ("podcast", 66))


    def test_successful_retrieval_audiobook(self):
        body_data = {"title": "aaa", "author":45, "narrator":1234, "duration":78, "uploaded_time":34}
        app.service.get_file = MagicMock(return_value=body_data)
        tester = app.test_client(self)
        response = tester.get("/audiobook/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == body_data
        assert response.status_code == 200
        self.assert_method_called_once_with_params(self, app.service.get_file, ("audiobook", 66))

    def test_successful_deletion_song(self):
        app.service.delete_file = MagicMock(return_value={'name': 'b', 'duration': 4, 'uploaded_time': 'b'})
        tester = app.test_client(self)
        response = tester.delete("/song/66")
        response_message = response.stream.response.data.decode("UTF-8")
        assert eval(response_message) == {"duration": 4, "name": "b", "uploaded_time": "b"}
        assert response.status_code == 200
        self.assert_method_called_once_with_params(self, app.service.delete_file, ("song", 66))

    @staticmethod
    def assert_method_called_once_with_params(self, method, expected_params):
        method.assert_called_once()
        call_args = method.call_args.args
        self.assert_are_same(call_args, expected_params)

    @staticmethod
    def assert_are_same(actual_params, expected_params):
        for i in range(0, len(actual_params)):
            assert actual_params[i] == expected_params[i], f"Expected={actual_params} Actual={expected_params}"
        assert len(actual_params) == len(expected_params), f"Expected={actual_params} Actual={expected_params}"






