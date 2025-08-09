# for file handling
import os

# to convert string to dictionary
import ast

# import all classes from tkinter
from tkinter import *

# import ttk class from tkinter
from tkinter import ttk

# for message box
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel

# for color box
from tkinter.colorchooser import askcolor

#for save data
# when id and password both box is empty
def save_idpaserror_message():
    return askokcancel(title = "Error", message = "your have not given your id and password", icon = "error")  

# when id box is empty
def save_iderror_message():
    return askokcancel(title = "Error", message = "your have not given your id", icon = "error")  

# when password box is empty
def save_paserror_message():
    return askokcancel(title = "Error", message = "your have not given your password", icon = "error") 

# for delete data 
# when id box is empty
def delete_iderror_message():
    return askokcancel(title = "Error", message = "your have not given your id", icon = "error")   

# for update data 
# when id and password box is empty
def update_idpaserror_message():
    return askokcancel(title = "Error", message = "your have not given your id and password", icon = "error") 
# when id box is empty
def update_iderror_message():
    return askokcancel(title = "Error", message = "your have not given your id", icon = "error")  
# when password box is empty
def update_paserror_message():
    return askokcancel(title = "Error", message = "your have not given your password", icon = "error") 

# for search data 
# when id box is empty
def search_iderror_message():
    return askokcancel(title = "Error", message = "your have not given your id", icon = "error")   

# function definition for saving data
def saveData():
    text_id = var_id.get()
    text_pas = var_pas.get()
    var_ok_save = True
    if not var_id.get() and not var_pas.get():
        var_ok_save = save_idpaserror_message()
    elif not var_id.get():
        var_ok_save = save_iderror_message()   
    elif not var_pas.get():
        var_ok_save = save_paserror_message()
    if var_ok_save == False:
        return
    text = {text_id : text_pas}
    file_name = "IdDatabase.txt"
    if os.path.exists(file_name):
        with open(file_name, 'a') as f:
            f.write(str(text) + "\n")
    else:
        with open(file_name, 'w') as f:   
            f.write(str(text) + "\n")  

# function for cancel to clear screen
def cancelData():
    ent_id.delete(0, END)
    ent_pas.delete(0, END)  

# delete any password
def deleteData():
    var_ok_delete = True
    if not var_id.get():
        var_ok_delete = delete_iderror_message()   
    if var_ok_delete == False:
        return
    flag = False    
    with open('IdDatabase.txt','r') as f:
        lines = f.readlines()
    with open('IdDatabase.txt','w') as f:
        for line in lines:
                temp_dict = ast.literal_eval(line.strip())
                if temp_dict.get(var_id.get()) or temp_dict.get(var_id.get()) == '':
                    flag = True
                    continue
                else:
                    f.write(str(temp_dict) + "\n")
        if flag == False:
            var_pas.set("no id found")  

# search any password
def searchData():
    var_ok_search = True
    if not var_id.get():
        var_ok_search = search_iderror_message()   
    if var_ok_search == False:
        return
    with open('IdDatabase.txt','r') as f:
        for line in f.readlines():
                temp_dict = ast.literal_eval(line.strip())
                if temp_dict.get(var_id.get()):
                    var_pas.set(str(temp_dict.get(var_id.get())))
                    return
                elif temp_dict.get(var_id.get()) == "":
                    var_pas.set("password doesn't exist")
                    return      
        else:
            var_pas.set("no id found")  

# update any password
def updateData():
    var_ok_update = True
    if not var_id.get() and not var_pas.get():
        var_ok_update = update_idpaserror_message()  
    elif not var_pas.get():
        var_ok_update = update_paserror_message()
    elif not var_id.get():
        var_ok_update = update_iderror_message()   
    if var_ok_update == False:
        return
    flag = False  
    with open('IdDatabase.txt','r') as f:
        lines = f.readlines()
    with open('IdDatabase.txt','w') as f:
        for line in lines:
                temp_dict = ast.literal_eval(line.strip())
                if temp_dict.get(var_id.get())or temp_dict.get(var_id.get()) == '':
                    flag = True
                    con = {var_id.get() : var_pas.get()}
                    f.write(str(con) + "\n")
                else:
                    f.write(str(temp_dict) + "\n")
        if flag == False:
            var_pas.set("this id doesn't exist")

