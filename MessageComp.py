import os

file = open("gui.asm").read()
t1 = file.split("\n")[6]
t2 = file.split("\n")[7]

def set_text(text = str()):
    global file
    global t1

    new_text = file.replace(t1, "  text db '" + text + "', 0")
    file = open("gui.asm", "w")
    file.write(new_text)
    file.close()
    file = open("gui.asm").read()

def set_title(title = str()):
    global file
    global t2

    new_title = file.replace(t2, "  text2 db '" + title + "', 0")
    file = open("gui.asm", "w")
    file.write(new_title)
    file.close()
    file = open("gui.asm").read()

def compile():
    os.system("fasm gui.asm")
