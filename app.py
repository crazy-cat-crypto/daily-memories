from flask import Flask
app=Flask(__name__)


@app.route("/")
def receive_email():
    return "Hello! This is the email receiver endpoint."