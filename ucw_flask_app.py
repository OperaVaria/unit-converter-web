"""
ucw_flask_app.py

This web application is an easy-to-use converter for historical measurement units.
Its aim is to assist both researchers and regular users with the conversion of units
from the past. Contrary to other converters available on the internet,
in the present project all information is derived from reliable literature,
their source is duly noted and verifiable in the unit database.

Further information in ./docs/README.md.

TODO: 1. Testing.
      2. Add more unit systems.
      3. Possibly add coin weights.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "1.3.0"
__date__ = "2024.03.12"


# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2024, Csaba Latosinszky"

"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>
"""

# Flask imports:
from flask import (Flask, abort, jsonify, make_response, redirect,
                   render_template, request, send_from_directory,
                   session, url_for)

# Flask extension imports:
from flask_babel import Babel
from flask_minify import Minify
from flask_session import Session
from flask_talisman import Talisman

# Other imports:
import json
from config.settings import csp  # Content security policy settings.
from config.settings import bypass  # Minify bypass settings.

# Local imports:
from py_backend.setup_functions import (title_setup, sys_dict_setup, sys_info_setup,
                                        unit_list_setup, unit_info_setup, calculation_setup,
                                        cat_dict_setup, source_dict_setup)
from py_backend.calc_functions import calculate

# Create Flask app.
app = Flask(__name__)

# Flask app configuration:
app.config.from_file("./config/secretKey.json", load=json.load)  # Load secret key.
app.config.from_pyfile("./config/settings.py")  # Load other settings.
app.json.sort_keys = False  # Do not sort json content alphabetically.

# Set up Talisman.
tali = Talisman(app, content_security_policy=csp)

# Set up Minify.
mini = Minify(app=app, bypass=bypass, html=True, js=True, cssless=True)

# Set up Session.
sess = Session(app)

# Babel get_locale function.
def get_locale():
    # If locale information in session: set it as locale.
    if "locale" in session:
        locale = session["locale"]
    else:
        # If not, attempt best match.
        loc_best = request.accept_languages.best_match(app.config["LANGUAGES"].keys())
        # if unsuccessful: set default locale.
        if loc_best is None:
            locale = app.config.get("BABEL_DEFAULT_LOCALE")
        # If successful: set best match.
        else:
            locale = loc_best
    return locale

# Set up Babel.
babel = Babel(app, locale_selector=get_locale)


# Flask page building decorators:

@app.route("/")
def index():
    """Set up index page."""
    # Get current locale.
    locale = get_locale()
    # Create dictionary for button builder loop.
    cat_dict = cat_dict_setup(locale)
    # Render.
    return render_template("index.html", locale=locale,
                           cat_dict=cat_dict, version=__version__)

@app.route("/<unit_cat>")
def converter(unit_cat):
    """Set up converter page."""
    # Get current locale.
    locale = get_locale()
    # Create dictionary for button builder loop
    # and request error handling.
    cat_dict = cat_dict_setup(locale)
    # Send error if invalid unit category URL is passed.
    if unit_cat not in cat_dict.keys():
        abort(404)
    # Get correct title from database.
    conv_title = title_setup(unit_cat, locale)
    # Create dictionary to populate system lists.
    unit_sys_dict = sys_dict_setup(unit_cat, locale)
    # Render.
    return render_template("converter.html", locale=locale, conv_title=conv_title,
                           unit_sys_dict=unit_sys_dict, cat_dict=cat_dict)

@app.route("/about")
def about():
    """Set up about page."""
    # Get current locale.
    locale = get_locale()
    # Render.
    return render_template("about.html", locale=locale)

@app.route("/about/sources")
def sources():
    """Set up sources page."""
    # Get current locale.
    locale = get_locale()
    # Create dictionary to populate sources lists.
    source_dict = source_dict_setup()
    # Render.
    return render_template("sources.html", locale=locale, source_dict=source_dict)

@app.route("/fetch-traffic", methods=["POST"])
def fetch_traffic():
    """URL for fetch request json data transfer."""
    # Get current locale.
    locale = get_locale()
    # Get request json.
    req = request.get_json()
    # Handle requests based on sender.
    match req["sender"]:
        case "input-system-menu" | "output-system-menu":
            # System menus: send system info data and unit list to populate unit menu.
            info_dat = sys_info_setup(req["value"], locale)
            menu_dat = unit_list_setup(req["value"], locale)
            res = make_response(jsonify({"reqSender": req["sender"], "info": info_dat, "list": menu_dat}), 200)
        case "input-unit-menu"| "output-unit-menu":
            # Unit menus: send unit info data.
            info_dat = unit_info_setup(req["value"], locale)
            res = make_response(jsonify({"reqSender": req["sender"], "info": info_dat}), 200)
        case "convert-btn"| "swap-btn":
            # Convert buttons: get unit intermediary values, get output unit symbol,
            # call calculation function, pass result and symbol.
            input_inter, output_inter, symbol_dat = calculation_setup(req["inputUnit"], req["outputUnit"])
            result_dat = calculate(req["inputValue"], input_inter, output_inter)
            res = make_response(jsonify({"reqSender": req["sender"], "result": result_dat, "symbol": symbol_dat}), 200)
        case _ :
            # Any other option (should not happen): error response.
            res = make_response(jsonify({"error": "Unknown sender id!"}), 400)
    # Send response.
    return res

@app.route("/receive-post", methods=["POST"])
def receive_post():
    """URL for receiving locale post requests."""
    if request.method == "POST":
        session["locale"] = request.form["locale-btn"]
    return redirect(url_for("index"))

@app.route("/robots.txt")
def robots_txt():
    """Set up robots.txt."""
    return send_from_directory("static", "other/robots.txt")

@app.route("/humans.txt")
def humans_txt():
    """Set up humans.txt."""
    return send_from_directory("static", "other/humans.txt")

@app.route("/sitemap.xml")
def sitemap_xml():
    """Set up sitemap.xml."""
    return send_from_directory("static", "other/sitemap.xml")


# When run as main run on localhost, port 8080:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
