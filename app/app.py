from flask import Flask
import socket, os

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "status": "ok",
        "host": socket.gethostname(),
        "env": os.getenv("ENV", "dev")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
