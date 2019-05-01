# Import the pyautogui library; will need to install it with pip (python package manager)
import pyautogui

# Get position of the chrome icon on the launcher
chromeX = 690
chromeY = 873

# Move the mouse to the position of the chrome icon and click it; make it take 2 seconds
pyautogui.moveTo(chromeX, chromeY, 2)
pyautogui.click()

# Press the key combination COMMAND and T; this combo opens a new tab in chrome
pyautogui.hotkey('command','t')

# Type the phrase "What can I use python for" and press enter; leave 0.1 seconds between key presses
pyautogui.typewrite('What can I use python for?\n', interval=0.1)
