# Classwork Control (CW) CW07 & CW08

## CW07: Verification Digit Algorithm
This directory contains the Python implementation of a script designed to automatically calculate a verification digit based on standard modular arithmetic rules.

### Algorithm Description
The program processes a string of numeric characters and applies the following logical steps:

1. **Reversal:** The base identification number provided by the user is reversed to process the positions from right to left.
2. **Weighting:** Each digit is sequentially multiplied by a constant sequence ranging from 2 to 7. If the number of digits exceeds the sequence, the multiplier automatically resets to 2.
3. **Modulus 11:** The remainder of the total sum of the products is calculated using the mathematical modulus 11 operation ( `total % 11` ).
4. **Subtraction:** The resulting remainder is subtracted from the fixed number 11 to determine the final verification code.
5. **Special Cases:**
   * If the final result equals 11, the assigned verification digit is `0`.
   * If the final result equals 10, the assigned verification digit is the letter `K`.

### Running the Script
To run the script locally, make sure you have a Python 3 execution environment active and run the following command from your terminal:

```bash
python CW07/verificador.py