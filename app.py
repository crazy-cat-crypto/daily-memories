from flask import Flask,request,jsonify
app=Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        email_data = request.get_json()
        email_form= email_data.get("form")
        email_subject= email_data.get("subject")
        email_body= email_data.get("body")
        print(f"Received email from: {email_form}, with subject: {email_subject}, and body: {email_body}")
        return jsonify({"message": "Email received successfully!"}), 200
    return "Hello! This is the email receiver endpoint."