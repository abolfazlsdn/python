def count_vowels(text):


    vowles=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    uniqe_vowles=set()

    for char in text:
        #print(item)
     
        if char in vowles:
            
            count+=1
            uniqe_vowles.add(char)
    return count , uniqe_vowles

