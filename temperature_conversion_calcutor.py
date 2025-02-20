# TASK: Write a program that converts a temperature from Celsius to Fahrenheit.

# Greet the user and ask what temperature type they want to find
print("Hello, and welcome to the temperature conversion calculator")
temp_type = input("What temperature do you want to find? [F/C]").strip().upper()
# Prompt the user to enter a temperature 
temp = int(input(f"Enter the temperature: "))

# Convert the Celsius temperature to Fahrenheit using the formula
if temp_type == "F":
    converted_temp = temp * (9/5) + 32

# Convert the Fahrenheit temperature to Celsius using the formula
else:
    converted_temp = (temp - 32) * (5/9)

# Display the converted temperature
print(converted_temp,temp_type)