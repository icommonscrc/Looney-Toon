# Looney-Toon
Author: Michael Galloway, Linh Vu
Description: Shift changing with Looney Toon (feel free to make it sound better)

Requirements:
1. Python latest version
2. python -m pip install opencv-python
3. python -m pip install pillow

How to use it with Task Scheduler:
1. Create Task
2. In General Tap, name the task and store in your prefer location.
3. In Triggers Tap, select "New". Set your prefer start time, repeatation, etc.
4. In Actions Tap, select "New".

a. Program/script: select "{PATH}\python.exe". Try "where python" to get the PATH.

b. Add arguments (optional): "{PATH}\OpenVideoAtTimeV8.py"

c. Start in (optional): "{PATH}". PATH is the location of the whole folder (containing the script, video, pictures).
