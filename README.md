## Example Python code snippets

### A collection of example code snippets for the Ladies Learning Code intro to python workshop

These can be run in the terminal with `python [PROGRAM_NAME]` for example `python ex1-show-cursor-position.py`
---
###### Examples 1 and 2 use the pyautogui library and example 3 uses the requests and BeautifulSoup libraries
###### These can be installed to your computer with [pip](https://pip.pypa.io/en/stable/)
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
