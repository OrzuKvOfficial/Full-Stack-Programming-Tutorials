import json

def sort_json_file(input_file, output_file):
    """JSON faylini yuklab, ichki kalitlari bo'yicha tartiblaydi va yangi faylga saqlaydi."""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sorted_data = sort_json(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_data, f, indent=4, ensure_ascii=False)

def sort_json(data):
    """JSON obyektini rekursiv tarzda kalitlar bo'yicha tartiblaydi."""
    if isinstance(data, dict):
        return {k: sort_json(v) for k, v in sorted(data.items())}
    elif isinstance(data, list):
        return [sort_json(item) for item in data]
    else:
        return data

def sort_json_string(json_string):
    """JSON stringni tartiblaydi va qaytaradi."""
    data = json.loads(json_string)
    sorted_data = sort_json(data)
    return json.dumps(sorted_data, indent=4, ensure_ascii=False)

# Misol
if __name__ == "__main__":
    input_json = '{"name": "Orzubek", "age": 18, "city": "Tashkent", "skills": ["Python", "C++", "Java"]}'
    print("Saralangan JSON:")
    print(sort_json_string(input_json))
