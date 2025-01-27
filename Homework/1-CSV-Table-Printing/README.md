# Parsing
> Difficulty: Easy to medium

Make a script similar to `cat`, but instead of just printing the file content, it should load a CSV-file, and print it as a pretty table. It should support many rows.


## CSV-example
```csv
Index,FirstName,LastName,Phone
01,Paul,Knutson,123-45-678
02,Erna,Solberg,876-54-321
03,Barack,Obama,555-123-4567
```

NB! In the example file there is no empty lines! You may add support for this, if you'd like.

## Expected table
(But feel free to use other standards.)
```
+-------+-----------+----------+--------------+
| Index | FirstName | LastName | Phone        |
+-------+-----------+----------+--------------+
| 01    | Paul      | Knutson  | 123-45-678   |
| 02    | Erna      | Solberg  | 876-54-321   |
| 03    | Barack    | Obama    | 555-123-4567 |
+-------+-----------+----------+--------------+
```


## Easy
- Just use a static column width of 15 or 20 characters.

## Medium
- Center the index column. (Use built-in functions.)
- Allow for different symbols for vertical (`|`), horizontal (`-`) and junction (`+`) pieces.
    - The function creating the table can take in these as optional/default values.
- Support more columns than shown above (arbitrarily many).

## Hard
- Find the necessary column width and use that. Based it on both the headers and the values.
