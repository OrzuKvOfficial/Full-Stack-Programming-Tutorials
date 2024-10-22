companies = [
    ("Company A", 10000, 5000),  # (kompaniya nomi, daromad, foyda)
    ("Company B", 15000, 3000),
    ("Company C", 12000, 7000),
]

# Foyda (profit) bo'yicha saralash
companies_sorted = sorted(companies, key=lambda x: x[2], reverse=True)
for company in companies_sorted:
    print(company)
