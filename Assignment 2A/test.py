#Oyama Nongvula
#NNGOYA001
#2025/03/06

#Collecting Variabls
import math as m
A_val=float(input("Enter the value of A:\n"))

Act_E=float(input("Enter the value of activation energy, E_a:\n"))

Temp=float(input("Enter the value of T:\n"))

k_val=m.exp(-(Act_E/(8.3145*Temp)))*A_val

print(f"The rate constant, k, is {round(k_val)}.")