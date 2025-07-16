from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.play("https://ai-sdr-assets-4608.twil.io/voice_preview_british%20sdr.mp3")
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
