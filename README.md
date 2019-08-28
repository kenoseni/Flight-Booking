# Flight-Booking

[![Build Status](https://travis-ci.org/kenoseni/Flight-Booking.svg?branch=develop)](https://travis-ci.org/kenoseni/Flight-Booking)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f74bd32cfd5eeae336d/maintainability)](https://codeclimate.com/github/kenoseni/Flight-Booking/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3f74bd32cfd5eeae336d/test_coverage)](https://codeclimate.com/github/kenoseni/Flight-Booking/test_coverage)

A flight book application for registerd users

## Description

The **flight-booking-api** enables registered users book their flight reservations after saving their passport information into the application

## Key Application features

1. User Signup and Signin
2. Passport Registration
3. Flight Booking

### Development set up

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.6.5
    ```

-   Install pipenv:

    ```
    brew install pipenv
    ```

-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.6.25
    ```
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```

-   Clone the flight-booking-api repo and cd into it:

    ```
    git clone https://github.com/kenoseni/Flight-Booking.git
    ```

-   Install dependencies:

    ```
    pipenv install
    ```

-   Install dev dependencies to setup development environment:

    ```
    pipenv install --dev
    ```

-   Make a copy of the .env.sample file and rename it to .env and update the variables accordingly:

    ```
    FLASK_ENV = "development" # Takes either development, production, testing
    DATABASE_URL = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME" # Development and production postgres db uri
    TEST_DATABASE_URI = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME" # Testing postgres db uri
    JWT_SECRET_KEY = "" # Secret key to decode jwt
    API_BASE_URL_V1 = "" # The base url for V1 of the API
    ```

-   Activate a virtual environment:

    ```
    pipenv shell
    ```

-   Apply migrations:

    ```
    flask db upgrade
    ```

*   Run the application with either commands:

    ```
    python manage.py runserver
    ```

    or

    ```
    flask run
    ```

*   Should you make changes to the database models, run migrations as follows

    -   Migrate database:

        ```
        flask db migrate
        ```

    -   Upgrade to new structure:
        ```
        flask db upgrade
        ```

*   Deactivate the virtual environment once you're done:
    ```
    exit
    ```

## Running tests and generating report

On command line run:

```
pytest
```

To further view the lines not tested or covered if there is any,

An `htmlcov` directory will be created, get the `index.html` file by entering the directory and view it in your browser.
