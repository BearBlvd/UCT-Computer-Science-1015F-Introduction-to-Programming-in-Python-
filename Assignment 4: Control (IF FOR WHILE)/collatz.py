#Oyama Nongcula
#NNGOYA001
#13/03/2025

Number=input("Enter a positive integer:\n")
try:
    inumber=int(Number)
except Exception:
    print("Invalid input. Please enter a valid integer.")
    exit()
num_list=[inumber]
num_string=""
if inumber<=0:
    print("Please enter a positive integer.")
    exit()
while inumber!=1 :
#Checking if number is even or odd
    if inumber%2==0:
        inumber=inumber/2
        num_list.append(int(inumber))
    else:
        inumber=3*inumber+1
        num_list.append(int(inumber))
for str_number in num_list:
    num_string=num_string+str(str_number)+" "

print(num_string)
