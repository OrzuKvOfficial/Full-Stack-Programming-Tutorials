# Qidiruv funksiyasi
def search_in_json(data, keyword):
    results = []
    for key, value in data.items():
        if keyword.lower() in str(value).lower():
            results.append({key: value})
    return results

# Qidiruvni sinash
results = search_in_json(data, 'example')
print(results)
