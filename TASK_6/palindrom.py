# List of words
words = ["madam", "aba", "bcb", "hello", "python"]

# Initialize an empty list to store palindromic words
palindromic_words = []

# Loop through each word in the list
for i in words:
    # Check if the word is the same forwards and backwards
    if i == i[::-1]:
        # If it is, add it to the list of palindromic words by concatenation
        palindromic_words += [i]

# Print the palindromic words
print("Palindromic words:", palindromic_words)
