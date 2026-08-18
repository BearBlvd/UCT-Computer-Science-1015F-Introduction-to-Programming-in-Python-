#Oyama Nongcula
#NNGOYA001
#15/03/2025
     
is_Building=True
while is_Building:

    try:
        start_num=int(input("Enter the starting number (n):\n"))
    except Exception:
        print("Invalid input. Please enter integers.")
        continue
    try:
        row=int(input("Enter the number of rows (r):\n"))
        col=int(input("Enter the number of columns (c):\n"))
    except Exception:
        print("Invalid input. Please enter integers.")
        continue

    if row<0 or col<0:
        print("Rows and columns must be positive integers.")
        continue

    for i in range(row):
        str_row_grid=[f"{start_num+i*col+j:3}"for j in range(col)]
        print(" ".join(str_row_grid))

    is_Building=False
