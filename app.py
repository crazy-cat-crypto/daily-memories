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
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(pytz.timezone('Asia/Kathmandu')))

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    entries = db.relationship('Entry', backref='user', lazy=True)


with app.app_context():
    db.create_all()

@app.route("/cache-email", methods=["POST"])
def cache_email():
    email_data = request.get_json()
    email_from= email_data.get("from")
    email_subject= email_data.get("subject")
    email_body= email_data.get("body")
    print(f"Received email from: {email_from}, with subject: {email_subject}, and body: {email_body}")
    user=User.query.filter_by(email=email_from).first()
    if not user:
        user=User(email=email_from,password=os.getenv("DEFAULT_PASSWORD"))
        db.session.add(user)
        db.session.flush()
    new_entry=Entry(user_id=user.id,title=email_subject,body=email_body)
    db.session.add(new_entry)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return jsonify({"message": "Email received successfully!"}), 200

@app.route("/")
def home():
    
    return render_template("home.html")

@app.route("/login",methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route("/signup",methods=["POST","GET"])
def signup():
    return render_template("signup.html")

@app.route("/resetpassword",methods=["POST","GET"])
def reset_password():
    return render_template("reset_password.html")

@app.route("/logout")
def logout():
    pass

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if not "user.id" in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")