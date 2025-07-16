from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.play("https://drive.google.com/uc?export=download&id=1oXnHg7dLy-2DkKC80GyoMtcL79JTcpLy")
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
