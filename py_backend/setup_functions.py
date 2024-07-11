"""
setup_functions.py

Module of the "Unit Converter for Historical Studies Web App" project.

Functions setting up correct database fetches.

By OperaVaria, 2024.
"""

# Local imports:
from py_backend.fetch_functions import fetch_one, fetch_dict


def title_setup(unit_cat, locale):
    """Retrieve calculator page title from the database."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT cat_hun FROM cat_list WHERE cat_raw = ?"
    else:
        command = "SELECT cat_eng FROM cat_list WHERE cat_raw = ?"
    # Search parameter.
    param = (unit_cat,)
    # Call fetch function.
    value = fetch_one(command, param)
    # Capitalize title.
    conv_title = str.capitalize(value)
    return conv_title


def sys_dict_setup(unit_cat, locale):
    """Build selected unit system dictionary from the database."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT name_raw, name_hun FROM system_list WHERE cat_raw LIKE ?"
    else:
        command = "SELECT name_raw, name_eng FROM system_list WHERE cat_raw LIKE ?"
    # Search parameter.
    param = (f"%{unit_cat}%",)
    # Call fetch function.
    unit_sys_dict = fetch_dict(command, param)
    return unit_sys_dict


def unit_list_setup(unit_system, locale):
    """Build selected unit list from the database."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT name_raw, name_hun FROM unit_list WHERE sys_raw = ?"
    else:
        command = "SELECT name_raw, name_eng FROM unit_list WHERE sys_raw = ?"
    # Search parameter.
    param = (unit_system,)
    # Call fetch function.
    unit_dict = fetch_dict(command, param)
    # Convert to proper Py list/JS array format for Choices.js.
    unit_list = [{"value": i, "label": j} for i, j in unit_dict.items()]
    return unit_list


def sys_info_setup(unit_system, locale):
    """Retrieve system info from the database based on unit system selection."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT info_hun FROM system_list WHERE name_raw = ?"
    else:
        command = "SELECT info_eng FROM system_list WHERE name_raw = ?"
    # Search parameter.
    param = (unit_system,)
    # Call fetch function.
    unit_sys_info = fetch_one(command, param)
    return unit_sys_info


def unit_info_setup(selected_unit, locale):
    """Retrieve unit info from the database based on unit selection."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT info_hun FROM unit_list WHERE name_raw = ?"
    else:
        command = "SELECT info_eng FROM unit_list WHERE name_raw = ?"
    # Search parameter.
    param = (selected_unit,)
    # Call fetch function.
    unit_info = fetch_one(command, param)
    return unit_info


def calculation_setup(input_unit, output_unit):
    """Retrieve intermediary values for calculation,
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


def cat_dict_setup(locale):
    """Build a dictionary from unit category information
       for error handling and jinja2 button builder loops."""
    # SQLite command based on current locale.
    if locale == "hu":
        command = "SELECT cat_raw, cat_hun FROM cat_list"
    else:
        command = "SELECT cat_raw, cat_eng FROM cat_list"
    # Search parameter.
    param = ()
    # Call fetch function.
    cat_dict = fetch_dict(command, param)
    # Capitalize button tiles
    cat_dict = {key: str.capitalize(value) for (key,value) in cat_dict.items()}
    return cat_dict


def source_dict_setup():
    """Build a dictionary of sources from the database (author date + html formatted entry)."""
    # SQLite command.
    command = "SELECT author_date, html FROM source_list"
    # Search parameter.
    param = ()
    # Call fetch function.
    source_dict = fetch_dict(command, param)
    return source_dict


# Display message when accidentally run:
if __name__ == "__main__":
    print("Importable module. Not meant to be run!")
