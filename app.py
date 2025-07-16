from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "AI SDR Voice App is live on Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT env var
    app.run(host="0.0.0.0", port=port)
