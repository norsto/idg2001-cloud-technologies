# Hints (from 2023)

Here are some hints for how to solve the problem. Try first. Use Google or DuckDuckGo. Don't read the hints before trying. :(

## Relative paths
In VS Code, the run-path is not the `.py`-file, but the main folder. If your python file is in `03-Python/program.py` and your `.vcf`-file is `03-Python/sample.vcf`, you may have to open `03-Python/sample.vcf`, not `sample.vcf`. Possibly.

## Reading files
There are multiple ways to read files (which you can google). The way I usually use, is the following:

```python
with open('filename.txt', 'r') as f:
    text = f.read()
```

Using `with` means you don't have to close the file after reading or writing, which you are probably going to forget anyway.

## Splitting
You can read one and one line in, but the way I would solve this, is by splitting the text from the file into contacts, rather than lines.
The text-part between each user is used to split the text below.

```python
user_strings = text.split('\nEND:VCARD\nBEGIN:VCARD\n')
```

Splittlig like this, you get one string per contact, and so you can iterate over them by doing something like:

```python
for user_string in user_strings:
    print(user_string)
```

Next problem to solve: The first and last value in the list will have some lines you may not want. Just print, and you'll see what I mean.

## Creating the data structures
Make empty lists and empty dicts, then fill them up one item/line/contact at the time.
```python
contacts = []
for user_string in user_strings:
    contact = {}
    # ...
    for line in lines:  # 'lines' does not exist yet, so create it above.
        # ...
        contact[key] = value  # 'key' and 'value' does not exist yet, so create them above.
    contacts.append(contact)
```

## Saving
We want to store the results as a JSON format. This can be done manually, by creating a string, and adding curly brackets, and such. You'll learn a lot from doing it this way, but you can also just use the `json` module.

```python
import json

json_string = json.dumps(list_of_user_dicts_or_whatever)
```

Now you can simply store `json_string`, and it'll be a JSON file. :D You can also add `indent=2` as an argument in the `json.dumps` function call. That way, the JSON file will be more easily readable.
