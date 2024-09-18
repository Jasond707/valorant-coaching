from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
