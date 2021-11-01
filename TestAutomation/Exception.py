try:
    user_input1= input("Pls Enter your first number")
    user_input2= input("Pls Enter your second number")
    c = int(user_input1) + int(user_input2)
    print(c)
except:
    print("Given input is incorrect, kindly provide right values")
finally:
    print("This is my final code")