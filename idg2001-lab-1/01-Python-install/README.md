# Setting up Python with VS Code
*Copied from lecture 03.*


## Version
Python exists in Python 2.xyz and 3.xyz. Use 3. Not 2. Version 2 is outdated and deprecated. Version 3.7 should probably be new enough, but if you going to install, just pick the latest version. (Press the big button on the download page.)


## Installation
0. Install VS Code.

1. Google Python, find the Python download page, and download the latest version. (Press the big button on the download page.)

2. __Important for Windows__ If on Windows, when installing, you will be asked if you want to add Python as PATH. Yes. You __do__ want this.

3. Otherwise, install, next, next, yes, continue, etc. Easy install.

4. When done, open/reopen VS Code.

5. (Optional) Open the terminal (or PowerShell) and run `python`. If it opens the Windows Store, close it and retry one of the following commands in the terminal:
    - `python`
    - `python3`
    - `py`

    If any of them shows something like the following, Python is working. Run `exit()` and press enter to close it.

```python
Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

6. In VS Code, make a new file. Language: Python, or file extension: `.py`

7. In the bottom right, a pop-up should open, asking if you want to install the Python extension in Code. Yes, you want this.

8. When installed, a Play/Run button should pop up in the top right interface of VS Code. Press it, and a terminal should open.

9. Add the following Python code, and re-run.

```python
print("Hello, World!")
```

If it worked, it should print out `Hello, World!`. Congratulations! You just wrote your first Python program.

If not, hmmm, not sure. Ask a friend?
