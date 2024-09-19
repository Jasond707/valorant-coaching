from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the app to use the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Submission model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discord_name = db.Column(db.String(100), nullable=False)
    tracker_link = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

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

        # Print form data to console for debugging
        print(f"Discord Name: {discord_name}")
        print(f"Tracker Link: {tracker_link}")
        print(f"Message: {message}")

        # Create a new Submission object
        new_submission = Submission(
            discord_name=discord_name,
            tracker_link=tracker_link,
            message=message
        )

        # Add the new submission to the database
        db.session.add(new_submission)
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

