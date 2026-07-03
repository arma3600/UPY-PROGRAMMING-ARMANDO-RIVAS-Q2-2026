# Classwork: Mandelbrot Set Visualizer and Renderer

## Program Description
This project consists of an automated digital image renderer designed to visualize the geometric boundaries of the **Mandelbrot Set** fractal. Developed in a linear and sequential manner, the program processes precomputed divergence datasets to perform color-space mapping and pixel-level image generation without relying on complex structural abstractions.

The execution architecture is divided into four distinct operational phases:
1. **Configuration and Data Ingestion:** The program reads structural parameters (`alto`, `ancho`, `max_iter`) from an external configuration file (`config.txt`). Concurrently, it loads the master raw data matrix from a previously generated CSV file (`clase.csv`), isolation-filtering the dataset by stripping the table headers.
2. **Canvas and Color Space Initialization:** Utilizing the Python Imaging Library (`PIL`), the system instantiates a digital canvas matching the precise matrix dimensions using the HSV (Hue, Saturation, Value) color model, which allows for dynamic luminosity scaling.
3. **Luminosity Mapping Loop:** A sequential loop parses every discrete coordinate sequence `(fila, columna, iteraciones)`. The system applies a normalization algorithm where points belonging to the stable set (where iterations equal `max_iter`) are mapped to absolute darkness (`brillo = 0`). Points that escaped are assigned a relative brightness value normalized between $0$ and $255$ based on their divergence velocity.
4. **Color Conversion and Image Export:** The script utilizes the `putpixel` method to map individual data points onto the coordinate canvas. Finally, it executes a programmatic color space conversion from HSV to RGB (Red, Green, Blue) and exports the finalized high-resolution fractal image under the filename `mandelbrot-clase.png`.

---

## Repository File Structure
To strictly comply with the requirements established in the assignment, the folder contains the following elements:
* `mandelbrot_renderer.py`: The functional Python script containing the pixel mapping and fractal rendering logic, fully documented with technical comments (`# INPUT`, `# PROCESS`, `# OUTPUT`).
* `config.txt`: The structural setup file containing execution dimensions and threshold metrics to align the canvas limits.
* `clase.csv`: The input dataset file containing the raw coordinate matrix and divergence records used to feed the renderer loop.
* `mandelbrot-clase.png`: The finalized graphical output image displaying the visually rendered fractal geometry.

---

## AI Usage Declaration
In compliance with academic integrity policies applicable to Data and AI Engineering projects, the strategic use of conversational AI tools (Gemini/Large Language Models) is hereby declared as a technological assistant during the development cycle of this coursework.

The scope of the interaction with the AI was strictly limited to the following optimization and acceleration activities:
* **Documentation Redaction and Fluency:** The AI was utilized as a heuristic support tool to structure, translate, and refine the technical descriptions contained within this `README.md` file, ensuring professional and academic terminology.
* **Flowchart Generation:** The assistant was used to design and map the logical architecture, image parsing steps, nested matrix conversion loops, and normalization formulas to ensure an accurate graphic layout of the renderer's control flow.

The entire digital rendering logic, pixel-to-complex transformations, normalization calculations, and local execution testing were thoroughly analyzed, validated, and supervised by the author of this repository.