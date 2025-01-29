# Exercises

## Problem 1: Python cache from Temu
We are given the function $f(x) = x^2$, which will look like the following in Python.

```python
def f(x):
    return x**2
```

Make the function `cached_f(x)` which uses the function `f(x)`, but remembers previous input and output. First time you run `cached_f(3)` it'll have to calculate using `f(x)`. Second time, it should just return the remembered output from the first time.


## Problem 2: Using Python to parse data files
Whether you are using Google Contacts or Apple's contacts, you probably have some contacts stored somewhere. Just to both follow GDPR and not require anyone to use specific file types, we will use a sample file found [here](https://www.phpclasses.org/browse/file/5543.html). This program should, however, support other files of the same type/setup (but focus on that once the other parts have been implemented).

### About the file(s)
The vCard files (.vcf) are a plain text file, which has the following structure

**This is what we want to read from the file:**

```
BEGIN:VCARD
KEY1:VALUE1
KEY2:VALUE2
END:VCARD
BEGIN:VCARD
KEY1:VALUE1
KEY2:VALUE2
END:VCARD
```

except that the KEY-values and VALUE-values will have more sensible values.

**This is what we wan't to store in the output file:**

```json
[
    {
        KEY1: VALUE1,
        KEY2: VALUE2
    },
    {
        KEY1: VALUE1,
        KEY2: VALUE2
    }
]
```

The file `sample.vcf` includes only _one_ contact, making it somewhat easier than `sample-1.vcf`, which includes _multiple_ contacts.

### Teacher's solutions
I made three solutions:
1. Solution-1.py: Supports _one_ contact per file.
2. Solution-2.py: Support _multiple_ contacts per file.
3. Solution-3.py: From last year. Same as 2, but different method. Also removes "`BEGIN`" and "`END`" from dict. Also adds a key-replacement, so "`EMAIL;TYPE=INTERNET`" will be replaced with "`email`", among others. More complex.

### About solving the problem
You can find my solution, as well as tips on how to solve the task in other files here. Try to solve it yourself, though. That way you'll learn more!
