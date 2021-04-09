from flask import Flask, request
from audio_service import AudioService

app = Flask(__name__)

audio_service = AudioService()


class Request:
    def __init__(self, dictionary):
        self.__dict__ = dictionary


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def join_room(audio_file_type, audio_file_id):
    audio_service.add_song(audio_file_id, request.get_json())
    return "ddd"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
