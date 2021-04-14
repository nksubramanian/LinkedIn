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
            app.service.get_file = MagicMock(side_effect=business_errors.UserInputError(error_message))
            tester = app.test_client(self)
            response = tester.get(f"/{scenario}/83662")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == error_message
            assert response.status_code == 400

    def test_get_with_system_error(self):
        scenarios = ["song", "podcast", "audiobook"]
        error_message = "SomeError"
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.get_file = MagicMock(side_effect=Exception(error_message))
            tester = app.test_client(self)
            response = tester.get(f"/{scenario}/83662")
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

    def test_unsuccesful_deletion_with_user_error(self):
        error_message = "SomeError"
        scenarios = ["song", "podcast", "audiobook"]
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.delete_file = MagicMock(side_effect=business_errors.UserInputError(error_message))
            tester = app.test_client(self)
            response = tester.delete(f"/{scenario}/83662")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == error_message
            assert response.status_code == 400

    def test_unsuccesful_deletion_with_system_error(self):
        error_message = "SomeError"
        scenarios = ["song", "podcast", "audiobook"]
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.delete_file = MagicMock(side_effect=Exception(error_message))
            tester = app.test_client(self)
            response = tester.delete(f"/{scenario}/83662")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == error_message
            assert response.status_code == 500

    def test_successful_deletion(self):
        scenarios = ["song", "podcast", "audiobook"]
        for scenario in scenarios:
            app.service = AudioFileService(None)
            app.service.delete_file = MagicMock(return_value=None)
            tester = app.test_client(self)
            response = tester.delete(f"/{scenario}/66")
            response_message = response.stream.response.data.decode("UTF-8")
            assert response_message == ""
            assert response.status_code == 200
            self.assert_method_called_once_with_params(self, app.service.delete_file, (scenario, 66))

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






