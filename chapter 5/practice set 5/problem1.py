
# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!



words = {
    
    "madad":"Help",
    "kursi":"Chair",
    "billi":"Cat",
    "kutta":"Dog",
}

word = input("Enter the word you want meaning of: ")

print("Meaning of ", word , " in English : " ,  words[word]);