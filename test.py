import tkinter as tk
field_text = ""
def add_to_field(sth):
    global field_text
    field_text=field_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global field_text
    result=str(eval(field_text))
    field.delete("1.0","end")
    field.insert("1.0",result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0","end")

window=tk.Tk()
window.geometry("300x400")
window.resizable(width=False,height=False)
field = tk.Text(window,height=2,width=21,font=("Arial",20))
field.grid(row=1,column=1,columnspan=4)
window.title("Calculator")
icon = tk.PhotoImage(file="calculator.png")
window.iconphoto(True, icon, icon)

button1 = tk.Button(text="1",font=("Arial",20), command=lambda: add_to_field(1))
button1.place(relx=0.1,rely=0.25,anchor=tk.CENTER)

button2 = tk.Button(text="2",font=("Arial",20), command=lambda: add_to_field(2))
button2.place(relx=0.3,rely=0.25,anchor=tk.CENTER)

button3 = tk.Button(text="3",font=("Arial",20), command=lambda: add_to_field(3))
button3.place(relx=0.5,rely=0.25,anchor=tk.CENTER)

button4 = tk.Button(text="4",font=("Arial",20), command=lambda: add_to_field(4))
button4.place(relx=0.1,rely=0.45,anchor=tk.CENTER)

button5 = tk.Button(text="5",font=("Arial",20), command=lambda: add_to_field(5))
button5.place(relx=0.3,rely=0.45,anchor=tk.CENTER)

button6 = tk.Button(text="6",font=("Arial",20), command=lambda: add_to_field(6))
button6.place(relx=0.5,rely=0.45,anchor=tk.CENTER)

button7 = tk.Button(text="7",font=("Arial",20), command=lambda: add_to_field(7))
button7.place(relx=0.1,rely=0.65,anchor=tk.CENTER)

button8 = tk.Button(text="8",font=("Arial",20), command=lambda: add_to_field(8))
button8.place(relx=0.3,rely=0.65,anchor=tk.CENTER)

button9 = tk.Button(text="9",font=("Arial",20), command=lambda: add_to_field(9))
button9.place(relx=0.5,rely=0.65,anchor=tk.CENTER)

button0 = tk.Button(text="0",font=("Arial",20), command=lambda: add_to_field(0))
button0.place(relx=0.1,rely=0.85,anchor=tk.CENTER)

buttonplus = tk.Button(text="+",font=("Arial",20), command=lambda: add_to_field("+"))
buttonplus.place(relx=0.7,rely=0.25,anchor=tk.CENTER)

buttonminus = tk.Button(text="-",font=("Arial",20), command=lambda: add_to_field("-"))
buttonminus.place(relx=0.7,rely=0.45,anchor=tk.CENTER)

buttonmultiply = tk.Button(text="*",font=("Arial",20), command=lambda: add_to_field("*"))
buttonmultiply.place(relx=0.7,rely=0.65,anchor=tk.CENTER)

buttondiv = tk.Button(text="/",font=("Arial",20), command=lambda: add_to_field("/"))
buttondiv.place(relx=0.9,rely=0.85,anchor=tk.CENTER)

buttonclear = tk.Button(text="CE",font=("Arial",20), command=lambda: clear())
buttonclear.place(relx=0.3,rely=0.85,anchor=tk.CENTER)

buttonequal = tk.Button(text="=",font=("Arial",20), command=lambda: calculate(), width=5)
buttonequal.place(relx=0.6,rely=0.85,anchor=tk.CENTER)

buttonopn = tk.Button(text="(",font=("Arial",20), command=lambda: add_to_field("("))
buttonopn.place(relx=0.9,rely=0.25,anchor=tk.CENTER)

buttoncls = tk.Button(text=")",font=("Arial",20), command=lambda: add_to_field(")"))
buttoncls.place(relx=0.9,rely=0.45,anchor=tk.CENTER)

buttoncomma = tk.Button(text=".",font=("Arial",20), command=lambda: add_to_field("."))
buttoncomma.place(relx=0.9,rely=0.65,anchor=tk.CENTER)

window.mainloop()
