from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

import logging


logging.basicConfig(level=logging.INFO)


REQUEST_COUNT = Counter('app_request_total','Total number of requests')


@app.routr("/")
def home():
    REQUEST_COUNT.inc()
    logging.info("Home endpoint was called")
     return jsonify({"message": "Flask DevOps App Running 🚀"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)