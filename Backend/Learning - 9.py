my_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Birinchi qadam: barcha ichki listlarni tekislaymiz (flat)
flat_list = [item for sublist in my_list for item in sublist]

# Yig'indi
total = sum(flat_list)
print("Yig'indisi:", total)
