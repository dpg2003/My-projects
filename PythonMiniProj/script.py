
import re

def match_patterns(strings):
    patterns = {
        "An integer": r'^\d+$',
        "A float consists of 1 or more digits before and after decimal point": r'^\d+\.\d+$',
        "A float with exactly 2 digits after the decimal point": r'^\d+\.\d{2}$',
        "A float ending with letter f": r'^\d+\.\d+f$',
        "Capital letters, followed by small case letters, followed by digits": r'^[A-Z]+[a-z]+\d+$',
        "Exactly 3 digits, followed by at least 2 letters": r'^\d{3}[a-zA-Z]{2,}$'
    }
    for string in strings:
        matched = False
        for pattern_name, pattern in patterns.items():
            if re.match(pattern, string):
                print(f'"{string}" matches the pattern: {pattern_name}')
                matched = True
        if not matched:
            print(f'"{string}" does not match any pattern.')

def remove_leading_integer(s):
    match = re.match(r'^(\d+)\s*(.*)', s)
    if match:
        integer_part = match.group(1)
        remaining_string = match.group(2)
        print(f'Found integer {integer_part} at the beginning of this string, starting at index 0 ending at index {len(integer_part) - 1}. The rest of the string is: {remaining_string}')
    else:
        print(f'No leading integer found in: {s}')

# Test cases for matching patterns
test_strings = ["22.11", "23", "66.7f", "123abcde", "Case44", "Happy", "78", "66.7", "yes123", "Book111"]
match_patterns(test_strings)

# Test cases for removing leading integers
remove_leading_integer("22 street")
remove_leading_integer("90years")
remove_leading_integer("NoNumberHere")
