# --- Variables ---
name = "Samuel"
age = 25
height = 5.9
is_learning = True

# --- Checking types ---
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_learning)) # <class 'bool'>

# --- f-strings (formatted strings) ---
print(f"My name is {name} and I am {age} years old.")
print(f"My height is {height} feet.")
print(f"Currently learning Python: {is_learning}")

# --- Type conversion: int, float, str ---
age_as_string = str(age)
print(f"Age as string: '{age_as_string}', type: {type(age_as_string)}")

price = "19.99"
price_as_float = float(price)
print(f"Price as float: {price_as_float}, type: {type(price_as_float)}")

whole_number = int(price_as_float)
print(f"Price as int (truncated): {whole_number}")

# --- Mini exercise: try it yourself ---
# 1. Create a variable called 'city' with your city name
# 2. Create a variable called 'population' with a number
# 3. Print an f-string like: "I live in {city}, population {population}"
# 4. Convert population to a string and print its type
