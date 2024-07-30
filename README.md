Claro! Aqui está uma sugestão de texto para o seu README no GitHub:


OldFilesHandler
This repository contains two Python scripts designed to manage old files efficiently. These scripts help automate the process of deleting and moving old files based on specified parameters.

Scripts Included
1. 
delete_old_files.py
•  Deletes files in a specified directory that are older than a given number of days.

•  Useful for maintaining clean directories by removing outdated files.

1. 
move_old_files.py
•  Moves files from a source directory to a destination directory if they are older than a specified number of days.

•  Helps in organizing files by relocating older files to a different directory.

Features
•  Customizable Parameters: Easily configure source, destination, and log directories, as well as the age threshold for files.

•  Logging: Both scripts generate log files to keep track of actions performed, including file deletions and movements.

•  Environment Variables: Uses environment variables for configuration, making it flexible and easy to manage.

Getting Started
Prerequisites
•  Python: Ensure Python is installed on your system. Download it from the official Python website.

Installation
1. 
Clone the Repository:

git clone https://github.com/yourusername/OldFilesHandler.git

2. 
Configure Environment Variables: Create a .env file in the root directory and set the necessary variables:

SRC_DIR=path/to/source_directory

DEST_DIR=path/to/destination_directory

LOG_DIR=path/to/log_directory

DELETE_DIR=path/to/delete_directory

DAYS_TO_DELETE=number_of_days

DAYS_TO_DELETE=number_of_days_for_moving_files

MAX_LOG_DAYS=number_of_days_for_logs


Usage
1. 
Run the delete_old_files.py script:

python delete_old_files.py

2. 
Run the move_old_files.py script:

python move_old_files.py

Creating an Executable for Windows
To create an executable for Windows, follow these steps:

1. 
Install PyInstaller:

pip install pyinstaller

2. 
Create the Executable:

pyinstaller --onefile --noconsole delete_old_files.py
pyinstaller --onefile --noconsole move_old_files.py

3. 
Locate the Executable:
After running PyInstaller, the executables will be located in the dist directory.

Optional: Improve the Appearance of the Executable
4. 
Specify an Icon:

pyinstaller --onefile --noconsole --icon=my_icon.ico delete_old_files.py
pyinstaller --onefile --noconsole --icon=my_icon.ico move_old_files.py

Contributions
Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!
