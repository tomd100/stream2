
x=1
total=0
while x<=10:
    total = total + x
    x = x + 1

print(total) 

def sumnums(n):
    x = 1
    total = 0
    while x <= n:
        total = total + x
        x = x + 1 
    return total

print(sumnums(1))    


# def contains(x, y, n):
#     if n < x or n > y:
#         return False
    
#     a=0
#     while x<=y:
#         if x==n:
#             a=1
#         x=x+1

#     return a==1

# def contains(x, y, n):
#     if (n < x) or (n > y):
#         return False
    
#     while x<=y:
#         if x == n:
#             return True
#         x = x + 1
#     return False

# def contains(x, y, n):
#     if n < x or n > y:
#         return False
#     else:
#         return True
    

def contains(x, y, n):
    return (n >= x) and (n <= y)

print(contains(1, 4, 1))
   
    