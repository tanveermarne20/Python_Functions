# Basic Methods
original_string = "hello, World!"
capitalized_string = original_string.capitalize()
uppercase_string = original_string.upper()
lowercase_string = original_string.lower()
titlecased_string = original_string.title()

print("Original String:", original_string)
print("Capitalized String:", capitalized_string)
print("Uppercase String:", uppercase_string)
print("Lowercase String:", lowercase_string)
print("Titlecased String:", titlecased_string)

# Substring Methods
prefix_check = original_string.startswith("hello")
suffix_check = original_string.endswith("World!")
substring_index = original_string.find("World")
substring_count = original_string.count("l")

print("Starts with 'hello':", prefix_check)
print("Ends with 'World!':", suffix_check)
print("Index of 'World':", substring_index)
print("Count of 'l':", substring_count)

# Manipulation Methods
replaced_string = original_string.replace("hello", "Hi")
stripped_string = "   spaces around   ".strip()
joined_string = "-".join(["Python", "is", "fun"])

print("Replaced String:", replaced_string)
print("Stripped String:", stripped_string)
print("Joined String:", joined_string)