# to clear all data
def clearData():
    os.remove("IdDatabase.txt")

# to exif from win
def exitfromwin():
    win.destroy()

# to change color win window
def backcolor():
    ans = askcolor(title = "Color box")
    lab.config(bg = ans[1])   

# Toggle password visibility
def togglePasswordVisibility():
    if var_show_hide.get() == 1:
        ent_pas.config(show="*")  # Hide password
    else:
        ent_pas.config(show="")  # Show password    

# show all password and id
def showData(): 

    top = Toplevel()   
    
     # to stop resizable function of screen
    top.resizable(False, False)
       
    # change title of window
    top.title("python")

    # to change logo of window
    #top.iconbitmap("D:\\self programming\\project\\project py\\python project\\id store manager\\python-logo.ico")

    # to change transparency of window
    top.attributes("-alpha", 1)

    # change colour of output window
    top["bg"] = "lightgreen"
 
    # to change color top window
    def topbackcolor():
        ans = askcolor(title = "Color box")
        lab_new.config(bg = ans[1])   

    def deletetext():
        text_box.delete('1.0', 'end')    

    # menu box 
    me1 = Menu(top)
    top.config(menu = me1)

    # menu box for edit
    me1_edit = Menu(me1, tearoff = 0)
    me1_edit.add_command(label = "clear screen", command = deletetext)
    me1_edit.add_separator()
    me1_edit.add_command(label = "exit", command = top.destroy)
    me1.add_cascade(label = "Edit", menu = me1_edit)

    # menu box for setting
    me1_setting = Menu(me1, tearoff = 0)
    me1_setting.add_command(label = "background colour", command = topbackcolor)
    me1_setting.add_separator()
    me1_setting.add_command(label = "clear all data", command = clearData)
    me1.add_cascade(label = "setting", menu = me1_setting)  

    # to set screen width
    width = 800
    height = 500
    sys_wid = top.winfo_screenwidth()
    sys_hei = top.winfo_screenheight()
    c_x = int(sys_wid/2 - width/2)
    c_y = int(sys_hei/2 - height/2)
    top.geometry(f"{width}x{height}+{c_x}+{c_y}")   

    # remains top window up on win window
    top.transient(win)

    # making label of id provider
    lab_new = LabelFrame(top, text = "EMAIL ID STORE", font = ("Times New Roman",20,"bold", "underline"), labelanchor = "n", relief = "groove", cursor = "target")
    lab_new.config(bg = "Yellow", fg = "Red") 
    lab_new.pack(padx = 10, pady = 10, ipadx = 0, ipady = 0, expand = True, fill = "both")
    
    # text box for show id and password
    text_box = Text(top, height = 10, width = 45, font = ("Times New Roman",20,"bold"))
    text_box.place(relx = 0.1, rely = 0.15)

    # open file and retrieve data from file
    if os.path.exists("IdDatabase.txt"):
        with open('IdDatabase.txt','r') as f:
            all_line = f.readlines()
            for line in all_line:
                temp_dict = ast.literal_eval(line.strip()) 
                for x, y in temp_dict.items():
                    text_box.insert(END, x + " --> " + y + "\n") 
    else:
        line = "no data available!!"
        text_box.insert(END, line) 

    # scroll bar of text_box in top window 
    scroll = Scrollbar(top, orient= "vertical", command = text_box.yview, cursor = "hand2")  
    scroll.place(relx = 0.867, rely = 0.15, height = 316.3, width = 20) 
    text_box['yscrollcommand'] = scroll.set 

    # back all task button for id
    back_show = Button(top, text = "back", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = top.destroy)
    back_show.place(x = 270, y = 420, height = 40, width = 260)

