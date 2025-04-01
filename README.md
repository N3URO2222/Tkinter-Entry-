# Simple Tkinter Form

## Description
This is a simple GUI-based form created using Python's Tkinter library. It consists of a basic user interface with two input fields: one for an email ("Mail") and another for a password ("Password").

## Features
- Uses Tkinter to create a graphical user interface.
- Includes labels and entry fields for user input.
- Utilizes the grid() method for layout management.
- Responsive and easy to use.

## Prerequisites
Before running the script, ensure you have Python installed on your system. Tkinter comes pre-installed with standard Python distributions.

## Installation
1. Install Python (if not already installed) from [python.org](https://www.python.org/).
2. Tkinter is included by default in Python, so no additional installation is required.

## How to Run
1. Save the script as form.py.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the following command:
   sh
   python form.py
   

## Code Explanation
- *Importing Tkinter:* The script imports tkinter to create the GUI.
- *Creating a Window:* Tk() initializes the main application window.
- *Setting Window Properties:* The window is titled "Simple" and given a size of 500x700 pixels.
- *Adding Labels & Entry Fields:* Labels are used for "Mail" and "Password," while Entry fields allow user input.
- *Using the Grid Layout:* grid(row, column) is used to position elements in the window.
- *Running the Application:* window.mainloop() starts the Tkinter event loop to display the GUI.

## Example Output
When the script is executed, a window appears with:
- A "Mail" label and input field.
- A "Password" label and input field.

## Future Improvements
- Add a "Submit" button to process input data.
- Implement input validation for email and password fields.
- Enhance the UI with styling and padding.

## License
This project is open-source and free to use.
