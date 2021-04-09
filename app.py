from flask import Flask, request

app = Flask(__name__)


class Request:
    def __init__(self, dictionary):
        self.__dict__ = dictionary


@app.route("/<string:audio_file_type>/<int:audio_file_id>", methods=['POST'])
def join_room(audio_file_type, audio_file_id):
    print(audio_file_type)
    print(audio_file_id)
    r = Request(request.get_json())
    print(r.name)
    print(r.duration)
    print(r.uploaded_time)
    return "ddd"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
