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
SESSION_COOKIE_SECURE = True 
PERMANENT_SESSION_LIFETIME = timedelta(days=30)
