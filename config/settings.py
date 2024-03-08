""" Flask and Flask extensions configuration file. """

# Timedelta import:
from datetime import timedelta

# Babel settings:
BABEL_DEFAULT_LOCALE="hu"
LANGUAGES = {
    "hu": "magyar",
    "en": "English",
}

# Session settings:
SESSION_TYPE = "filesystem"
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = timedelta(days=30)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Strict"

# Talisman settings:
csp = {
    "default-src": [
        "'self'",

    ],
    "script-src": [
        "'self'",
        "'unsafe-inline'",
        "https://cdn.jsdelivr.net/npm/"
    ],
    'style-src': [
        "'self'",
        "https://cdn.jsdelivr.net/npm/"
    ]
}


# Display message when accidentally run:
if __name__ == "__main__":
    print("This is a config file for Flask. Not meant to be run!")
