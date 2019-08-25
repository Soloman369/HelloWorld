#		**	fonction qui calcule la somme des élément d'une liste	**

l = [5,8,9,2,4,4,2,1,3,0]


#print(sum(l))

def sum_l(l):
	total = 0
	for i in range(len(l)):
		total = l[i] + total
	return total



print(sum_l(l))



