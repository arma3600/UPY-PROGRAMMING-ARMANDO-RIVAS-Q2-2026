## CW08: Numerical Integration

### Description
This directory contains a Python program developed to approximate the definite integral of a function $f(x)$ within a specified closed interval $[a, b]$ using numerical methods. The script supports four distinct approximation techniques:
* **LRM:** Left Riemann Minimum / Left Rectangle Method.
* **RRM:** Right Riemann Maximum / Right Rectangle Method.
* **MRM:** Midpoint Riemann Method.
* **TRAP:** Trapezoidal Rule.

### Implementation Logic & Flow
The program reads the integration limits ($a, b$), the mathematical function expression as a string ($f(x)$), and the requested method. It handles mathematical constants dynamically (such as parsing `"pi"` to `math.pi`) before initializing a uniform partition grid of $n = 1000$ subintervals with width:
$$h = \frac{b - a}{n}$$

Depending on the chosen integration method, the algorithm adjusts iteration parameters, shifts, and evaluation points:
* **Rectangular Methods (LRM/RRM/MRM):** Computes the Riemann sum by evaluating the function heights at the designated partition points ($x_i + \text{constant}$) multiplied by the subinterval width $h$.
* **Trapezoidal Method (TRAP):** Approximates the area under the curve by evaluating endpoints individually and computing the composite sum of inner partitions scaled by a factor of 2, weighted by $\frac{h}{2}$.

### Execution
To run the script locally, ensure you have a Python 3 environment configured and execute the following command from the repository root:

```bash
python Classwork-08-Numerical-Integration/numerical_integration.py
```
AI Use Declaration
Tool Used: Gemini Large Language Model (Google).

Purpose: Primarily used to learn how to operate the terminal correctly, troubleshoot environment errors, and translate Python code logic into structured flowchart representations.
