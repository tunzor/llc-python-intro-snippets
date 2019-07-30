## Example Python code snippets

### A collection of example code snippets for the Ladies Learning Code intro to python workshop

These can be run in the terminal with `python [PROGRAM_NAME]` for example `python ex1-show-cursor-position.py`

---

Examples 1 and 2 use the **pyautogui** library, example 3 uses the **requests** and **BeautifulSoup** libraries, example 4 uses the **Flask** library, and example 5 uses the **pillow** library

These can be installed on your computer with [pip](https://pip.pypa.io/en/stable/) (a Python package manager). If using pip on the command line you can install all of them with the requirements.txt file included here with the command
`pip install -r requirements.txt`

If you want to install them with PyCharm Edu, check out [this page](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)

---

`ex1-show-cursor-position.py`

This will endlessly print the position of the cursor to the command line. Stop it by pressing control+c.

---

`ex2-chrome-python-uses.py`

This will move the cursor to a specific point on the screen (the chrome icon on the launcher bar at the bottom), click the left mouse button, press the key combo COMMAND+T to open a new tab in chrome, type "What can I use python for?", and hit enter.
The `chromeX` and `chromeY` variables should be changed to correspond to the location on your computer.

---

`ex3-get-clc-team.py`

This will get the about us team page from the CLC website and display all of the team members and their titles.

---

`ex4-flask-web-server.py`

This will start a [Flask web server](https://palletsprojects.com/p/flask/) on your computer and make it accessible at http://localhost:5000

It displays a simple webpage.

---

`ex5-image-manipulation.py`

This will crop, resize, and rotate the photo of the Toronto skyline in the ex5 folder and save the new copies in the same folder.

---
