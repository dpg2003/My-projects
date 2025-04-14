
import re

def CutOneLineTokens(line):
    # Define token types and regex patterns
    token_specification = [
        ('KEY', r'\b(if|else|int|float)\b'),
        ('OP', r'[=+>*]'),
        ('SEP', r'[():;]'),
        ('FLOAT_LIT', r'\b\d+\.\d+\b'),
        ('INT_LIT', r'\b\d+\b'),
        ('STR_LIT', r'"(.*?)"'),
        ('ID', r'[a-zA-Z][a-zA-Z0-9]*'),
        ('SKIP', r'\s+')
    ]

    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    regex = re.compile(token_regex)

    tokens = []
    for match in regex.finditer(line):
        token_type = match.lastgroup
        token = match.group(token_type)
        if token_type == 'SKIP':
            continue
        elif token_type == 'KEY':
            tokens.append(f'<key,{token}>')
        elif token_type == 'OP':
            tokens.append(f'<op,{token}>')
        elif token_type == 'SEP':
            tokens.append(f'<sep,{token}>')
        elif token_type in ('FLOAT_LIT', 'INT_LIT', 'STR_LIT'):
            tokens.append(f'<lit,{token}>')
        elif token_type == 'ID':
            tokens.append(f'<id,{token}>')

    print('Test input string: ', line)
    print('Output <type, token> list: ', tokens, "\n")

# Test cases
CutOneLineTokens('int A1=5')
CutOneLineTokens('float BBB2 =1034.2')
CutOneLineTokens('float cresult = A1 +BBB2 * BBB2')
CutOneLineTokens('if (cresult >10):')
CutOneLineTokens('print("TinyPie")')
