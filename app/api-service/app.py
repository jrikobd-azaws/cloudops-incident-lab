from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

log_dir = "/var/log/voice-api"
log_file = os.path.join(log_dir, "app.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@app.route("/")
def home():
    logger.info("Root endpoint accessed")
    return jsonify({
        "service": "voice-api",
        "status": "running",
        "message": "CloudOps Incident Lab API"
    })

@app.route("/health")
def health():
    logger.info("Health endpoint checked")
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/simulate-error")
def simulate_error():
    logger.warning("Simulated application error triggered")
    return jsonify({
        "status": "error",
        "message": "Simulated failure for testing"
    }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
