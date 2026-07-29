#Assignment 2B 
#Oyama Nongcula 
#NNGOYA001
#2025/03/01

text="""Dearest <first_name>
It is with a heavy heart that I inform you of the death of my father,
General Fayk <last_name>, your long lost relative from Mapsfostol.
My father left the sum of <money>USD for us, your distant cousins.
Unfortunately, we cannot access the money as it is in a bank in <country>.
I desperately need your assistance to access this money.
I will even pay you generously, 30% of the amount - <money30>USD,
for your help.  Please get in touch with me at this email address asap.
Yours sincerely
Frank <last_name>"""

first_name=input("Enter first name:\n")
last_name=input("Enter last name:\n")
money=int(input("Enter sum of money in USD:\n"))
country=input("Enter country name:\n")
#Using Replace function to Update the text
money_30=round(money*0.3,1)
text=text.replace("<first_name>",first_name)
text=text.replace("<last_name>",last_name)
text=text.replace("<money>",str(money))
text=text.replace("<money30>",str(money_30))
text=text.replace("<country>",country)
print(" ")
print(text)