from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI SDR Voice App is live on Render!"

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello! This is your AI SDR. Please leave your message after the tone.", voice='alice')
    response.record(max_length=30, timeout=5)
    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
