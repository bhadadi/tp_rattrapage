from flask import Flask
from flask_cors import CORS
from bookings_controller import bookings_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(bookings_bp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)