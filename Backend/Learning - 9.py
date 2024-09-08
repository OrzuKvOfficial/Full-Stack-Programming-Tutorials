# Aralash turdagi list
my_list = [1, "hello", 3.5, True]

# Har xil turlarga ko'ra tahrirlash
for i in range(len(my_list)):
    if isinstance(my_list[i], int):
        my_list[i] += 10
    elif isinstance(my_list[i], str):
        my_list[i] = my_list[i].upper()
    elif isinstance(my_list[i], float):
        my_list[i] = round(my_list[i])
    elif isinstance(my_list[i], bool):
        my_list[i] = not my_list[i]

# Natijani chop etish
print(my_list)
