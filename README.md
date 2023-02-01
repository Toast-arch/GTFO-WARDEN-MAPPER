# GTFO-WARDEN-MAPPER

### WHAT IS GTFO WARDEN MAPPER?

GTFO WARDEN MAPPER is a GTFO tool meant for speedrunning. It helps speedrunners optimize paths and mapping to reach optimal times on their runs without modifying the game in any way and thus it's use is authorized for GTFO speedrunning.  

This tool uses custom made packages for specific levels that enhance log analyis thanks to pre-mapped ressources and allow additional features such as visual maps and extra information to be displayed. These packages can be found in the packages/ sub folder where it is indicated which levels have a package. Levels without a package can still be analysed but to a lesser extent.

As of version 1.3.1 (January 2023), GTFO WARDEN MAPPER uses a terminal to display output information and image files for generated maps.

### HOW TO USE

The following requirements assume that you are running on Windows and are using steam to play GFTO.

REQUIREMENTS:
- python3+ : you can install python 3.10 on the Microsoft store or on the python official website at https://www.python.org/downloads/windows/.
- python PIL : to install a python package, open a terminal using the "cmd" or "powershell" windows application and use the command **pip install pillow**.
- python opnecv (optional) :  to install a python package, open a terminal using the "cmd" or "powershell" windows application and use the command **pip install opencv-python**.

HOW TO DOWNLOAD:
- You can directly download the zip archive with link: https://github.com/Toast-arch/GTFO-WARDEN-MAPPER/archive/refs/heads/main.zip
- Or pull the repository using git with this link: https://github.com/Toast-arch/GTFO-WARDEN-MAPPER.git.

HOW TO USE:
- Open GTFO and start a level.
- Open a terminal using the "cmd" windows application.
- Navigate to the GTFO-WARDEN-MAPPER folder with the command **cd C:/Path/to/the/folder/GTFO-WARDEN-MAPPER**.
- Run the python script with the command **python warden-mapper.py** a couple seconds after the level has started (if you run the script too early it may output incorrect or no information at all).
- If a mapping package is available for the level you are playing, check for ZONE_XX_GENERATED.png images in the GTFO-WARDEN-MAPPER/ folder for visual maps.
- [Optional] Run the script with --help option for more info on optional arguments.

RECOMMENDATIONS:
- Download and install Visual Studio Code at https://code.visualstudio.com/download for simple visualization of generated images and ease of use of the terminal.

### AVAILABLE PACKAGES

- Finished:
&nbsp;&nbsp;&nbsp;&nbsp;R1 : A1, B1, C2
&nbsp;&nbsp;&nbsp;&nbsp;R2 : C2
&nbsp;&nbsp;&nbsp;&nbsp;R7 : C1
&nbsp;
- Unfinished (contains potential errors or is missing content):
&nbsp;&nbsp;&nbsp;&nbsp;R1 : B2
&nbsp;
- Work In Progress (not added yet):
&nbsp;&nbsp;&nbsp;&nbsp;R2 : A1, B1, B3, B4, D1, D2
&nbsp;&nbsp;&nbsp;&nbsp;R7 : E1

### NOTES & REMARKS

- warden-mapper.py is the tool you should be using to speedrun.
- package-mapper.py is a tool used to create level specific packages, do not use if unfamiliar.
- Generated maps are found in the root folder as png files. Visual Studio Code updates images as they are overwritten which is great for visualizing them.