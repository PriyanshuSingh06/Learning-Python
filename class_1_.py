 
'''string = (input())
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)'''

# str = input("Enter: ")
# str = str.lower()
# inp = input("Enter the Word: ")
# counter = str.count(inp)
# print(counter)
string = (input())
sum = 0
i = 0
for i in range(0,len(string)):
    if(string[i].isnumeric()):
        sum+=int(str[i])
print(sum)        
000