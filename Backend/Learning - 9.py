import re

def filter_code_blocks(text):
    # Kod bloklarini qidiradigan regex
    code_block_pattern = r"```(.*?)```|'''(.*?)'''|\"\"\"(.*?)\"\"\""
    
    # Matndan kod bloklarini ajratib olish
    code_blocks = re.findall(code_block_pattern, text, re.DOTALL)

    # Har bir topilgan kod blokini qayta ishlash yoki filtrlash (bu yerda shunchaki ularni yig'amiz)
    filtered_code = []
    for block in code_blocks:
        # 'block' turli uslubdagi uchli qo'shtirnoqlar orasidagi kod blokini oladi
        filtered_code.append(block[0] or block[1] or block[2])
    
    return filtered_code

# Matn
text = """
This is some text.

```python
print('Hello, World!')
