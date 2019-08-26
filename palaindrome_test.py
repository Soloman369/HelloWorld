s1 = 'Ce satrape repart a sec' # True
s2 = 'Ce satra reparst a sec'  # False



def palindrome_test(l):
    l = l.replace(' ', '')
    l = l.lower()
    m = l[::-1]
    if l == m :
        return l + ' est palindrome'
    else:
        return l + " n'est pas palindrome"
        
print(palindrome_test(s1))
print(palindrome_test(s2))