# Putting a Python program on Railway.app

Last time we made a Python API. Now, we will make it run on our Railway cloud platform. But first, we can make sure that a simple Python script is running.

## Simple Python script
The following code print `'Hello, Railway! :D'` to the console (or railway logs when online). It will then wait for 5 seconds. And this will be repeated 50 times.

```python
import time

for _ in range(50):
    print('Hello, Railway! :D')
    time.sleep(5)
```

Copy the code into a file called `main.py`, so Railway will understand which file to execute. First, run it offline and make sure it works.

## Setting up Railway
There are two-ish ways to set this up. You can:

1. Use an empty/template project
2. Create your own folder and link it manually.

I do the latter, though generally you should connect it to a GitHub repository.

Some of these steps are only necessary for the API setup, but not for the simple script. Like adding `requirements.txt`, `Procfile` and copying the last line. (See below.)

I got some code/text from the Flask template project on Railway.app, and so should you. [This is the template repo](https://github.com/forgery810/flask-railway).

You can also find parts of this guide at [Railway.app's CLI guide](https://docs.railway.app/develop/cli).

### Install Railway.app (if not already isntalled)
Only one of the following:
```
brew install railway
npm i -g @railway/cli
curl -fsSL https://railway.app/install.sh | sh
scoop install railway
```

### Log in and set up
CD to your local project folder:
```
cd /path/to/project
```
Or just open terminal at that folder.

Then log in and link with the railway command.
```
railway login
railway link [project-ID]
```
The `project-ID` can be found on the project dashboard on Railway.app.

### Do dev
You should probably be using virtual environments (`venv`), though it is not necessary. I din't this time.
It is at least a good for bigger projects. Just like a GitHub connection.

* Make/copy `main.py`
    - Copy the last line, though (and add import `os`)
* Copy `requirements.txt` (or copy an updated from my files)
* Copy `Procfile`

(Copy from the Flask template repo linked above.)

### Opening the API to the internet
[More info here](https://docs.railway.app/deploy/exposing-your-app).

### Launch and read logs
To start the server
```
railway up
railway logs
```
Now you should see the `Hello, Railway! :D`, if you are running that script. If you are running the API, go to the URL (after exposing it using the link above), and the GET should work.

### Take down from Railway
```
railway down
```

### Allow POST++ to work using Postman
My Postman didn't want to POST or DELETE, but I managed it by changing the request settings by turning on the `Follow original HTTP Method` option.
