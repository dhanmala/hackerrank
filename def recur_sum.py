#def recur_sum(n):
#   if n <= 1:
#       return n
#   else:
#       return n + recur_sum(n-1)   
#print(recur_sum(20))    
# 
   
#def findRoot(x):
#    if ((x*x > n - t) and (x*x <= n + t)):
#        return x
#    else:
#        x = (x + n/x)/2
#        return findRoot(x)
#n=4
#t = 0.0001
#print(findRoot(n))

def recursive(x):
    if x == 0:
        return 0
    else:
        return (x / (x + 1)) + recursive(x-1)
print(recursive(10))       