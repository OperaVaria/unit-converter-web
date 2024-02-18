"""
ucw_flask_app.py

Main file of the "Unit Converter for Historical Studies Web App" project.

This Flask app is a simple converter for historical measurement units. For the moment, the app it is only available
with a Hungarian UI, and features historical unit systems mainly associated with Austria and Hungary, as well as the
Ancient Greek and Roman measurements—however, any unit system can be implemented. All modern metric and Anglo-American
units are added for reference. The converter uses the Flask web framework, with a Python backed and a standard
HTML-CSS-JS frontend. The unit database was built with the SQLite database engine.

TODO: 1. Testing
      2. Implement English UI.
      3. Add more unit systems.
      4. Possibly add coin weights.
"""

# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2024, OperaVaria"

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
from flask import Flask, jsonify, make_response, render_template, request

# Local imports:
from py_backend.setup_functions import (title_setup, sys_dict_setup, sys_info_setup,
                                        unit_dict_setup, unit_info_setup, calculation_setup)
from py_backend.calc_functions import calculate

# Create Flask app:
app = Flask(__name__)


# Page building decorators:
@app.route("/")
def index():
    """Set up index page."""
    return render_template("index.html")

@app.route("/<unit_cat>")
def converter(unit_cat):
    """Set up converter page."""
    # Get correct title from database.
    conv_title = title_setup(unit_cat)
    # Create dictionary to populate system lists.
    unit_sys_dict = sys_dict_setup(unit_cat)
    # Render.
    return render_template("converter.html", conv_title=conv_title, unit_sys_dict=unit_sys_dict)

@app.route("/about")
def about():
    """Set up about page."""
    return render_template("about.html")

@app.route("/fetch-traffic", methods=["POST"])
def fetch_traffic():
    """URL for fetch json data transfer."""
    req = request.get_json()
    # Handle requests based upon sender.
    match req["sender"]:
        case "input_system_menu" | "output_system_menu":
            # System menus: send system info data and a dictionary to populate unit list. 
            info_dat = sys_info_setup(req["value"])
            menu_dat = unit_dict_setup(req["value"])
            res = make_response(jsonify({"req_sender": req["sender"], "info": info_dat, "list": menu_dat}), 200)
        case "input_unit_menu"| "output_unit_menu":
            # Unit menus: send unit info data.
            info_dat = unit_info_setup(req["value"])
            res = make_response(jsonify({"req_sender": req["sender"], "info": info_dat}), 200)
        case "convert_btn":
            # Convert button: get unit intermediary values, get output unit symbol,
            # call calculation function, pass result and symbol.
            input_inter, output_inter, symbol_dat = calculation_setup(req["input_unit"], req["output_unit"])
            result_dat = calculate(req["input_value"], input_inter, output_inter)
            res = make_response(jsonify({"req_sender": req["sender"], "result": result_dat, "symbol": symbol_dat}), 200)
        case _ :
            # Any other option (should not happen): error response.
            res = make_response(jsonify({"Error": "Unknown sender element."}), 400)
    return res


# When run as main run on localhost, port 8080:
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)