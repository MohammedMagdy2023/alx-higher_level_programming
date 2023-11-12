#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        replacements = ['.', '?', ':']
        for char in replacements:
            text = text.replace(char, char + '\n\n')
        lines = text.split('\n')
        lines = [line.strip() for line in lines]
        text = '\n'.join(lines)
        print(text)
