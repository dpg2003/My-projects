
import tkinter as tk
import re

class TinyLexerApp:
    def __init__(self, root):
        self.root = root
        self.line_counter = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("TinyLexer Analyzer")
        tk.Label(self.root, text="TinyLexer Lexical Analyzer", bg="#90caf9", width=80, font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Source Code").grid(row=1, column=0, pady=5)
        tk.Label(self.root, text="Lexical Tokens").grid(row=1, column=1, pady=5)

        self.input_box = tk.Text(self.root, width=45, height=20, font=('Courier', 10))
        self.input_box.grid(row=2, column=0, padx=10)

        self.output_box = tk.Text(self.root, width=45, height=20, font=('Courier', 10))
        self.output_box.grid(row=2, column=1, padx=10)

        self.line_label = tk.Label(self.root, text=f"Current Line: {self.line_counter}")
        self.line_label.grid(row=3, column=0, pady=5)

        tk.Button(self.root, text="Analyze Line", command=self.process_line, bg="#aed581").grid(row=4, column=0, pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#ef9a9a").grid(row=4, column=1, pady=5)

    def process_line(self):
        start = f"{self.line_counter + 1}.0"
        end = f"{self.line_counter + 2}.0"
        line_text = self.input_box.get(start, end).strip()

        if line_text:
            tokens = self.tokenize(line_text)
            for token in tokens:
                self.output_box.insert(tk.END, token + '\n')
            self.output_box.insert(tk.END, '\n')
            self.line_counter += 1
            self.line_label.config(text=f"Current Line: {self.line_counter}")

    def tokenize(self, line):
        specs = [
            ('KEY', r'\b(if|else|int|float)\b'),
            ('OP', r'[=+>*]'),
            ('SEP', r'[():;]'),
            ('FLOAT', r'\b\d+\.\d+\b'),
            ('INT', r'\b\d+\b'),
            ('STRING', r'"(.*?)"'),
            ('ID', r'[a-zA-Z][a-zA-Z0-9]*'),
            ('SKIP', r'\s+')
        ]
        pattern = '|'.join(f'(?P<{name}>{regex})' for name, regex in specs)
        regex = re.compile(pattern)

        result = []
        for match in regex.finditer(line):
            type_ = match.lastgroup
            value = match.group()
            if type_ == 'SKIP':
                continue
            tag = 'key' if type_ == 'KEY' else                   'op' if type_ == 'OP' else                   'sep' if type_ == 'SEP' else                   'lit' if type_ in ('FLOAT', 'INT', 'STRING') else                   'id'
            result.append(f"<{tag},{value}>")
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = TinyLexerApp(root)
    root.mainloop()
