#		**	fonction qui calcule le produit des élément d'une liste	**

l = [5,8,9,2,4,4,2,1,3,0]


#print(prod(l))

def prod_l(l):
	total = l[0]

	for i in range(len(l)-1):

		
		total = l[i+1] * total

		if l[i] == 0:
			pass

	return total
#


print(prod_l(l))
