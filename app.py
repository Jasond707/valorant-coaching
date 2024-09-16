from flask import Flask, request, render_template, redirect, url_for
from config import Config
from models import db, Submission  # Import models

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the app with the SQLAlchemy database
db.init_app(app)

# Ensure the database tables are created when the app starts
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')  # Your form page

@app.route('/submit', methods=['POST'])
def submit():
    discord_name = request.form.get('discord')
    tracker_link = request.form.get('tracker')
    message = request.form.get('message')
    clips = request.files.getlist('clips')

    # Save the uploaded clips
    for clip in clips:
        if clip:
            clip.save(f"uploads/{clip.filename}")

    # Save form data to the database
    new_submission = Submission(discord_name=discord_name, tracker_link=tracker_link, message=message)
    db.session.add(new_submission)
    db.session.commit()

    # Print form data to console (for debugging)
    print(f"Discord Name: {discord_name}")
    print(f"Tracker Link: {tracker_link}")
    print(f"Message: {message}")

    # Redirect to confirmation page
    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')  # Your confirmation page

if __name__ == '__main__':
    app.run(debug=True)
