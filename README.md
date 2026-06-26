# Classwork 10: School Management System

## Program Description
This project consists of an automated school management system developed in a strictly linear and sequential manner. It ensures data persistence and validation using fundamental structures (dictionaries and tuples) without relying on complex functions or external subprocesses.

The program implements centralized access control through a user authentication system that dynamically branches the interface execution into three distinct roles with independent hierarchical permissions:

1. **Student Mode:** Allows users to query the grade report associated with the authenticated profile. It executes a logical filtering process to dynamically structure a final report, classifying and separating the taken subjects into two discrete sets: *Approved Subjects* (grade $\ge 7.0$) and *Pending Subjects*.
2. **Teacher Mode:** Provides an interactive editing environment. The teacher can view the complete list of students registered in the system, select a specific student along with the desired subject, and input a new grade. The system implements strict control loops to validate that numeric values remain within a range of $0.0$ to $10.0$ and includes a double security confirmation (Yes/No) before updating the database records.
3. **Coordinator Mode:** A high-level, read-only interface designed for academic auditing. It displays the complete catalog of teachers in the system, the static tuple of global subjects, and a comprehensive master matrix that maps every student in the database to their respective grade history.

---

## Repository File Structure
To strictly comply with the requirements established in the assignment, the folder contains the following elements:
* `school_management_system.py`: The functional Python script containing the system architecture, fully documented with technical comments (`# INPUT`, `# PROCESS`, `# OUTPUT`).
* `PPP.txt`: Structured technical pseudocode in plain English describing the sequential logic, validation loops, and branching structures using standard assignment symbols (`←`) and control comments (`#`).
* `Flowchart.png`: A complete high-resolution flowchart mapping the iterative validation flows, internal teacher loops, and menu decision paths.

---

## AI Usage Declaration
In compliance with academic integrity policies applicable to Data and AI Engineering projects, the strategic use of conversational AI tools (Gemini/Large Language Models) is hereby declared as a technological assistant during the development cycle of this coursework.

The scope of the interaction with the AI was strictly limited to the following optimization and acceleration activities:
* **Flowchart Generation:** The assistant was used to structure and refine the declarative syntax of the script in Mermaid format. This allowed for accurate mapping of the control logic, closed validation loops, and forced the correct visual rendering of independent menu boxes within the graphic design platform.
* **Code Redaction and Fluency:** The AI was utilized as a heuristic support tool to streamline the syntactic translation of the logical design into native Python statements and the structuring of the technical pseudocode. This guaranteed the absolute elimination of function calls or external dependencies, ensuring algorithmic consistency across iterations.

The entire system architecture, data structure relational logic, academic passing rules, and local execution testing were thoroughly analyzed, validated, and supervised by the author of this repository.