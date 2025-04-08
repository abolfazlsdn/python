def filter_messages(messages):
   def filter_messages(messages):
    # Create the two empty lists to return
    filtered_messages = []
    counts_removed = []
    
    # Iterate over each message in the input list
    for message in messages:
        # Split the message into a list of words
        words = message.split()
        
        # Create a new empty list for non-bad words
        non_bad_words = []
        
        # Initialize a counter for bad words
        counter = 0
        
        # Iterate over each word in the message
        for word in words:
            if word == "dang":
                # Increment the counter if the word is "dang"
                counter += 1
            else:
                # Add the word to the non-bad word list if it's not "dang"
                non_bad_words.append(word)
        
        # Join the list of non-bad words into a single string
        clean_message = ' '.join(non_bad_words)
        
        # Append the new clean message to the filtered messages list
        filtered_messages.append(clean_message)
        
        # Append the count of bad words removed to the counts list
        counts_removed.append(counter)
    
    # Return the filtered messages and the counts of bad words removed
    return filtered_messages, counts_removed

# Example usage
messages = [
    "This is a dang test message",
    "Another dang message with dang words",
    "No bad words here"
]

filtered, counts = filter_messages(messages)
print("Filtered Messages:", filtered)  # Output: ['This is a test message', 'Another message with words', 'No bad words here']
print("Counts of Removed Words:", counts)  # Output: [1, 2, 0]

