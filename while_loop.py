''' l1 =["Rohan","Sohan","Sachin","Rahul"]
for name in l1:
    if name.startswith("S"):
        print("Hello " + name) 
num = int(input("Enter the number:"))
prime = True
for i in range(2,num):
    if(num%i==0):
        prime = False
        break
if prime:    
    print("This number is prime")        
else:
    print("This number is not prime")   
'''
n = int(input())
i = 0
for i in range(0, 5):
    print(i**2)