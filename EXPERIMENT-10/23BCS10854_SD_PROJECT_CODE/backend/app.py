from flask import Flask, request, jsonify
from models import Notification
from database import db, init_db

app = Flask(__name__)
init_db(app)

@app.route('/send', methods=['POST'])
def send_notification():
    data = request.json
    notif = Notification(message=data['message'], user=data['user'])
    db.session.add(notif)
    db.session.commit()
    return jsonify({'status': 'Notification sent'})

@app.route('/notifications', methods=['GET'])
def get_notifications():
    notifs = Notification.query.all()
    return jsonify([n.to_dict() for n in notifs])

if __name__ == '__main__':
    app.run(debug=True)
