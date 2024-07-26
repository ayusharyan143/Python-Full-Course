word = "ayushfromgoogle"

# 1. Get the length of the string
length = len(word)  # Output: 14

# 2. Convert all characters to lowercase
lowercase_word = word.lower()  # Output: "ayushfromgoogle"

# 3. Convert all characters to uppercase
uppercase_word = word.upper()  # Output: "AYUSHFROMGOOGLE"

# 4. Remove leading and trailing whitespace (not applicable here but shown for example)
stripped_word = word.strip()  # Output: "ayushfromgoogle"

# 5. Split the string into a list of substrings (using 'o' as the delimiter for example)
split_word = word.split('o')  # Output: ["ayushfr", "mg", "", "gle"]

# 6. Replace occurrences of a substring with another substring
replaced_word = word.replace("google", "openai")  # Output: "ayushfromopenai"

# 7. Find the index of the first occurrence of a substring
index_of_r = word.find('r')  # Output: 6

# 8. Join elements of a list into a single string
joined_word = "-".join(["ayush", "from", "google"])  # Output: "ayush-from-google"

# 9. Format the string by substituting placeholders with specified values
formatted_word = "Hello, {}".format(word)  # Output: "Hello, ayushfromgoogle"

# 10. Check if the string starts with 'ayush' and ends with 'google'
starts_with_ayush = word.startswith("ayush")  # Output: True
ends_with_google = word.endswith("google")    # Output: True

# Print all results
print(f"Length: {length}")
print(f"Lowercase: {lowercase_word}")
print(f"Uppercase: {uppercase_word}")
print(f"Stripped: {stripped_word}")
print(f"Split: {split_word}")
print(f"Replaced: {replaced_word}")
print(f"Index of 'r': {index_of_r}")
print(f"Joined: {joined_word}")
print(f"Formatted: {formatted_word}")
print(f"Starts with 'ayush': {starts_with_ayush}")
print(f"Ends with 'google': {ends_with_google}")
