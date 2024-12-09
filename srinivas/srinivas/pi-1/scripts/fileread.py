# Create an empty list to store the words
all_words = []

# Open the file
with open("your_file.txt", "r") as file:
    # Read each line
    for line in file:
        # Split the line into words
        words = line.strip().split(',')
        # Add the words to the list
        all_words.extend(words)
    file.close()
# Print the list
print(all_words)
