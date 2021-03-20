# Faulty Calculations
# 45 * 3 = 555
# 56 + 9 = 77
# 56 / 6 = 4

print("Enter the first value")
num1 = float(input())
print("Enter the operator")
op = input()
print("Enter the second value")
num2 = float(input())

# Faulty Calculations
if num1==45 and op=='*' and num2==3:
    print("Your answer is 555")
elif num1==56 and op=='+' and num2==9:
    print("Your answer is 77")
elif num1==56 and op=='/' and num2==6:
    print("Your answer is 4")

# Normal Calculations
elif op=='*':
    print("Your answer is", num1 * num2)
elif op=='/':
    print("Your answer is", num1 / num2)
elif op=='+':
    print("Your answer is", num1 + num2)
elif op=='-':
    print("Your answer is", num1 - num2)

else:
    print("You entered some wrong values!")


