# GUI for ABAQUS Mesh Refinement 
While working with ABAQUS for Finite Element Analysis (FEA) applications, mesh quality plays a critical role in obtaining accurate and reliable results. To facilitate this process, a Python-based Graphical User Interface (GUI) has been developed. This tool assists users in visualizing and evaluating mesh refinement results, making it easier to interpret and optimize meshing strategies for better FEA outcomes.


While working with ABAQUS for Finite Element Analysis (FEA) applications, mesh quality plays a critical role in obtaining accurate and reliable results. To assist with this, a Python-based Graphical User Interface (GUI) has been developed. This tool allows users to visualize and analyze mesh refinement statistics such as node count, time increment (stableDT), and scale factors.

Features
Header GUI (Header_GUI.py): Displays project title or status bar.

Command Bar (CommandBar_GUI.py): Provides user controls for interactions like loading data or triggering analysis.

Main Screen (MainScreen_GUI.py): Visualizes mesh refinement results with plots (e.g., Scale Factor vs. Node Count).

Main Application (MainApp_GUI.py): Integrates all components and launches the complete GUI.

Requirements
Python 3.x

matplotlib

numpy

tkinter (typically included with Python)

ABAQUS-generated CSV data (meshRefinementStats.csv)
