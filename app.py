from flask import Flask
app = Flask(__name__)


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def join_room(audio_file_type, audio_file_id):
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
