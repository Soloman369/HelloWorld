#		**	fonction qui calcule le produit des élément d'une liste	**

l = [5,8,9,2,4,4,2,1,3]


#print(prod(l))

def prod_l(l):
	total = 1

	for i in range(len(l)):

		
		total = l[i] * total

		if l[i] == 0:
			pass

	return total
#


print(prod_l(l))
