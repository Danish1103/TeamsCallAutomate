# TeamsCallAutomate

This Python script automates attending online lectures on Microsoft Teams based on a provided schedule. It uses the following libraries:

time: To track the current time and schedule actions.
datetime: To parse and compare time values accurately.
pyautogui: To interact with the user interface by simulating mouse clicks and keyboard presses.
pynput.keyboard: To enable keyboard key presses programmatically.
webbrowser: To open the provided Teams meeting link in your default web browser.
Features:

Automatic Scheduling: The script iterates through a list of lectures, each containing a link, start time, and end time.
Meeting Join: When the current time matches the start time of a lecture, the script opens the Teams meeting link in your web browser.
Microphone/Camera Mute (Optional): You can uncomment the commented-out line (#pyautogui.hotkey('ctrl','shift','m')) to automatically mute your microphone upon joining. Explore pyautogui documentation for other mute options.
Meeting Leave: When the current time matches the end time of a lecture, the script simulates the keyboard shortcut (ctrl + shift + b) to exit fullscreen mode and then closes the browser window using (alt + f4).
