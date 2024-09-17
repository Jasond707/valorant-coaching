from flask import Flask, request, render_template, redirect, url_for
from config import Config
from models import db, Submission
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the app with the SQLAlchemy database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

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

# Handle errors globally
@app.errorhandler(500)
def internal_error(error):
    return "500 Error - Internal Server Error", 500

@app.errorhandler(404)
def not_found_error(error):
    return "404 Error - Page Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

