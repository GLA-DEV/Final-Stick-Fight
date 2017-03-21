#Code par GLA ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ’Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã‚Â¢ÃƒÂ¢Ã¢â‚¬Å¡Ã‚Â¬Ãƒâ€¦Ã‚Â¡ÃƒÆ’Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©2016
#v0.9(beta)
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import sys,os
from winsound import *
import time

fen2 = Tk()
fen2.title=('credits')
fen2.minsize(width="50", height="50")

fen2.iconbitmap('favicon.ico')

credit = LabelFrame(fen2, text="financÃ© par BETMAX !", padx=20, pady=20)
canvas = Canvas(credit)
canvas.pack()

photo = PhotoImage(file="baton Fight.gif")
canvas.create_image(190, 200, image=photo)


credit.pack(fill="both", expand="yes")

Label(credit, text="un jeux cree par 3 jeunes ignorants  ").pack()
Button(credit, text="jouer", command=fen2.destroy).place(x=150, y=45)

fen2.mainloop()


