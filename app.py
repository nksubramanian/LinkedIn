from flask import Flask, request
from audio_service import AudioService

app = Flask(__name__)
app.service = AudioService()


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def create_audio_file(audio_file_type, audio_file_id):
    app.service.add_audio_file(audio_file_type, audio_file_id, request.get_json())
    return ""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
