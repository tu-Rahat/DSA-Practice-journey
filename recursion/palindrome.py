x='ANBCDDCBNA'
'''
2 pointer logic
'''
def palindrome(x,l,r):
    if l>=r:
        return True
    else:
        if x[l] == x[r]:
            return palindrome(x,l+1,r-1)
        else:
            return False 
        
print(palindrome(x,0,len(x)-1))