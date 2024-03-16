# concatinate
from codecs import charmap_build


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = a + b

print("concatinated", c)

# list sclicing

t = [4, 19, 45, 67, 34, 78, 90, 100, 112]
slice1 = t[1:3]  # up to but not including index 3
print("slice 1:", slice1)

slice2 = t[:4]  # up to but not including index 4

print("Slice 2:", slice2)

slice3 = t[3:]  # index 3 to the end.

print(slice3)

# List Methods

stuff = list()
stuff.append('book') # add items to the end of the list. 
stuff.append('cookies')
print(stuff)

# Liat comprehension
# This Python script converts a given string in PascalCase or camelCase to snake_case.

def convert_to_snake_case(pascal_or_camel_case_string):
    # This function converts a given string in PascalCase or camelCase to snake_case.
    # It creates a new list of characters, checking each character if it's uppercase.
    # If the character is uppercase, it adds an underscore and converts it to lowercase.
    # If the character is not uppercase, it simply adds the character to the new list.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()  # Add an underscore and convert to lowercase if the character is uppercase
        else char  # Otherwise, keep the character as it is
        for char in pascal_or_camel_case_string
    ]

    # Join the characters in the list back into a single string, removing any leading underscore.
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Call the convert_to_snake_case function with a test string and print the result.
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    # Execute the main function if the script is run directly.
    main()