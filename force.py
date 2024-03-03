import abc
import aifc
from cmath import acosh


print("Newtons second law of motion")
print("----------------------------------------")

#Determine the missing value
print("select the missing value:")
print("1. mass (m)")
print("2. acceleration (a)")
print("3. force (f)")
missing_value_choice = input("Enter the option number for the missing value: ")

# prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    f = float(input("Enter force (f): "))
    m = f / a
    print(f"Mass (m) = {m}")

elif missing_value_choice == "2":
    m = float(input("Enter mass (m): "))
    f = float(input("Enter force (f): "))
    a = f / m
    print(f"acceleration (a) = {a}")

elif missing_value_choice == "3":
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    f = m * a
    print(f"force (f) = {f}")

else:
    print("Invalid option selected fot the missing value.")
