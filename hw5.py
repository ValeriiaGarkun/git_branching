num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
print("Max num: ", max_num)