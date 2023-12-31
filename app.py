from flask import Flask, request, jsonify
# from flask_cors import CORS
from dashboard import dashboard
from chatbot import DialoGPT

app = Flask(__name__)
# cors = CORS(app)
app.register_blueprint(dashboard, url_prefix="/dashboard")

datajson = None

@app.route("/receiver", methods=["POST"])
def postME():
    global datajson
    data = request.get_json()
    data = jsonify(data)
    datajson = data.json
    return data.json


@app.route("/return", methods =["GET"])
def getJSON():
    global datajson
    datajson = DialoGPT.user_generate(datajson)
    print(datajson[1])
    return datajson[1]

if __name__== '__main__':
    app.run(debug=True,port = 8000)