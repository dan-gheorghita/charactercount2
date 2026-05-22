message = 'It was a bright cold day in April, and the clocks were striking thirteen.'  # The input message

count = {}  # Initialize a dictionary to store character counts

for character in message:  # Iterate over each character in the message
    count.setdefault(character, 0)  # Set a default count to 0 if the character is not already in the dictionary
    count[character] = count[character] + 1  # Increment the count of the current character

print(count)  # Print the character counts