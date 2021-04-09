from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


class User(db.Document):
    ID = db.StringField()
    audio_file_type = db.StringField()
    name = db.StringField()
    duration = db.StringField()
    uploaded_time = db.StringField()

    def to_json(self):
        return {"name": self.name,
                "duration": self.duration,
                "uploaded_time": self.uploaded_time}




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
    user = User(ID=str(audio_file_id),
                audio_file_type="SONG",
                name=r.name,
                duration=r.duration,
                uploaded_time=r.uploaded_time)
    user.save()
    return jsonify(user.to_json())
    #return "ddd"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
