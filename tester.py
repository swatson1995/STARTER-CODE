#def count(lst):
#    
#    even = 0
#    odd = 0
#    
#    for i in lst :
#        if i%2==0:
#            even += 1
#        else:
#            odd += 1
#    return even,odd
#
#lst = [555,100000,3000,445,3,5,7,9]
#
#
#even, odd= count(lst)
#
#print('number of even nums: {}\nnumber of odd nums:{}'.format(even,odd))
#
####################################################################################
#def fact(n):
#    x=1
#    for i in range(1,(n+1)):
#        x = i*x
#        
#    return x
#
#
#
#x = 1200
#
#result= fact(x)
#print(result)
#######################################################################################
#import sys 
#print(sys.getrecursionlimit)
#sys.setrecursionlimit(1000)
#i = 0
#
#def greet():
#    global i    
#    i += 1
#    print('hello world', i)
#    greet()
#
#    
#    
#greet()

#################################################################################
#
#
#f = lambda a,b : a+b
#
#result = f(6,5)
#
#print (result)


######################################################################
from functools import reduce


numb = [1,1,1,2,5555555,2,2,2,3,3,4,54,5,6,4,23,234,35,324,5,42,5,4516,43,41,5,4,6]


evens = list(filter(lambda n : n%2 == 0,numb))

odds = list(filter(lambda n : n%2 == 1, numb))

doubles = list(map(lambda n:n*2, evens))

sum = reduce(lambda a,b : a+b ,doubles)

print(odds)
print(evens)
print(doubles)
print(sum)

###################################################################################


