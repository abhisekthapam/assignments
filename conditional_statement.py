#Conditional Statements:
number = int(input("Enter the number: "))

if number % 5 ==0 and number % 3 == 0:
    print("Fizzbuzz")
elif number % 3== 0:
    print("Fuzz")
elif number % 5== 0:
    print("Fz")
else:
    print("Hey you----")

    

month = ["January", "February","March","April","May","June","July","August","Spetember","October","NOvember","December"]
number=int(input("Enter the number: "))
if number==1:
    print(f"The month is {month[0]}.")
elif number==2:
    print(f"The month is {month[1]}.")
elif number==3:
    print(f"The month is {month[2]}.")
elif number==4:
    print(f"The month is {month[3]}.")
elif number==5:
    print(f"The month is {month[4]}.")
elif number==6:
    print(f"The month is {month[5]}.")
elif number==7:
    print(f"The month is {month[6]}.")
elif number==8:
    print(f"The month is {month[7]}.")
elif number==9:
    print(f"The month is {month[8]}.")
elif number==10:
    print(f"The month is {month[9]}.")
elif number==11:
    print(f"The month is {month[10]}.")
elif number==12:
    print(f"The month is {month[11]}.")
else:
    print("The number is out of range----->You FoooooL...")

    
# Accept any city from the user and display monument of the city.
# | City          A
# | Kathamdnu -->    A
# | Delhi     -->   Fort
# | Agra      -->    Taj

city = input("(The options are Kathmandu,Delhi,Agra)Enter the city name: ")
if city == "Kathmandu":
    print("A")
elif city == "Delhi":
    print("Fort")
elif city == "Agra":
    print("Taj")
else:
    print("Choose from options... Read first You -----> Fool")





'''Write a program to accept two numbers and mathematical operators and perform operation accordingly.
Hint:
    1st number=7
    2nd number = 8
    operation = +
    Result = 7+8=15
'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operator = input("Operators(+,-,*,/)--> Choose the operator: ")
if operator =="+":
    print(f"The answer is {first+second}.")
elif operator =="-":
    print(f"The answer is {first-second}.")
elif operator =="*":
    print(f"The answer is {first*second}.")
elif operator =="/":
    print(f"The answer is {first/second}.")

else:
    print("Choose the operator correctly.")
