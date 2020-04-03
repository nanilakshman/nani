n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
    
print("reverse of it")

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()        
 
