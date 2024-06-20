# Project Name

## Overview

This project contains a Qt Designer UI file (`hareettashfer.ui`) which needs to be converted to a Python file. The Python file will be used to create the graphical user interface (GUI) defined in the `.ui` file.

## Prerequisites

- Python 3.x
- PyQt5 or PyQt6

## Installation

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install PyQt5 or PyQt6

Install PyQt5 using pip:

```bash
pip install PyQt5
```

or install PyQt6:

```bash
pip install PyQt6
```

## Converting .ui to .py

### Using the Command Line

1. Open a command prompt or terminal.
2. Navigate to the directory containing your `hareettashfer.ui` file.
3. Run the following command for PyQt5:

    ```bash
    pyuic5 -x hareettashfer.ui -o hareettashfer.py
    ```

    or for PyQt6:

    ```bash
    pyuic6 -x hareettashfer.ui -o hareettashfer.py
    ```

### Using a Python Script

Alternatively, you can use a Python script to perform the conversion:

For PyQt5:

```python
from PyQt5 import uic

with open('hareettashfer.py', 'w', encoding='utf-8') as py_file:
    uic.compileUi('hareettashfer.ui', py_file)
```

For PyQt6:

```python
from PyQt6 import uic

with open('hareettashfer.py', 'w', encoding='utf-8') as py_file:
    uic.compileUi('hareettashfer.ui', py_file)
```

## Running the Generated Python File

After converting the `.ui` file to a `.py` file, you can run it using Python:

```bash
python hareettashfer.py
```

This will launch the GUI defined in the `hareettashfer.ui` file.

## Additional Information

- The `-x` option in the `pyuic` command generates a Python file that can be executed as a standalone script.
- The `-o` option specifies the output filename.
- Ensure you are in the same directory as the `hareettashfer.ui` file when running the conversion commands.

## Troubleshooting

- If you encounter any issues with missing modules, ensure that PyQt5 or PyQt6 is correctly installed.
- Verify the path to the `hareettashfer.ui` file if you receive a file not found error.

## References

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)