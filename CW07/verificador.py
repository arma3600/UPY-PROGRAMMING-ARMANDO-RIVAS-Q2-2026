

# Ask the user for the identification number
rol_number = input("Enter the identification number (only numbers): ")

# Reverse the string 
reversed_rol = ""
for character in rol_number:
    reversed_rol = character + reversed_rol

# Variables for the math loop
total_sum = 0
multiplier = 2

# Loop through each number to multiply and sum
for digit in reversed_rol:
    number = int(digit)
    result = number * multiplier
    total_sum = total_sum + result
    
    # Increase multiplier, reset if it goes past 7
    multiplier = multiplier + 1
    if multiplier > 7:
        multiplier = 2

# Calculate the remainder 
remainder = total_sum % 11

# Calculate the final verification digit
final_digit = 11 - remainder

# Check special cases 
if final_digit == 11:
    print("The complete number is: " + rol_number + "-0")
elif final_digit == 10:
    print("The complete number is: " + rol_number + "-K")
else:
    print("The complete number is: " + rol_number + "-" + str(final_digit))