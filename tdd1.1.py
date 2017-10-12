

def count_upper_case(message):
    if not isinstance(message, str):
        return 0
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

# print(count_upper_case("Here is a message with some text and some CAPITALS and a FEW more"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("$%^&") == 0, "Only special caracters"
assert count_upper_case("ABCDEF") == 6, "6 Upper Case"
assert count_upper_case("AbCD") == 3, "3 Upper Case"
assert count_upper_case(1) == 0, "Numeric value"
assert count_upper_case(["A"]) == 0, "char list"
assert count_upper_case([1]) == 0, "numeric list"
assert count_upper_case([1,2]) == 0, "numeric list"
assert count_upper_case("A\r\nA") == 2, "carrage return char"
assert count_upper_case("A\bA") == 2, "backspace char"
assert count_upper_case("A\tA") == 2, "backspace char"

print("All tests pass")
        
