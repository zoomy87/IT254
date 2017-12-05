#@authors: Joel Schmidt and Eric Zumbahlen

import Tkinter as tk

#initializes gui and sets button and text entry

class guiClass(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.input=""
        tk.Label(self, text="Welcome to Contoso Travel.\nSay new reservation or press 1.\nSay change reservation or press 2.\nSay restaurant recommendation or press 3.").grid(row=0)

        tk.Label(self, text="Selection").grid(row=1)
        
        self.e1= tk.Entry(self)
        self.e1.grid(row=1, column=1)
        
        button1= tk.Button(self, text= "Submit", command= self.setInput)
        button1.grid(row=2)
        #command= self.setInput
        
    #returns what was typed into text field
    def getInput(self):
        return self.e1.get()
    
    #prints to console
    def printInput(self):
        print self.input
    
    #returns the input variable
    def sendInput(self):
        return self.input
    
    #sets what was entered into input variable and prints to console
    def setInput(self):
        self.input= self.getInput()
        print self.input

#root= tk.Tk()
#guiClass(root).pack(side="top", fill="both", expand=True)
#root.mainloop()
