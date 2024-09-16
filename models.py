from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discord_name = db.Column(db.String(100), nullable=False)
    tracker_link = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return (f"Submission(id={self.id}, discord_name='{self.discord_name}', "
                f"tracker_link='{self.tracker_link}', message='{self.message}')")
