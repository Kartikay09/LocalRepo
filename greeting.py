import tkinter as tk

root =tk.Tk()
root.geometry('2000x1000')
root.title("Greeting App")


class greetingApp:
    def __init__(self,mainwindow):
        self.mainwindow =mainwindow

        tk.Label(root, text= 'Enter your name').pack()
        self.name = tk.Entry(mainwindow)
        self.name.pack()
        tk.Button(mainwindow , text ='Enter',command=self.action).pack()

        self.out = tk.Label(mainwindow, text='')
        self.out.pack()

    def action(self):
        data = self.name.get()
        self.out.config(text = 'Hello,' + data)
        self.name.delete(0, tk.END)

exe = greetingApp(root)
root.mainloop() 