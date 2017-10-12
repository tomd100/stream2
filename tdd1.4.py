


def even_number_of_evens(numbersList):
    numberEvens = sum([int(i % 2 == 0) for i in numbersList])
    return numberEvens % 2 == 0 and numberEvens > 0
    
    
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("all pass")

def even_number_of_evens2(numbersList):
    numberEvens = sum([1 for i in numbersList if i % 2 == 0])
    return numberEvens % 2 == 0 and numberEvens > 0
    
assert even_number_of_evens2([]) == False, "No numbers"
assert even_number_of_evens2([2]) == False, "One even number"
assert even_number_of_evens2([2, 4]) == True, "Two even numbers"
assert even_number_of_evens2([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens2([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens2([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens2([1, 3, 9]) == False, "No even numbers"
    
print("all pass")    
