import Tkinter as tk

class guiClass(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent= parent
        self.input=""
        tk.Label(self, text="Welcome to Contoso Travel.\nSay new reservation or press 1.\nSay change reservation or press 2.\nSay restaurant recommendation or press 3.").grid(row=0)

        tk.Label(self, text="Selection").grid(row=1)
        
        self.e1= tk.Entry(self)
        self.e1.grid(row=1, column=1)
        
        tk.Button(self, text= "Submit", command= self.setInput).grid(row=2)
    def getInput(self):
        return self.e1.get()
    
    def sendInput(self):
        return self.input
    
    def setInput(self):
        self.input= self.getInput()

root= tk.Tk()
guiClass(root).pack(side="top", fill="both", expand=True)
root.mainloop()
