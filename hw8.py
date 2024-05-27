def find_first_repeating_charater(s):
    char_count= {}
    for char in s:
        if char in char_count:
             print(f"first repeating charater{char}, memory adress:{id(char)}")
             return char, id(char)
        else:
            char_count[char]= 1
    return None

output=find_first_repeating_charater("abcdefgabc")
print(output)
if output is None:
    print("no repeating charater found")

       
    

