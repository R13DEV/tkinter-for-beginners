from tkinter import*

root = Tk()
root.title("first tkinter app")
root.geometry("400x400")


txt1 = Label(root, text="this is a label").pack()
btn1 = Button(root, text="this is a button")
root.mainloop()