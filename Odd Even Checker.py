#function
def check_number():
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

#main
num = int(input("Enter a number: "))
check_number()

while True: #loop
    a = input("Run Again?(yes/no): ").strip().lower() 
    if a == "yes":
        print("Confirmed")
        num = int(input("Enter a new number: "))
        check_number()
    else:
        print("Confirmed")
        print("PROGRAM ABORTED")
        break