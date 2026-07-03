# Classwork: Mandelbrot Set Data Generator

## Program Description
This project consists of an automated numerical data generator designed to map and analyze the geometry of the famous **Mandelbrot Set** fractal. Developed in a strictly linear and sequential manner, the program ensures data persistence and precision by avoiding complex function abstractions, relying instead on fundamental iterative loops and native complex number operations.

The execution architecture is divided into four distinct phases:
1. **Configuration Ingestion:** The program opens and parses an external configuration file (`config.txt`). It dynamically dynamically extracts execution boundaries, mapping limits, and resolution parameters (`ancho`, `alto`, `max_iter`), loading them into a centralized control dictionary.
2. **Coordinate Plane Mapping:** Using nested loops to traverse the requested pixel grid, the system maps each discrete matrix coordinate `(columna, fila)` into a precise point `c` on the mathematical complex number plane.
3. **Divergence Evaluation:** For every point, the system evaluates the classic quadratic recurrence relation $z_{n+1} = z_n^2 + c$ starting from $z_0 = 0$. A sequential control loop tracks the exact number of iterations required for the absolute value of $z$ to escape the boundedness boundary ($|z| > 2$), stopping automatically if it hits the maximum predefined threshold.
4. **Structured Data Export:** The results are formatted dynamically and exported in real-time into a structured CSV file (`clase.csv`), recording the matrix position and its specific divergence rate under the header `fila,columna,iteraciones`.

---

## Repository File Structure
To strictly comply with the requirements established in the assignment, the folder contains the following elements:
* `mandelbrot_generator.py`: The functional Python script containing the fractal simulation architecture, fully documented with technical comments (`# INPUT`, `# PROCESS`, `# OUTPUT`).
* `config.txt`: The external setup file containing the required parameters (dimensions, iterations, and complex plane boundaries) to feed the execution grid.
* `clase.csv`: The generated master matrix dataset detailing the exact layout and iteration count for each pixel, ready for visualization rendering.

---

## AI Usage Declaration
In compliance with academic integrity policies applicable to Data and AI Engineering projects, the strategic use of conversational AI tools (Gemini/Large Language Models) is hereby declared as a technological assistant during the development cycle of this coursework.

The scope of the interaction with the AI was strictly limited to the following optimization and acceleration activities:
* **Documentation Redaction and Fluency:** The AI was utilized as a heuristic support tool to structure, translate, and refine the technical descriptions contained within this `README.md` file, ensuring professional and academic terminology.
* **Flowchart Generation:** The assistant was used to design and map the logical architecture, nested execution loops, and complex number decision boundaries to ensure an accurate graphic layout of the generator's control flow.

The entire mathematical mapping logic, bounding validation criteria, data structures, and local execution testing were thoroughly analyzed, validated, and supervised by the author of this repository.
