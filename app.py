from flask import Flask, request, render_template, redirect, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Submission model
class Submission(db.Model):
    __tablename__ = 'submission'
    
    id = db.Column(db.Integer, primary_key=True)
    discord_name = db.Column(db.String(50), nullable=False)  # User's Discord name
    valorant_tracker = db.Column(db.String(255), nullable=True)  # Optional Valorant tracker link
    message = db.Column(db.Text, nullable=True)  # Optional message field
    video_link = db.Column(db.String(255), nullable=True)  # Optional video link
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of submission

    def __repr__(self):
        return f'<Submission {self.discord_name}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        discord_name = request.form.get('discord')
        tracker_link = request.form.get('tracker')
        message = request.form.get('message')
        video_link = request.form.get('video_link')  # Get video link from the form

        # Print form data to console for debugging
        print(f"Discord Name: {discord_name}")
        print(f"Tracker Link: {tracker_link}")
        print(f"Message: {message}")
        print(f"Video Link: {video_link}")  # Print the video link

        # Save form data to the database
        submission = Submission(
            discord_name=discord_name,
            valorant_tracker=tracker_link,
            message=message,
            video_link=video_link  # Save the video link
        )
        db.session.add(submission)
        db.session.commit()

        # Redirect to confirmation page
        return redirect(url_for('confirmation'))
    
    except Exception as e:
        # Print detailed error to the console for debugging
        print(f"Error during form submission: {e}")
        # Return error message with details
        return f"An error occurred during form submission: {e}", 500

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

