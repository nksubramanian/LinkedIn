from flask import Flask, request
from audio_service import AudioService, UserInputError

app = Flask(__name__)
app.service = AudioService()


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def create_audio_file(audio_file_type, audio_file_id):
    try:
        app.service.add_audio_file(audio_file_type, audio_file_id, request.get_json())
        return "Record added"
    except UserInputError as error:
        return error.args[0], 400


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['GET'])
def get_audio_file(audio_file_type, audio_file_id):
    try:
        x = app.service.get_file(audio_file_type, audio_file_id)
        return x
    except UserInputError as error:
        return error.args[0], 400


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['DELETE'])
def delete_audio_file(audio_file_type, audio_file_id):
    try:
        return app.service.delete_file(audio_file_type, audio_file_id)
    except UserInputError as error:
        return error.args[0], 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
