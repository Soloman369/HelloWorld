import tkinter as tk
import random

win = tk.Tk()

win.title('My first GUI')


	
def Dice():
	return tk.Label(win, text = random.choice(range(1,7))).pack()

tk.Button(win, text='Générer', command = Dice).pack()

win.mainloop()