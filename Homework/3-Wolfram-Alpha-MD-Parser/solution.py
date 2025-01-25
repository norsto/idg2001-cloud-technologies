input_text = '''Solve for x:
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
 | x = -2'''


def convert_to_markdown(text):
    # Simple replaces.
    text = text.replace('Hint: |', '>')
    text = text.replace('Answer: | ', '> **Answer:**')
    text = text.replace('\n | ', '\n> ')

    # Make empty string, split lines and iterate through them.
    new_text = ''
    lines = text.split('\n')
    for line in lines:
        # If math expression, add $$ around it.
        if '=' in line and not line.endswith(':'):
            line = f'$${line}$$'

        # Add updated line to new_text, including newline.
        new_text += line + '\n'

        # Add newline after each hint.
        if line.startswith('>'):
            new_text += '\n'
    
    # Remove extra newline for answer.
    new_text = new_text.replace('> **Answer:**\n\n$$> ', '> **Answer:**\n> $$')
    return new_text
        
print(convert_to_markdown(input_text))


'''
Copy result into a new file/editor, select "Markdown" as the language, and
preview the result. Then you'll see if it looks correct. Compare to the
README.md preview.
'''
