# Python Path Resolver

## Problem 1
When we have a path and a subpath and we want to merge them, we can do this in multiple different ways. Take the following two paths

```python
home_dir = '/users/You'
sub_dir = 'Code/File.py'
```

If we want to merge them into the full path, we can just add them (string concatenation). We would have to do a couple of checks, though:

- Does the first string end in a slash? Does the last string begin with a slags? Are both or neither of these true?
    - If both: We would get `/users/You//Code...` with a double slash.
    - If neither: We would get `/users/YouCode...` with no slashes.
    - If exactly one of them is true, we would get a single slash, like we want.
    - These scenarios would have to be checked.
- Is it unix slashes (`/`) or Windows slashes (`\`)?
    - Either is fine, but you want to make sure the tests support either. And maybe even a combination?
    - A simple solution-ish: Replace one slash with another slash.

__Problem:__
Make a tool to combine two strings like this. Include checks for types of slashes and number of slashes. Your code may want you to write `\\`, not `\`, since this slash is also the escape symbol in Python strings.


## Problem 2
(Read problem 1 first.)

A more difficult thing to solve is the problem of the sub_dir (a relative path) may include a `..`. We are given the following two paths.

```python
home_dir = '/users/You/Downloads'
sub_dir = '../Code/File.py'
```

Here, we jump _out_ of the `Downloads` folder, and into the `Code` folder instead. Merging them properly will give us the following path.

```python
full_path = '/users/You/Downloads/../Code/File.py'
```

But the `..` should effectively remove the `Downloads` path.

__Problem:__
Make a function which takes a path as a string, and resolves this "`..`"-ing and gives us the following path.

```python
full_path = '/users/You/Code/File.py'
```


## Built-in modules
We have built-in paths which can fix all of this for us, and normally, we should preferrably use those. Less work for us, and less possibility to mess up. The following two modules have relevant functions.

- `os.path`: Includes simple functions to check if file exists and more.
- `pathlib`: Includes a lot of functions allowing us to deal with paths, including `resolve`.
