import re 

s = 'My phone number is 0640660955 , the old one was 0781509909'
output1 = re.findall(r'\w+',s)
output2 = re.findall(r'\d+',s)
output = []

for i in output1:
	if i not in output2:
		output.append(i)

print(output)
print(output2)

print(re.findall(r'\D+',s)) # this is another solution



