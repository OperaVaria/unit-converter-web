"""
setup_functions.py

Module of the "Unit Converter for Historical Studies Web App" project.

Functions setting up correct database fetches.

By OperaVaria, 2024.
"""

# Local imports:
from py_backend.fetch_functions import fetch_one, fetch_dict


def title_setup(unit_cat):
    """Retrieve calculator page title from the database."""
    # SQLite command.
    command = "SELECT cat_hun FROM cat_list WHERE cat_raw = ?"
    # Search parameter.
    param = (unit_cat,)
    # Call fetch function.
    value = fetch_one(command, param)
    # Capitalize title.
    conv_title = str.capitalize(value)
    return conv_title


def sys_dict_setup(unit_cat):
    """Build selected unit system dictionary from the database."""
    # SQLite command.
    command = "SELECT name_raw, name_hun FROM system_list WHERE cat_raw LIKE ?"
    # Search parameter.
    param = (f"%{unit_cat}%",)
    # Call fetch function.
    unit_sys_dict = fetch_dict(command, param)
    return unit_sys_dict


def unit_dict_setup(unit_system):
    """Build selected unit dictionary from the database."""
    # SQLite command.
    command = "SELECT name_raw, name_gui FROM unit_list WHERE sys_raw = ?"
    # Search parameter.
    param = (unit_system,)
    # Call fetch function.
    unit_dict = fetch_dict(command, param)
    return unit_dict


def sys_info_setup(unit_system):
    """Retrieve system info from the database based on unit system selection."""
    # SQLite command.
    command = "SELECT info FROM system_list WHERE name_raw = ?"
    # Search parameter.
    param = (unit_system,)
    # Call fetch function.
    unit_sys_info = fetch_one(command, param)
    return unit_sys_info


def unit_info_setup(selected_unit):
    """Retrieve unit info from the database based on unit selection."""
    # SQLite command.
    command = "SELECT info FROM unit_list WHERE name_raw = ?"
    # Search parameter.
    param = (selected_unit,)
    # Call fetch function.
    unit_info = fetch_one(command, param)
    return unit_info


def calculation_setup(input_unit, output_unit):
    """ Retrieve intermediary values for calculation,
        and unit symbol to display with result."""
    # SQLite commands.
    inter_command = "SELECT inter_val FROM unit_list WHERE name_raw = ?"
    symbol_command = "SELECT symbol FROM unit_list WHERE name_raw = ?"
    # Search parameters.
    param_input = (input_unit,)
    param_output = (output_unit,)
    # Call fetch function.
    input_inter = fetch_one(inter_command, param_input)
    output_inter = fetch_one(inter_command, param_output)
    unit_symbol = fetch_one(symbol_command, param_output)
    # Fetch output unit intermediary value:
    return input_inter, output_inter, unit_symbol


# Display message when accidentally run:
if __name__ == "__main__":
    print("Importable module. Not meant to be run!")
