import unittest
from unittest.mock import MagicMock
from audio_service import AudioService


class AudioServiceTests(unittest.TestCase):
    def test_add_audio_file(self):
        audioservice = AudioService()
        audioservice.database.add_song = MagicMock(return_value=None)
        audioservice.add_audio_file("SONG", 1234, {"name": "s"})
        # assert a database method is called
