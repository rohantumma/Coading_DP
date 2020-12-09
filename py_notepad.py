from tkinter import *    # import at the very start
from tkinter import filedialog   #use for file open function
from tkinter import messagebox
from tkinter.colorchooser import askcolor   #background and text color functions
import datetime  #import for current_date function
import webbrowser  #import for help function
import tkinter.font    # import for bold italic underline functions
from tkinter.messagebox import askyesno, showwarning, showinfo
import tkinter.ttk
import sys


def New_File():
    if askyesno('Notepad', 'Save Existing Work?'):
        filename = filedialog.asksaveasfilename()
        if filename:
            alltext = text.get(1.0, END)
            open(filename, 'w').write(alltext)

    if askyesno('Notepad', 'Open Existing File?'):
        text.delete(1.0, END)
        file = open(filedialog.askopenfilename(), 'r')
        if file != '':
            txt = file.read()
            text.insert(INSERT, txt)
        else:
            pass
    else:
        text.delete(1.0, END)

def Open_File():
    text.delete(1.0, END)
    file = open(filedialog.askopenfilename(), 'r')
    if file != '':
        txt = file.read()
        text.insert(INSERT, txt)
    else:
        pass

def Save_As():
    filename = filedialog.asksaveasfilename()
    if filename:
        alltext = text.get(1.0, END)
        open(filename, 'w').write(alltext)

def Close():
    root.destroy()

def Copy():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def Paste():
    try:
        teext = text.selection_get(selection='CLIPBOARD')
        text.insert(INSERT, teext)
    except:
        pass

def Replace():
    def replaceall():
        findtext = str(find.get(1.0, END))
        replacetext = str(replace.get(1.0, END))
        alltext = str(text.get(1.0, END))
        alltext1 = all.replace(findtext, replacetext)
        text.delete(1.0, END)
        text.insert('1.0', alltext1)

    replacebox = Tk()
    replacebox.geometry("230x150")
    replacebox.title("Replace..")
    find = Text(replacebox, height=2, width=20).pack()
    replace = Text(replacebox, height=2, width=20).pack()
    replaceallbutton = Button(replacebox, text="Replace..", command=replaceall)
    replaceallbutton.pack()

def Erase():
    sel = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)

def Clear_Screen():
    text.delete(2.0,END) #1.0 indicates line no.
    #Specifying 2.0 will delete only upto line no 2 not line 1

def Current_Date():
    data = datetime.date.today()
    text.insert(INSERT, data)

def Text_Color():
    (triple, color) = askcolor()

    if color:
        text.config(foreground=color)

def No_Format():
    text.config(font=("Arial", 10))

def Bold():
    current_tags = text.tag_names("sel.first")
    if "bt" in current_tags:
        text.tag_remove("bt", "sel.first", "sel.last")
    else:
        text.tag_add("bt", "sel.first", "sel.last")
        text.tag_config("bt", font=("Arial", 10, "bold"))

def Italic():
    text.tag_add("here", "1.0", "1.4")
    text.tag_add("start", "1.8", "1.13")  # use it after explaining 1st tag
    text.tag_config("here", font=("Arial", 10, "italic"))
    text.tag_config("start", background="black", foreground="green") #explain second last

def Underline():
    text.tag_add("here", "1.0", "1.4")
    text.tag_config("here", font=("Arial", 10, "underline"))

def Background():
    (triple, color) = askcolor()

    if color:
        text.config(background=color)

def Online_Help():
    webbrowser.open('https://www.google.com/')

if __name__=="__main__":
    root = Tk()
    root.title("Notepad")
    Main_Menu = Menu(root)
    Commands = Menu(root)
    root.config(menu=Main_Menu)

    Main_Menu.add_cascade(label="File", menu=Commands)
    Commands .add_command(label="New File", command=New_File)
    Commands .add_command(label="Open...", command=Open_File)
    Commands .add_command(label="Save As...", command=Save_As)
    Commands .add_command(label="Close", command=Close)

    Edit_Menu = Menu(root)
    Main_Menu.add_cascade(label="Edit", menu=Edit_Menu)
    Edit_Menu.add_command(label="Copy", command=Copy)
    Edit_Menu.add_command(label="Paste", command=Paste)
    Edit_Menu.add_command(label="Replace", command=Replace)
    Edit_Menu.add_command(label="Delete", command=Erase)
    Edit_Menu.add_command(label="Clear Screen", command=Clear_Screen)

    Insert_in_Menu = Menu(root)
    Main_Menu.add_cascade(label="Insert", menu=Insert_in_Menu)
    Insert_in_Menu.add_command(label="Date", command=Current_Date)

    Change_Format = Menu(root)
    Main_Menu.add_cascade(label="Format", menu=Change_Format)
    Change_Format.add_cascade(label="Font", command=Text_Color)
    Change_Format.add_separator()
    Change_Format.add_radiobutton(label='No Format', command=No_Format)
    Change_Format.add_radiobutton(label='Bold', command=Bold)
    Change_Format.add_radiobutton(label='Italic', command=Italic)
    Change_Format.add_radiobutton(label='Underline', command=Underline)

    Personalize = Menu(root)
    Main_Menu.add_cascade(label="Personalize", menu=Personalize)
    Personalize.add_command(label="BackGround", command=Background)

    User_Help = Menu(root)
    Main_Menu.add_cascade(label="Help", menu=User_Help)
    User_Help.add_command(label="Online", command=Online_Help)

    text = Text(root, height=40, width=100, font=("Arial", 10))
    scrollbar = Scrollbar(root, command=text.yview)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack()
    root.resizable(0, 0)
    root.mainloop()
