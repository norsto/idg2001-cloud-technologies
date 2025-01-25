# Wolfram Alpha Plaintext to Markdown Converter
> Difficulty: Medium to hard (depending on how much of the problem you do).

When using Wolfram Alpha, and asking for the Step-by-step solution, you get the option to download as plaintext. For the problem

$$3x + 6 = 0$$

([Link](https://www.wolframalpha.com/input?i=3x+%2B+6+%3D+0).)


## Input
The plaintext ends up looking like the following

```raw
Solve for x:
3 x + 6 = 0

Hint: | Isolate terms with x to the left hand side.
Subtract 6 from both sides:
3 x + (6 - 6) = -6

Hint: | Look for the difference of two identical terms.
6 - 6 = 0:
3 x = -6

Hint: | Divide both sides by a constant to simplify the equation.
Divide both sides of 3 x = -6 by 3:
(3 x)/3 = (-6)/3

Hint: | Any nonzero number divided by itself is one.
3/3 = 1:
x = (-6)/3

Hint: | In (-6)/3, divide 6 in the numerator by 3 in the denominator.
6/3 = (3×2)/3 = 2:
Answer: | 
 | x = -2
```

**NB!** This is copy/pasted exactly. Notice newlines and spaces.

## Requirements
We want to convert this text to Markdown. We want to support the following requirements.
- Hints: Lines starting with "Hint:" are hints, and should use start with `>` (quote formatting).
- Text: Lines with text, which ends with ":", are explenations, and should be regular text.
- Answer: Where lines starts with "Answer: |", where next line starts with " |" are answers, and the "Answer" should be bold, and a new paragraph.
    - Optional (medium): Add a `>` before every answer-line.
- Math: Lines with maths (E.g., includes "=", but does not end with ":") should be placed in Latex math formatting (within "$$").
    - Optional (hard): Support fractions (`a/b -> frac{a}{b}`), including brackets.

NB! Remember to add empty lines certain places, as Markdown sometimes ignores single newlines / "`\n`" as.


## Output
This should then end up looking like the following.

---

Solve for x:
$$3 x + 6 = 0$$

> Isolate terms with x to the left hand side.

Subtract 6 from both sides:
$$3 x + (6 - 6) = -6$$

> Look for the difference of two identical terms.

6 - 6 = 0:
$$3 x = -6$$

> Divide both sides by a constant to simplify the equation.

Divide both sides of 3 x = -6 by 3:
$$(3 x)/3 = (-6)/3$$

> Any nonzero number divided by itself is one.

3/3 = 1:
$$x = (-6)/3$$

> In (-6)/3, divide 6 in the numerator by 3 in the denominator.

6/3 = (3×2)/3 = 2:
> **Answer:**
> $$x = -2$$

---


## Possible input/output setups
Three possible setups for the input and output:
- Make an input- and output file, read the input, process, and store the markdown in the output file.
- Use the input-function to paste in the plaintext, process, and print the result out in the console.
- Use the `pyperclip` module to directly access the clipboard (copy/paste) to modify the plaintext in memory.

Either way, make sure the processing happens in a function which takes in plaintext (str) and returns markdown (str). The loading and saving should be their own section of the code.
