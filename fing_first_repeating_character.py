def find_first_repeating_character(s):
    char_count = {}
    for char in s:
        # Check if character already encountered
        if char in char_count:
            # Print the repeating character along with its memory address
            print("First repeating character:", char, "Memory address:", id(char))
            return char, id(char)
        else:
            # Store the count of the character
            char_count[char] = 1
    # If no repeating character found, return None
    return None

# Example usage:
string = "abcdefghija"
result = find_first_repeating_character(string)
if result is None:
    print("No repeating character found.")