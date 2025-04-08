def fizzbuzz(start, end):
    result = []  # Initialize an empty list to store results
    
    # Loop over the range from start to end (excluding end)
    for number in range(start, end):
        if number % 3 == 0 and number % 5 == 0:
            result.append("fizzbuzz")  # Append "fizzbuzz" for multiples of both 3 and 5
        elif number % 3 == 0:
            result.append("fizz")  # Append "fizz" for multiples of 3
        elif number % 5 == 0:
            result.append("buzz")  # Append "buzz" for multiples of 5
        else:
            result.append(number)  # Append the number itself if not a multiple of 3 or 5
    
    return result  # Return the resulting list