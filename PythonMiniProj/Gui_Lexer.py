from tkinter import *

def inputClick():
    global num
    line_start = f"{num + 1}.0"
    line_end = f"{num + 2}.0"
    current_line = t.get(line_start, line_end).strip()
    if current_line:
        t2.insert(END, current_line + '\n')
        num += 1
    line.config(text="Current line number: " + str(num))

root = Tk()

# Title for the whole program
title = Label(root, text="Lexical Analyzer for TinyPie", bg="lightblue", width=100)
title.grid(row=0, column=0, columnspan=2)

# Input box title
input_text = Label(root, text="Source Code Input")
input_text.grid(row=1, column=0, padx=10, pady=5)

# Output box title
output_text = Label(root, text="Lexical Analyzed Result")
output_text.grid(row=1, column=1, padx=10, pady=5)

# Input box
t = Text(root, width=40, height=15)
t.grid(row=2, column=0, padx=10)

# Output box
t2 = Text(root, width=40, height=15)
t2.grid(row=2, column=1, padx=10)

# Processing line text with counter
num = 0
line = Label(root, text="Current Processing Line: " + str(num))
line.grid(row=3, column=0, pady=5)

# Button for processing the next line
nextButton = Button(root, text="     Next Line     ", command=inputClick, bg="lightgreen")
nextButton.grid(row=4, column=0, pady=5)

# Quit button to terminate the program
quitButton = Button(root, text="     Quit     ", command=root.destroy, bg="lightgreen")
quitButton.grid(row=4, column=1, pady=30)

# Start the main event loop
root.mainloop()
