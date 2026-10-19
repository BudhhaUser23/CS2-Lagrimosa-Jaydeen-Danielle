# Travel Fare Calculator
# With Input Validation Code
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

if name.strip() == "":
    print("Please enter your name.")
    name = input("Enter passenger name: ")
    
if not 0 <= int(distance):
    print("Please enter the distance you are going to travel.")
    distance = float(input("Enter distance (km): "))
    
if not 0 <= int(passengers):
    print("Please enter the number of passengers.")
    passengers = int(input("Enter number of passengers: "))
    
total_fare = distance * FARE_RATE * passengers
print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
