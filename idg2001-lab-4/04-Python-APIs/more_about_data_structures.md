# More about different formats to structure data in

Okay, so there are an infinite number of different ways to format data in, but there are some very popular formats we will look at a few examples of:

* JSON
* XML
* YAML
* CSV

## JSON
JSON, or JavaScript Object Notation, works well with JavaScript and Python, as they use more or less the same syntax as JavaScript Objects and Python Dictionaries.

```JSON
{
    "users": [
        {
            "name": "Andrew"
        },
        {
            "name": "Mary"
        },
        {
            "name": "John"
        }
    ]
}
```

The file does not have to be split into multiple lines, like this, but is often a single looong line. However, that's difficult to read, so we often show it like above.

## XML
XML files are closely related to HTML files, and use basically the same syntax.
We can store the same data in the following way.

```XML
<users>
    <name>Andrew</name>
    <name>Mary</name>
    <name>John</name>
</users>
```

## YAML
YAML are similar to JSON, but with more of a Python-like syntax.

```YAML
- user one
    name: Andrew

- user two
    name: Mary

- user three
    name: John
```

## CSV
CSV files, or Comma Separated Values, are great for data which would fit neatly in an Excel sheet.
It is _great_ for data which fits nicely into columns and rows.
Otherwise, not so great.

```CSV
id, name
0, Andrew
1, Mary
2, John
```

Ps. this is shown with spaces after the comma.
This is not really the standard, but I do it because I want to.
Some CSV files will use other separators, like `;` or a tab.

## Conclusion
Lots of file formats.
Go to YouTube or something, and watch a comparison between them.
You may mostly use JSON, but it's nice to know about other formats.
