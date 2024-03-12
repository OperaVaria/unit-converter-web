"""
calc_functions.py

Module of the "Unit Converter for Historical Studies Web App" project.

Functions related to calculations.

By OperaVaria, 2024.
"""

# Built-in module imports:
from decimal import Decimal, getcontext, Overflow, InvalidOperation
from flask_babel import gettext


def calculate(input_value, input_inter, output_inter):
    """Performs final calculation with error handling and rounding."""
    # Calculation with the decimal module.
    try:
        solution = (Decimal(input_value)
                    * Decimal(input_inter)
                    / Decimal(output_inter))
        # Rounded with precision 10.
        getcontext().prec = 10
        # Normalize, if between 1E-5 and 1E+5: no scientific notation.
        # Smaller or larger numbers: yes.
        if 0.00001 <= float(solution) <= 100000:
            solution = "{:f}".format(solution.normalize())
        else:
            solution = solution.normalize()
    # Zero division, overflow, invalid operator displays an error.
    except (ZeroDivisionError, Overflow, InvalidOperation):
        solution = gettext("Hiba!")
    return solution


# Display message when accidentally run:
if __name__ == "__main__":
    print("Importable module. Not meant to be run!")
