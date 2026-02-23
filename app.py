from flask import Flask,request,jsonify
app=Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        email_data = request.get_json()
        email_from= email_data.get("from")
        email_subject= email_data.get("subject")
        email_body= email_data.get("body")
        print(f"Received email from: {email_from}, with subject: {email_subject}, and body: {email_body}")
        return jsonify({"message": "Email received successfully!"}), 200
    return "Hello! This is the email receiver endpoint."
