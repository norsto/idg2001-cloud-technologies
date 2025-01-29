# Exercise 4 - Creating a Python API
In this exercise, we will both use public APIs using the module `requests` and create a Python API using the Python module `flask`.
We can also use FastAPI or other modules.


**NB! These notes are updated from last year, where we used Flask instead of FastAPI. Therefore, some notes _may_ discuss Flask-stuff instead of FastAPI-stuff. But it should be mostly similar.


## API
I think of an API as a website made for applications, not humans.
They have links, like `api.google.com/something/something_else`.
To communicate with them, we can open the link in a browser, and see the result.
We can also (and should) use tools like TC/Postman.

APIs communicate in a client-server format.
The client requests something from the server, and the server responds.
They usually use data in the JSON format, though they can also use other file formats, like XML and CSV. See `more_about_data_structures.md` for more on this.

### HTTP Methods
When we are talking about APIs, we are often/usually talking about REST APIs.
REST is a standard for how to structure APIs.
It has multiple methods, but the four most important are the *CRUD* methods, which you may remember from learning about databases.

```
+--------------+--------+------+--------+--------+
| DB Method    | Create | Read | Update | Delete |
+--------------+--------+------+--------+--------+
| REST method  | POST   | GET  | PUT    | DELETE |
+--------------+--------+------+--------+--------+
```

## Consume public API
There are many open and public APIs available on the internet. Like [this one](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/).

The first in the list: 7Timer!, can give you the current weather at a given GPS coordinate.

### In the browser
If we go to the following link in our browser, we will get the current weather in Gjøvik.

https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0

Great stuff. Of course, it's not very readable.
It's in JSON format, which is not amazing for reading, but programs like them.
Especially languages like JavaScript and Python.

### Thunder Client (TC) / Postman
To read this data from TC/Postman, we can simply paste the same link into TC/Postman, make sure it's set to GET, and click `Send`.
We should then get the JSON data, in a slightly more readable format.
You may be able to click a few things to make it even more readable.
You can also use the "Thunder Client" in VS Code.

### Python
To load it from Python, we use an external module names `requests`.
We need to install this using the command `pip install requests`.

NB! Check the `requirements.txt` file for the requirements. Or even better, run `pip install -r requirements.txt` to install all at the same time.

Note: It may be `pip3`, not `pip`.
Also, if your system has not added `pip` to path automatically, you may need to tell the system that this is a Python module.
Do this by adding `python -m `before `pip`.
I.e. `python -m pip install requests`.

Once `requests`++ is installed and available, we can use it in Python.
Add the following code in your Python program to read the API data and print it.

```python
import requests


# Link to the API
API_LINK = 'https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'


response = requests.get(API_LINK)
data = response.json()

print(data)
```

Now, if you want to, you can also import the `json` module, and add this to your code, before printing:

```python
data = json.dumps(data, indent=4)
```

Pretty JSON data! :D

See the file `consume_public_API.py` for an example of the program.


## Create API
Creating an API using FastAPI is easy.
We will need to install `fastapi` first, but this can be done is the same way as with `requests` (see description above).

Once we have installed `fastapi`, we can add the following code in a Python file, and run it.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World! :D'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}
```

Launch the server by running the command

```bash
uvicorn example_API:app --reload
```

This is placed in the `example_API.py` file.

We can now run the program, and go to the URL/website which the script prints.
For me, this is `http://127.0.0.1:8000`.
We can also connect to this using Thunder Client/Postman.
There, we should see the `read_root` JSON/dictionary being printed.
Yay! Our first API (maybe).

We can add more paths (now, we are just using root `'/'`).
We can add paths like `'/items'` and more.
To do this, just add more functions, including the decorator (`@app...`).

We can also return something more interesting, like data from a database.
More on this later.

To add other REST methods, see the file `launch_API.py` for examples.
There, I use an internal datastructure called `CONTACTS` to simulate a database.

### Alternative server launching method
The server can either be launched using the bash command in CLI (as seen above), or by including this command into the script. There may be better ways, but at least this works fine.

```python
import subprocess
subprocess.run(['uvicorn', 'example_API:app', '--reload'])
```

If you also include this into an if-block checking if the file is ran, not imported, you will be able to import it more easily at a later point.

```python
if __name__ == '__main__':
    import subprocess
    subprocess.run(['uvicorn', 'example_API:app', '--reload'])
```
