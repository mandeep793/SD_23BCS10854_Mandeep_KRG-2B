from database import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200))
    user = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'user': self.user
        }
