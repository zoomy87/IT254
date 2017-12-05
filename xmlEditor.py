# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 22:59:53 2017

@authors: Joel Schmidt and Eric Zumbahlen
"""
import Tkinter as tk
from BeautifulSoup import BeautifulStoneSoup as Soup
from gui2 import guiClass 

root= tk.Tk()
gui= guiClass(root)
root.mainloop()

xml = """
  <menu id="main">
       <prompt>
            Welcome to Contoso Travel.
            Say new reservation or press 1.
            Say change reservation or press 2.
            Say restaurant recommendation or press 3.
       </prompt>
       <choice1 dtmf="1" next1="#new_reservation">
          new reservation
       </choice1>
       <choice2 dtmf="2" next2="change-reservation.vxml">
          change reservation
       </choice2>
       <choice3 dtmf="3" next3="restaurant.vxml" accept="approximate">
          restaurant recommendation
       </choice3>
   </menu>

"""
"""
Start XML manipulation section.
"""
soup = Soup(xml)
choice1 = soup.menu.choice1
choice2 = soup.menu.choice2
choice3 = soup.menu.choice3
#choice1['next1'] = 'Thank you for your new reservation!'
#choice2['next2'] = 'Thank you for changing your reservation!' 
#choice3['next3'] = 'Searching restaurants in your area!' 
"""
Start user choice logic flow.
"""

userChoice= gui.sendInput(gui)
print userChoice
if userChoice == 1:
    choice1['next'] = 'Thank you for your new reservation!'
elif userChoice == 2:
    choice2['next2'] = 'Thank you for changing your reservation!' 
elif userChoice == 3:
    choice3['next3'] = 'Searching restaurants in your area!' 
else:
    print "No choice selected. Hanging up."
"""
Show updated XML file.
"""
print soup
