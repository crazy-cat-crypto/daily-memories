from flask import Flask,request,jsonify,session, redirect, url_for,abort,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os,pytz
from dotenv import load_dotenv
app=Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_from = db.Column(db.String(120), nullable=False)
    email_subject = db.Column(db.String(255), nullable=False)
    email_body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Kathmandu')))



with app.app_context():
    db.create_all()

@app.route("/cache-email", methods=["POST"])
def home():
    email_data = request.get_json()
    email_from= email_data.get("from")
    email_subject= email_data.get("subject")
    email_body= email_data.get("body")
    print(f"Received email from: {email_from}, with subject: {email_subject}, and body: {email_body}")
    return jsonify({"message": "Email received successfully!"}), 200

@app.route("/", methods=["GET"])
def home():

    return render_template("index.html")