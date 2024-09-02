

# List of words
words = ["madam", "aba", "bcb", "hello", "python"]

# Initialize an empty list to store palindromic words
palindromic_words = []

# Loop through each word in the list
for word in words:
    # Check if the word is the same forwards and backwards
    if word == word[::-1]:
        # If it is, add it to the list of palindromic words by concatenation
        palindromic_words += [word]
        
# Print the palindromic words
print("Palindromic words:", palindromic_words)