# about gui
def aboutguime():
    top_gui = Toplevel()   
    # to stop resizable function of screen
    top_gui.resizable(False, False)
       
    # change title of window
    top_gui.title("python")

    # to change logo of window
    #top_gui.iconbitmap("D:\\self programming\\project\\project py\\python project\\id store manager\\python-logo.ico")

    # to change transparency of window
    top_gui.attributes("-alpha", 1)

    # change colour of output window
    top_gui["bg"] = "lightgreen"

    # to set screen width
    width = 800
    height = 520
    sys_wid = top_gui.winfo_screenwidth()
    sys_hei = top_gui.winfo_screenheight()
    c_x = int(sys_wid/2 - width/2)
    c_y = int(sys_hei/2 - height/2)
    top_gui.geometry(f"{width}x{height}+{c_x}+{c_y+10}")  

    # making label of email provider
    lab = LabelFrame(top_gui, text = "EMAIL ID STORE", font = ("Times New Roman",20,"bold", "underline"), labelanchor = "n", relief = "groove", cursor = "target")
    lab.config(bg = "Yellow", fg = "Red") 
    lab.pack(padx = 10, pady = 10, ipadx = 0, ipady = 0, expand = True, fill = "both") 

    style = ttk.Style()
    style.configure("TFrame", background = "lightgreen")
    
    # notebook in top_gui window
    note = ttk.Notebook(top_gui)
    note.place(x = 50, y =60, height = 380, width = 700)

    frame1 = ttk.Frame(note, style = "TFrame")
    frame1.pack(fill = "both", expand = True)
    note.add(frame1, text = "About GUI")

    label_gui = Label(frame1, text = "About GUI", font = ("Times New Roman",20,"bold", "underline"), relief = "flat", cursor = "target", bg = "brown", fg = "white")
    label_gui.place(x = 280, y = 20)

    label_gui_content = Label(frame1, text = 'Hello Users\nthis is a gui application which is made from tkinter.\nit can store your email id and password.', font = ("Times New Roman",20, "bold"), relief = "flat", cursor = "target", bg = "lightgreen", fg = "black")
    label_gui_content.place(x = 70, y = 100, height = 150)

    frame2 = ttk.Frame(note, style = "TFrame")
    frame2.pack(fill = "both", expand = True)
    note.add(frame2, text = "About me")

    label_me = Label(frame2, text = "About me", font = ("Times New Roman",20,"bold", "underline"), relief = "flat", cursor = "target", bg = "brown", fg = "white")
    label_me.place(x = 280, y = 20)

    label_me_content = Label(frame2, text = 'NIKHIL KUMAR\nB.TECH (CSE - AI)\nUIET, CSJMU KANPUR', font = ("Times New Roman",20, "bold"), relief = "flat", cursor = "target", bg = "lightgreen", fg = "black")
    label_me_content.place(x = 210, y = 100, height = 150)

    # remains top_gui window up on win window
    top_gui.transient(win)

    # back all task button for id
    back_show = Button(top_gui, text = "back", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = top_gui.destroy)
    back_show.place(x = 270, y = 450, height = 40, width = 260)


# make object window of Tk classs
win = Tk()

# change title of window
win.title("python")

# to change logo of window
#win.iconbitmap("D:\\self programming\\project\\project py\\python project\\id store manager\\python-logo.ico")

# to change transparency of window
win.attributes("-alpha", 1)

# change colour of output window
win["bg"] = "lightgreen"

# menu box 
me = Menu(win)
win.config(menu = me)
# menu box of option
me_file = Menu(me, tearoff = 0)
me_file.add_command(label = "save data", command = saveData)
me_file.add_command(label = "search data", command = searchData)
me_file.add_command(label = "show all data", command = showData)
me_file.add_separator()
me_file.add_command(label = "update data", command = updateData)
me.add_cascade(label = "File", menu = me_file)

# menu box for edit
me_edit = Menu(me, tearoff = 0)
me_edit.add_command(label = "delete data", command = deleteData)
me_edit.add_command(label = "clear screen", command = cancelData)
me_edit.add_separator()
me_edit.add_command(label = "exit", command = exitfromwin)
me.add_cascade(label = "Edit", menu = me_edit)

