#Oyama Nongcula 
#NNGOYA
#12/03/2025

first_num=int(input("Enter first number:\n"))
second_num=int(input("Enter second number:\n"))

first_div=[]
second_div=[]

for i in range(1,first_num):
    if first_num%i==0:
        first_div.append(i)

for j in range(1,second_num):
    if second_num%j==0:
        second_div.append(j)

if sum(first_div)==second_num and sum(second_div)==first_num:
    print(f"{first_num} and {second_num} are amicable numbers.")
else:
    print(f"{first_num} and {second_num} are not amicable numbers.")
