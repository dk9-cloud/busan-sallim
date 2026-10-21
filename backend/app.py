
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "부산살림 Flask 서버 정상 작동"
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
