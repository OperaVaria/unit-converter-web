"""
ucw_flask_app.py

This web application is an easy-to-use converter for historical measurement units. Its aim is
to assist both researchers and regular users with the conversion of historical units. Contrary to
other converters available on the internet, in the present project all information is derived from reliable
literature, their source is duly noted and verifiable in the unit database. The short information
notices on the interface provide the user with the basic context of the selected unit or unit system.

Currently the database features mostly unit systems connected to the historical Austria and Hungary,
as well as the Ancient Greek and Roman measurements; however any unit system can be implemented,
and their addition is continuous. All modern metric and relevant Anglo-American units are present for reference.

The application is available with both English and Hungarian interfaces.

Our project is built on the Flask web framework, with a Python backend and a conventional HTML-CSS-JS frontend.
No external website templates were utilized. The application relies greatly on the Jinja template engine in
generating the HTML pages to achieve the most optimal website coding. The localization is done with the aid of
the Flask-Babel extension, the language selection is stored in server-side sessions.

TODO: 1. Testing.
      2. Add more unit systems.
      3. Possibly add coin weights.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "1.0.0"
__date__ = "2024.02.23"


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
from flask import Flask, abort, jsonify, make_response, redirect, render_template, request, session, url_for

# Flask extension imports:
from flask_babel import Babel
from flask_session import Session

# Other imports:
import json

# Local imports:
from py_backend.setup_functions import (title_setup, sys_dict_setup, sys_info_setup,
                                        unit_dict_setup, unit_info_setup, calculation_setup,
                                        cat_dict_setup, source_dict_setup)
from py_backend.calc_functions import calculate

# Create Flask app.
app = Flask(__name__)

# Flask app configuration:
app.config.from_file("./config/secretKey.json", load=json.load) # Load secret key.
app.config.from_pyfile("./config/settings.py") # Other settings.
app.json.sort_keys = False # Do not sort json content alphabetically.

# Set up Session.
sess = Session(app)

# Babel get_locale function.
def get_locale():
    if "locale" in session:
        return session["locale"]
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# Set up Babel.
babel = Babel(app, locale_selector=get_locale)


# Flask page building decorators:

@app.route("/")
def index():
    """Set up index page."""
    # Get current locale:
    locale = get_locale()
    # Create dictionary for button builder loop.
    cat_dict = cat_dict_setup(locale)
    return render_template("index.html", cat_dict=cat_dict)

@app.route("/<unit_cat>")
def converter(unit_cat):
    """Set up converter page."""
    # Get current locale:
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
    return render_template("converter.html", conv_title=conv_title,
                           unit_sys_dict=unit_sys_dict, cat_dict=cat_dict)

@app.route("/about")
def about():
    """Set up about page."""
    return render_template("about.html")

@app.route("/about/sources")
def sources():
    """Set up sources page."""
    # Create dictionary to populate sources lists.
    source_dict = source_dict_setup()
    # Render.
    return render_template("sources.html", source_dict=source_dict)

@app.route("/fetch-traffic", methods=["POST"])
def fetch_traffic():
    """URL for fetch request json data transfer."""
    # Get current locale:
    locale = get_locale()
    # Get request json:
    req = request.get_json()
    # Handle requests based on sender.
    match req["sender"]:
        case "input-system-menu" | "output-system-menu":
            # System menus: send system info data and a dictionary to populate unit list.
            info_dat = sys_info_setup(req["value"], locale)
            menu_dat = unit_dict_setup(req["value"], locale)
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
    return res

@app.route("/receive-post", methods=["POST"])
def receive_post():
    """URL for receiving locale post requests."""
    if request.method == 'POST':
        session["locale"] = request.form["locale-btn"]
    return redirect(url_for("index"))


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
