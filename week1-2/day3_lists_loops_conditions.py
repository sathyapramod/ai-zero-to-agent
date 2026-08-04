# LIST

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits) # print the list
print(fruits[0]) # print the first item
print(fruits[-1]) # print the last item

fruits.append("fig")
print(fruits)

fruits.remove("banana")
print(fruits)

print(fruits[0:3]) # print the first three items

print(len(fruits)) # print the length of the list

# FOR LOOP

for fruit in fruits:
    print(fruit)

for i in range(1,11):
    print(i)

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# WHILE LOOP

i = 1

while i <= 5:
    print(i)
    i += 1

# Using Break Statement
i = 1

while i <=10:
    if i == 5:
        print("Stopping at 5!")
        break
    print(i)
    i += 1

# Using Continue Statement
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# CONDITION 

# Check if a number is positive, negative, or zero

number = 10

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Check if a person's age makes them a child, teen, or adult
age = 18

if age < 18:
    print("You are a child")
elif age >= 18 and age < 20:
    print("You are an teenager")
else:
    print("You are a adult")

# Check if a fruit is in the list
fruit = "cherry"

if fruit in fruits:
    print(f"{fruit} is in the list")
else:
    print(f"{fruit} is not in the list")

# MINI PROJECT: Grocery List Filter
# 1. Create a list of grocery item names
# 2. Create a matching list of prices for each item
# 3. Loop through both lists using range(len())
# 4. Use if to filter only items under ₹100
# 5. Print each affordable item and its price
# 6. Track and print the total cost of filtered items

