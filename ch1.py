def is_unique(str):
    arr = [False] * 128
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        arr[index] = True
    return True

def is_unique_sorting(str):
    sorted_string = sorted(str)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

print(is_unique("yolo") == False)
print(is_unique("rad") == True)
print(is_unique("yOlo") == True)


print(is_unique_sorting("yolo") == False)
print(is_unique_sorting("rad") == True)
print(is_unique_sorting("yOlo") == True)

