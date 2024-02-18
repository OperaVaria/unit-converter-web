"""
fetch_functions.py

Module of the "Unit Converter for Historical Studies Web App" project.

Functions related to database fetching. These functions are called by the setup functions.

By OperaVaria, 2024.
"""

# Built-in module imports:
import sqlite3


def fetch_one(command, param):
    """Fetch a single value from the database."""
    # Database access.
    con = sqlite3.connect("database/unit_database.db")
    cur = con.cursor()
    # Execute.
    res = cur.execute(command, param)
    # Fetch and unpack tuple,
    value = (res.fetchone()[0])
    # Close connection.
    con.close()
    return value


def fetch_dict(command, param):
    """Build dictionary from the database."""
    # Create dict.
    value_dict = {}
    # Database access.
    con = sqlite3.connect("database/unit_database.db")
    cur = con.cursor()
    # Fill unit system dict.
    for key, value in cur.execute(command, param):
        value_dict[key] = value   
    # Close connection.
    con.close()
    return value_dict


# Display message when accidentally run:
if __name__ == "__main__":
    print("Importable module. Not meant to be run!")
