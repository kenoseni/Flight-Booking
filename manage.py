"""Module to run the app"""
from main import create_app
from config import app_config

app, jwt = create_app(app_config)


@app.route("/")
def get():
    """Returns a welcome message"""
    return "Welcome to the Flight Booking API"

if __name__ == "__main__":
    app.run()
