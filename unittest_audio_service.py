import unittest
from unittest.mock import MagicMock
from audio_service import AudioService
from audio_service import UserInputError

l = [
    ("song", "Name of the song is mandatory", {'namea': 'gh','duration': 45, 'uploaded_time': 1234}),
    ("song", "duration has to be integer", {'name': 'gh', 'duration': 'g45', 'uploaded_time': 1234}),
     ]

class AudioServiceTests(unittest.TestCase):
    def test_add_validation(self):
        global l
        for t in l:
            audioservice = AudioService()
            audioservice.database.add_song = MagicMock(return_value=None)
            audioservice.database.add_podcast = MagicMock(return_value=None)
            audioservice.database.add_audiobook = MagicMock(return_value=None)
            try:
                audioservice.add_audio_file(t[0], 3333, t[2])
                exception_thrown = False
            except UserInputError as error:
                print(error.args[0])
                assert error.args[0] == t[1]
                exception_thrown = True
            assert exception_thrown is True








    def test_add_audio_file(self):
        song_body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        podcast_body_data = {'name': 'gh',
                             'duration': 45,
                             'uploaded_time': 1234,
                             'host': 'abced',
                             "participants": ["ac", "ca"]}
        audiobook_body_data = {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78, "uploaded_time": 34}
        audioservice = AudioService()
        audioservice.database.add_song = MagicMock(return_value=None)
        audioservice.database.add_podcast = MagicMock(return_value=None)
        audioservice.database.add_audiobook = MagicMock(return_value=None)
        assert audioservice.add_audio_file("song", 9999, song_body_data) is None
        assert audioservice.add_audio_file("podcast", 9999, podcast_body_data) is None
        assert audioservice.add_audio_file("audiobook", 9999, audiobook_body_data) is None


    def test_get_file(self):
        song_body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        podcast_body_data = {'name': 'gh',
                             'duration': 45,
                             'uploaded_time': 1234,
                             'host': 'abced',
                             "participants": ["ac", "ca"]}
        audiobook_body_data = {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78, "uploaded_time": 34}
        audioservice = AudioService()
        audioservice.database.get_song = MagicMock(return_value=song_body_data)
        audioservice.database.get_podcast = MagicMock(return_value=podcast_body_data)
        audioservice.database.get_audiobook = MagicMock(return_value=audiobook_body_data )
        assert audioservice.get_file("song", 9999) == song_body_data
        assert audioservice.get_file("podcast", 9999) == podcast_body_data
        assert audioservice.get_file("audiobook", 9999) == audiobook_body_data


    def test_delete_file(self):
        song_body_data = {'name': 'b', 'duration': 4, 'uploaded_time': 'b', 'date':'wef'}
        podcast_body_data = {'name': 'gh',
                             'duration': 45,
                             'uploaded_time': 1234,
                             'host': 'abced',
                             "participants": ["ac", "ca"]}
        audiobook_body_data = {"title": "aaa", "author": "ds", "narrator": "ds", "duration": 78, "uploaded_time": 34}
        audioservice = AudioService()
        audioservice.database.delete_song = MagicMock(return_value=song_body_data)
        audioservice.database.delete_podcast = MagicMock(return_value=podcast_body_data)
        audioservice.database.delete_audiobook = MagicMock(return_value=audiobook_body_data )
        assert audioservice.delete_file("song", 9999) == song_body_data
        assert audioservice.delete_file("podcast", 9999) == podcast_body_data
        assert audioservice.delete_file("audiobook", 9999) == audiobook_body_data


