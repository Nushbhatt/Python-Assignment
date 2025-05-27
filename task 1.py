num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

sum_result = num_1 + num_2
sub_result = num_1 - num_2
mul_result = num_1 * num_2

if num_2 != 0:
    div_result = num_1 / num_2
    print("Addition: ", num_1, "+", num_2, "=", sum_result)
    print("Subtraction: ", num_1, "-", num_2, "=", sub_result)
    print("Multiplication: ", num_1, "*", num_2, "=", mul_result)
    print("Division: ", num_1, "/", num_2, "=", div_result)
else:
    print("Error: Cannot divide by zero.")