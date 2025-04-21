from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def time_service():
    timestamp = datetime.utcnow().isoformat() + "Z"
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    response_data = {
        "timestamp": timestamp,
        "ip": ip
    }

    return Response(
        response=json.dumps(response_data),
        mimetype='application/json'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
