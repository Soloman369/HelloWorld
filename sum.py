import argparse

#Hello_Everybody :)

"""a = float(input("give me a number"))
b = float(input("give me another number"))

c = a + b
print(c)"""



parser = argparse.ArgumentParser()
parser.add_argument("op", type=str)
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)



args = parser.parse_args()




def cal(a,b):
	if args.op == "+":
		return a + b;
	elif args.op == "-":
		return a - b
	elif args.op == "x":
		return a*b
	elif args.op == "/":
		return a/b
	else:
		print("operator not found")

print(cal(args.a, args.b))
