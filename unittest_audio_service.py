import unittest
from unittest.mock import MagicMock
from audio_service import AudioService



class AudioServiceTests(unittest.TestCase):
    def test_add_audio_file(self):
        audioservice = AudioService()
        audioservice.database.add_song = MagicMock(return_value=None)
        audioservice.add_audio_file("SONG", 9999, {"name": "s", "duration": 4, "uploaded_time": "b"})
        # assert a database method is called
        print(audioservice.get_file("SONG", 9999))
        assert audioservice.get_file("SONG", 9999) == {"name": "s", "duration": 4, "uploaded_time": "b"}

