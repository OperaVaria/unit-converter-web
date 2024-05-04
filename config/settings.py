""" Flask and Flask extensions configuration file. """

# Built-in imports:
from datetime import timedelta
from pathlib import Path

# CacheLib import:
from cachelib.file import FileSystemCache

# Babel settings:
BABEL_DEFAULT_LOCALE = "hu"
LANGUAGES = {
    "hu": "magyar",
    "en": "English",
}

# Minify settings:
bypass = ["robots_txt", "humans_txt", "sitemap_xml"]

# Session settings:
sessions_path = Path(__file__).parents[1].resolve() / "flask_session"
SESSION_TYPE = "cachelib"
SESSION_CACHELIB = FileSystemCache(threshold=500, cache_dir=sessions_path)
SESSION_PERMANENT = True
PERMANENT_SESSION_LIFETIME = timedelta(days=30)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Strict"

# Talisman settings:
csp = {
    "default-src": ["'none'"],
    "connect-src": ["'self'"],
    "script-src": [
        "'self'",
        "'sha256-StHcb2rwa+JQQMEW05Q1ksZqLW064v3HKGcKpiYMMsc='",
        "'sha256-mNoUSBnIsLtJrvz4HSLr6Zob4ftw0pbk4UzBxZfjr04='",
        "https://cdn.jsdelivr.net/npm/choices.js/public/assets/scripts/choices.min.js",
    ],
    "style-src": ["'self'"],
    "img-src": ["'self'"],
    "object-src": ["'none'"],
    "base-uri": ["'none'"],
    "form-action": ["'self'"],
}


# Display message when accidentally run:
if __name__ == "__main__":
    print("This is a config file for Flask. Not meant to be run!")
