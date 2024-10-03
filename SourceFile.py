# Module 1

print("hissssss...")
print("\"I'm\"\n\"\"learning\"\" \n\"\"\"Python\"\"\"")
print()

# Module 2

print(2+2) # Addition
print(2-2) # Subtraction
print(2*2) # Multiplication
print(2**2) # to the power of(2^2)
print(2/2) # Division (Result is a float)
print(2//2) # Division (result is an integer)


# Section 2.6:

#Input function
var = input()
print("you typed:", var)

# Concatenating using plus sign
print("string" + "string")

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you")
print("\nYour name is " + fnam + " " + lnam + ".")
print()

# String Replication
print("Example" * 3)
print(3 * "Example")

# Estimated time an event will end
hour = int(input("Starting time (hours): ")) #hour:mins
mins = int(input("Staring time (minutes): ")) # hour: mins
dura = int(input("Event Duration (Minutes: "))

#displays your inputs
print("Inputs:", hour, mins, dura)

# Does the calculations for minutes/hours
time_mins = (mins + dura%60)%60
time_hours = (hour + dura // 60 + (mins + dura%60) // 60)%24

# Prints the results
print("If an event starts at", hour, ":", mins, "\nthen it will end at")
print(str(time_hours) + ":" + str(time_mins))
print()

#Module 3

# does the calculations for minutes/ hours being less than 100
n = int(input("Enter an integer: "))
print(n >= 100)

#while True:
#   print("You are Gay!")
