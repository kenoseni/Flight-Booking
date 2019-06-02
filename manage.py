"""Module to run the app"""
from flask_restplus import Resource
from main import create_app
from app import api
from config import app_config

app = create_app(app_config)


@app.route("/")
def get():
    """Returns a welcome message"""
    return "Welcome to the Flight Booking API"

if __name__ == "__main__":
    app.run()
