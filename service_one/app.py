from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def app_root():
    return jsonify(message="Welcome to service 1", status="ok")