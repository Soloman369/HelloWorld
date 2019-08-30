import random
import tkinter
import tkmessagebox

s = range(2)

def p_o_f():
	if random.choice(s) == 0:
		return "Pile"
	else:
		return "Face"