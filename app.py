from flask import Flask,request,jsonify
app=Flask(__name__)


@app.route("/cache-email", methods=["POST"])
def home():
    email_data = request.get_json()
    email_from= email_data.get("from")
    email_subject= email_data.get("subject")
    email_body= email_data.get("body")
    print(f"Received email from: {email_from}, with subject: {email_subject}, and body: {email_body}")
    return jsonify({"message": "Email received successfully!"}), 200

@app.route("/", methods=["GET"])
def index():

    return "Hello! This is the email receiver endpoint."
