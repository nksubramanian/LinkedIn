from flask import Flask, request
from business_errors import UserInputError

app = Flask(__name__)


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def create_audio_file(audio_file_type, audio_file_id):
    try:
        app.service.add_audio_file(audio_file_type, audio_file_id, request.get_json())
        return ""
    except UserInputError as error:
        return error.args[0], 400
    except Exception as error:
        return error.args[0], 500


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['GET'])
def get_audio_file(audio_file_type, audio_file_id):
    try:
        x = app.service.get_file(audio_file_type, audio_file_id)
        return x
    except UserInputError as error:
        return error.args[0], 400
    except Exception as error:
        return error.args[0], 500


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['DELETE'])
def delete_audio_file(audio_file_type, audio_file_id):
    try:
        app.service.delete_file(audio_file_type, audio_file_id)
        return ""
    except UserInputError as error:
        return error.args[0], 400
    except Exception as error:
        return error.args[0], 500
