def join_strings(strings):
    new_string=""
    for string in range(len(strings)):
        new_string+= strings[string]
        if string <len(strings)-1:
            new_string+=","
    return new_string
    
    
     