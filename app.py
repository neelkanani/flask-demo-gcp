from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite DB for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Read - Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'message': 'User fetched successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
