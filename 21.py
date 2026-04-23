import os
import random

print("Welcome to 21")

Mccv1 = random.randint(1,10)
Mccv2 = random.randint(1,10)
Mplcv1 = random.randint(1,10)
Mplcv2 = random.randint(1,10)


def mains(ccv1,ccv2,plcv1,plcv2):
	ccvt = ccv1+ccv2
	print("Opponent's Cards:")
	print(ccv1)
	print(" ")
	print(" ")
	print("Your Cards:")
	print("Showing: ",plcv1)
	print("Hidden: ",plcv2)
	plhc = hitreg()

	if plhc == 1:
		plcv1 = plcv1+random.randint(1,10)

	elif ccvt < 17:
		ccv1 = ccv1 + random.randint(1,10)
	return ccv1,ccv2,plcv1,plcv2,plhc

def hitreg():
	plch = input("Hit or Stay?\n")
	if plch == "Hit":
		plhv = 1
	elif plch == "hit":
		plhv = 1
	elif plch == "h":
		plhv = 1
	elif plch == "H":
		plhv = 1
	elif plch == "Stay":
		plhv = 0
	elif plch == "stay":
		plhv = 0
	elif plch == "s":
		plhv = 0
	elif plch == "S":
		plhv = 0
	else:
		print("Try again")
	return plhv
def gloop(Cv1,Cv2,Pv1,Pv2):
	varlist = mains(Cv1,Cv2,Pv1,Pv2)
	clis, plis, neg = varlist[:2], varlist[2:], varlist[4:]
	neg = int(neg[0])
	Gccv1, Gccv2 = clis[:1], clis[1:]
	Gpcv1, Gpcv2 = plis[:1], plis[1:]
	Gccv1 = int(Gccv1[0])
	Gccv2 = int(Gccv2[0])
	Gpcv1 = int(Gpcv1[0])
	Gpcv2 = int(Gpcv2[0])
	Gcct = Gccv1 + Gccv2
	Gpct = Gpcv1 + Gpcv2
	if Gpct > 21:
		print("You went bust\nYou lose")
		ploop()
	elif Gcct > 21:
		print("The dealer went bust\nYou win!")
		ploop()
	elif neg == 0:
		if Gcct < 16:
			Gccv1 = Gccv1 + random.randint(1,10)
			gloop(Gccv1,Gccv2,Gpcv1,Gpcv2)
		elif Gpct > Gcct:
			print("You win!")
			ploop()
		elif Gcct > Gpct:
			print("You lose")
			ploop()
		else:
			print("Tie")
			ploop()
	else:
		gloop(Gccv1,Gccv2,Gpcv1,Gpcv2)
def ploop():
	pc = input("Play Again?\nY/N\n")
	if pc == "Y":
		pco = 1
	elif pc == "y":
		pco = 1
	elif pc == "Yes":
		pco = 1
	elif pc == "yes":
		pco = 1
	elif pc == "N":
		pco = 0
	elif pc == "n":
		pco = 0
	elif pc == "No":
		pco = 0
	elif pc == "no":
		pco = 0
	else:
		print("Invalid input")
	if pco == 1:
		gloop(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
gloop(Mccv1,Mccv2,Mplcv1,Mplcv2)
