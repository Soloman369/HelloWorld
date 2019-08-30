import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=int)
args = parser.parse_args()

#a = int(input("donnez une valeur pour a"))



def fact(a):
	if a == 1:
		return 1
	elif a > 1:
		return fact(a-1)*a
	else:
		print("sorry souleiman")

print(fact(args.a))
