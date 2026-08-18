#Oyama Nongcula
#NNGOYA001
#12/03/2025
number=int(input("Enter a number:\n"))
proper_divsiors=[]
pd=""
for i in range(1,number):
    if number % i ==0:
        proper_divsiors.append(i)

for divisor in proper_divsiors:
        pd=pd+str(divisor)+" "

if sum(proper_divsiors)==number:
    print(f"The proper divisors of {number} are:\n{pd}")
    print(f"\n{number} is a perfect number.")
else:
    print(f"The proper divisors of {number} are:\n{pd}")
    print(f"\n{number} is not a perfect number.")
