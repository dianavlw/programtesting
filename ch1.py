def is_unique(str):
    arr = [False] * 128
    for char in str:
        index = ord(char)
        if arr[index]:
            return False
        arr[index] = True
    return True


print(is_unique("yolo") == False)
print(is_unique("rad") == True)
print(is_unique("yOlo") == True)


