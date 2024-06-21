### Create an Executable File (.exe) Using PyInstaller

#### Overview

This guide will walk you through packaging your Python application into a standalone executable file (.exe) using PyInstaller.

#### Prerequisites

Before you begin, ensure the following are installed on your system:

- **Python**: Download and install Python from the [official Python website](https://www.python.org/downloads/).
- **PyInstaller**: Install PyInstaller using pip, which is included with Python by default.

#### Installation

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

2. **Install PyInstaller**:
   - Open a terminal or command prompt.
   - Use pip to install PyInstaller:
     ```bash
     pip install pyinstaller
     ```

#### Create an Executable File (.exe)

##### Using the Command Line

1. **Prepare Your Project**:
   - Organize your project directory with `main.py` and any necessary files, such as `HareetTashferIcon.png`, placed in relevant folders (e.g., `images`).

2. **Navigate to Your Project Directory**:
   - Open a terminal or command prompt.
   - Change directory (`cd`) to where your `main.py` file is located:
     ```bash
     cd /path/to/your/project
     ```

3. **Run PyInstaller**:
   - Execute PyInstaller with the following command:
     ```bash
     pyinstaller --onefile --windowed --add-data "images/HareetTashferIcon.png;images" --add-data "LICENSE;." --version-file version.txt --name HareetTashfer main.py
     ```
     Here’s a breakdown of each option and their functions:
      - `--onefile`: This option bundles everything into a single executable file.
      - `--windowed`: This runs the application without showing a console window (useful for GUI applications).
      - `--add-data "images/HareetTashferIcon.png;images"`: Specifies that `HareetTashferIcon.png` located in the `images` directory should be included in the bundled executable. The `;images` part means that `images` directory will be copied to the root directory of the executable.
      - `--add-data "LICENSE;."`: Adds the `LICENSE` file to the root directory of the executable.
      - `--version-file version.txt`: Includes version information from `version.txt` into the executable.
      - `--name HareetTashfer`: Names the generated executable file as `HareetTashfer` (or `HareetTashfer.exe` on Windows).


4. **Locate Your Executable**:
   - After PyInstaller completes the process, find the executable in the `dist` directory within your project folder.

5. **Run Your Executable**:
   - Double-click the executable (`HareetTashfer.exe`) to run your Python application as a standalone program.

#### Additional Notes

- **Customization**: Modify paths and options as necessary to fit your project structure and requirements.
- **Dependencies**: Ensure all required Python modules are correctly imported and installed for your application to run smoothly.

This guide should help you successfully package your Python application into a standalone executable file using PyInstaller, complete with a custom icon. Adjust paths and instructions according to your specific project needs.
