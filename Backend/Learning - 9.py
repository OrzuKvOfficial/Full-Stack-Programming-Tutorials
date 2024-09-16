import os

# Papka va fayllarni ko'rsatish
for root, dirs, files in os.walk("."):  # "." joriy katalogni bildiradi
    for name in files:
        print(os.path.join(root, name))