# menu box for setting
me_setting = Menu(me, tearoff = 0)
me_setting.add_command(label = "background colour", command = backcolor)
me_setting.add_separator()
me_setting.add_command(label = "clear all data", command = clearData)
me.add_cascade(label = "Setting", menu = me_setting)

# menu box for about
me_about = Menu(me, tearoff = 0)
me_about.add_command(label = "about GUI", command = aboutguime)
me.add_cascade(label = "About", menu = me_about)

# to set screen width
width = 800
height = 500
sys_wid = win.winfo_screenwidth()
sys_hei = win.winfo_screenheight()
c_x = int(sys_wid/2 - width/2)
c_y = int(sys_hei/2 - height/2)
win.geometry(f"{width}x{height}+{c_x}+{c_y}")

# making label of email provider
lab = LabelFrame(win, text = "EMAIL ID STORE", font = ("Times New Roman",20,"bold", "underline"), labelanchor = "n", relief = "groove", cursor = "target")
lab.config(bg = "Yellow", fg = "Red") 
lab.pack(padx = 10, pady = 10, ipadx = 0, ipady = 0, expand = True, fill = "both")

# label for id
lab_id = Label(win, text = "Enter Your Email Id", font = ("Times New Roman",20,"bold"), bg = "Yellow", fg = "red", cursor = "Plus", justify = "center")
lab_id.place(x = 270, y = 90, height = 40, width = 240)

# entry box for id
var_id = StringVar()
ent_id = Entry(win, font = ("Times New Roman",20), bg = "white", cursor = "plus", bd = 8, textvariable = var_id)
ent_id.place(x= 190, y = 130, height = 45, width = 400)

# label for password
lab_pas = Label(win, text = "Enter Your password", font = ("Times New Roman",20,"bold"), bg = "Yellow", fg = "red", cursor = "Plus", justify = "center")
lab_pas.place(x = 260, y = 200, height = 40, width = 280)

# entry box for password
var_pas = StringVar()
ent_pas = Entry(win, font = ("Times New Roman",20), bg = "white", cursor = "plus", bd = 8, textvariable = var_pas)
ent_pas.place(x= 281, y = 240, height = 44, width = 240)

var_show_hide = IntVar()
# Show password radio buttons
rad_bt1 = Radiobutton(win, bg="yellow", font=("Times New Roman", 15), cursor="hand2", text="hide", value=1, variable=var_show_hide, command=togglePasswordVisibility)
rad_bt1.place(x=525, y=235)

# Hide password radio buttons
rad_bt2 = Radiobutton(win, bg="yellow", font=("Times New Roman", 15), cursor="hand2", text="show", value=2, variable=var_show_hide, command=togglePasswordVisibility)
rad_bt2.place(x=525, y=259)

# separator to seperate button and entry box
style = ttk.Style()
style.configure("TSeparator",
                thickness = 0.1,
                relief = "groove",
                background = "black"
                )
sep = ttk.Separator(win, orient = "horizontal", style="TSeparator")
sep.place(x = 50, y = 320, width = 700)

# save button for id
save = Button(win, text = "save", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = saveData)
save.place(x = 60, y = 350, height = 40, width = 210)

# cancel button for id
cancel = Button(win, text = "cancel", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = cancelData)
cancel.place(x = 295, y = 350, height = 40, width = 210)

# delete button for id
delete = Button(win, text = "delete", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = deleteData)
delete.place(x = 530, y = 350, height = 40, width = 210)

# search button for id
search = Button(win, text = "search", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = searchData)
search.place(x = 60, y = 420, height = 40, width = 210)

# update all task button for id
update = Button(win, text = "update", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = updateData)
update.place(x = 295, y = 420, height = 40, width = 210)

# show all task button for id
show = Button(win, text = "show", font = ("Times New Roman",20,"bold"), bg = "red", fg = "white", cursor = "hand2", justify = "center", relief = "groove", bd = 8, command = showData)
show.place(x = 530, y = 420, height = 40, width = 210)

# to stop resizable function of screen
win.resizable(False, False)

# run loop
win.mainloop()