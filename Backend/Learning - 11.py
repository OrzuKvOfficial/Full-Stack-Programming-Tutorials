nested_list = [[1, 2], [3, 4], [5, 6]]

# 1-usul: "itertools.chain" yordamida
from itertools import chain
flattened = list(chain.from_iterable(nested_list))
print(flattened)  # Natija: [1, 2, 3, 4, 5, 6]

# 2-usul: Oddiy tsikl yordamida
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Natija: [1, 2, 3, 4, 5, 6]
