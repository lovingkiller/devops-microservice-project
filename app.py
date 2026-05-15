from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route('/')
def home():
    #Environment variable check which we will sent from kubernetes/jenkins
    env_name = os.getenv("APP_ENV", "Local-Dev")
    return jsonify({
        "message": "Welcome to my DevOps Microservice!",
        "status": "Success",
        "environment": env_name
    })

if __name__ == '__main__':
    # 0.0.0.0 this means it will be accessable from outside container
    app.run(host='0.0.0.0', port=5000)