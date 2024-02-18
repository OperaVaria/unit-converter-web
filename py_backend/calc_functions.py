"""
calc_functions.py

Module of the "Unit Converter for Historical Studies Web App" project.

Functions related to calculations.

By OperaVaria, 2024.
"""

# Built-in module imports:
from decimal import Decimal, getcontext, Overflow, InvalidOperation


def calculate(input_value, input_inter, output_inter):
    """Performs final calculation with error handling and rounding."""
    # Calculation with the decimal module.
    try:
        solution = (Decimal(input_value)
                    * Decimal(input_inter)
                    / Decimal(output_inter))
        # Final result rounded to 10 decimals and normalized to the simplest form.
        getcontext().prec = 10
        solution = solution.normalize()
    # Zero division, overflow, invalid operator displays an error.
    except (ZeroDivisionError, Overflow, InvalidOperation):
        solution = "Hiba!"
    return solution


# Display message when accidentally run:
if __name__ == "__main__":
    print("Importable module. Not meant to be run!")