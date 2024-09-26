# Qabul qilish bo'limi uchun Python dasturi

class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}"

class Reception:
    def __init__(self):
        self.patients_list = []

    def add_patient(self, name, age, ailment):
        new_patient = Patient(name, age, ailment)
        self.patients_list.append(new_patient)

    def show_all_patients(self):
        if self.patients_list:
            for patient in self.patients_list:
                print(patient.display_info())
        else:
            print("No patients in the list.")

# Qabul qilish bo'limi bilan ishlash
reception = Reception()

# Bemorlarni qo'shish
reception.add_patient("John Doe", 30, "Flu")
reception.add_patient("Jane Smith", 25, "Headache")

# Barcha bemorlarni ko'rsatish
reception.show_all_patients()
