""" Flask and Flask extensions configuration file. """

# Timedelta import:
from datetime import timedelta

# Babel settings:
BABEL_DEFAULT_LOCALE="hu"
LANGUAGES = {
    "hu": "magyar",
    "en": "English",
}

# Minify settings:
bypass = ["robots_txt", "humans_txt", "sitemap_xml"]

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
        "'none'"
    ],
    "connect-src": [
        "'self'"
    ],

    "script-src": [
        "'self'",
        "'sha256-StHcb2rwa+JQQMEW05Q1ksZqLW064v3HKGcKpiYMMsc='",
        "'sha256-mNoUSBnIsLtJrvz4HSLr6Zob4ftw0pbk4UzBxZfjr04='",
        "https://cdn.jsdelivr.net/npm/",
        "https://gc.kis.v2.scr.kaspersky-labs.com"
    ],

    "style-src": [
        "'self'",
        "https://cdn.jsdelivr.net/npm/"
    ],

    "img-src": [
        "'self'"
    ],

    "object-src": [
        "'none'"
    ],

    "base-uri": [
        "'none'"
    ],

    "form-action": [
        "'self'"
    ]
}


# Display message when accidentally run:
if __name__ == "__main__":
    print("This is a config file for Flask. Not meant to be run!")
