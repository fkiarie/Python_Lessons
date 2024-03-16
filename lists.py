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

#List compreensions

def convert_to_snake_case(pascal_or_camel_case_string):
    snake_cased_char_list = [

        '_'+ char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_case_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))

if __name__ == '__main__':
    main()